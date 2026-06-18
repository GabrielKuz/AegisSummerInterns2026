from fastapi.testclient import TestClient

from main import app
from modules.LinkGenerator import LinkRequest, generate_links


client = TestClient(app)


def test_generate_links_returns_expected_link():
    link_request = LinkRequest(
        users_with_access=["alice"],
        case_id="case-123",
        link="http://example.com",
        creator="bob",
        timestamp="2026-06-18T00:00:00Z",
        uuid="uuid-123",
    )

    result = generate_links(link_request)

    assert result["link"] == "http://example.com/links/uuid-123"
    assert result["users_with_access"] == ["alice"]
    assert result["case_id"] == "case-123"
    assert result["creator"] == "bob"
    assert result["timestamp"] == "2026-06-18T00:00:00Z"


def test_create_link_endpoint_returns_generated_link():
    payload = {
        "users_with_access": ["alice"],
        "case_id": "case-123",
        "link": "http://example.com",
        "creator": "bob",
        "timestamp": "2026-06-18T00:00:00Z",
        "uuid": "uuid-123",
    }

    response = client.post("/backend/links/", json=payload)

    assert response.status_code == 200
    assert response.json()["link"] == "http://example.com/links/uuid-123"
