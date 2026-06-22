from pathlib import Path

from fastapi.testclient import TestClient

import modules.uploader as uploader
from main import app


client = TestClient(app)


def test_create_file_no_file_returns_message():
    response = client.post("/files/")

    assert response.status_code == 200
    assert response.json() == {"message": "No file present"}


def test_create_upload_file_writes_file(tmp_path, monkeypatch):
    monkeypatch.setattr(uploader, "UPLOAD_DIR", tmp_path)
    tmp_path.mkdir(exist_ok=True)

    response = client.post(
        "/uploadfile/",
        files={"file": ("hello.txt", b"hello world", "text/plain")},
    )

    assert response.status_code == 200
    body = response.json()
    assert body["filename"] == "hello.txt"
    assert body["content_type"] == "text/plain"
    assert body["size"] == len(b"hello world")

    output_path = Path(body["path"])
    assert output_path.exists()
    assert output_path.read_bytes() == b"hello world"
