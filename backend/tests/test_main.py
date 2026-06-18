from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_read_root_returns_ok_status():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}