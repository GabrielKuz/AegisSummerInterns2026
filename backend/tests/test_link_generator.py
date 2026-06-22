from fastapi.testclient import TestClient

from main import app
from modules.LinkGenerator import LinkRequest, generate_links


client = TestClient(app)


def test_generate_links_returns_link_and_uuid():
    link_request = LinkRequest(
        case_id="case-123",
    )

    result = generate_links(link_request)

    assert result["link"].startswith("http://localhost:8000/backend/links/")
    assert result["uuid"]
    assert result["link"].endswith(result["uuid"])


def test_create_link_endpoint_returns_generated_link():
    payload = {
        "case_id": "case-123",
    }

    response = client.post("/links/create/", json=payload)

    assert response.status_code == 201
    assert response.json()["link"].startswith("http://localhost:8000/backend/links/")
    assert response.json()["uuid"]
