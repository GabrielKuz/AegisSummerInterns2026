import asyncio
from urllib import response
from fastapi.testclient import TestClient
from main import app
from modules.LinkGenerator import LinkRequest, generate_links, get_all_links
from datetime import datetime, timedelta
from modules.auth import User, getCurrentActiveUser
import os


client = TestClient(app)
current_user = User(username="testuser", disabled=False)  # Mock user for testing
url = f"{os.getenv('BACKEND_URL')}/backend/links/"  # Assuming this is the base URL for links

async def override_get_current_active_user() -> User:
    return User(username="testuser", disabled=False)

app.dependency_overrides[getCurrentActiveUser] = override_get_current_active_user

def test_generate_links_returns_link_and_uuid():
    link_request = LinkRequest(
        case_id="case-123",
        itar=False
    )

    result = generate_links(link_request, current_user)

    assert result["link"].startswith(url)
    assert result["uuid"]
    assert result["link"].endswith(result["uuid"])


def test_create_link_endpoint_returns_generated_link():
    payload = {
        "case_id": "case-123",
        "itar": False
    }
    
    response = client.post("/links/create/", json=payload)

    assert response.json()["link"].startswith(url)
    assert response.json()["uuid"]



def test_store_link_persists_data():
    link_request = LinkRequest(
        case_id="case-456",
        itar=False
    )

    result = generate_links(link_request, current_user)

    # Fetch the link from the database using the returned UUID
    uuid = result["uuid"]
    response = client.get(f"/links/{uuid}")

    assert response.status_code == 200
    data = response.json()
    assert data["uuid"] == uuid
    assert data["link"].endswith(uuid)
    assert data["case_id"] == "case-456"
    assert data["itar"] is False
    assert data["creator"]  # Assuming the creator is set to the current user
    assert data["timestamp"]  # Assuming the timestamp is set to the current time
    assert data["users_with_access"]  # Assuming the current user is added to the access list
    assert data["expired"] is False
    assert data["expiration_date"]  # Assuming the expiration date is set to 2 days from now

def test_get_all_links_returns_links_for_user():
    # Create a link for the test user
    link_request = LinkRequest(
        case_id="case-789",
        itar=False
    )
    generate_links(link_request, current_user)

    response = client.get("/links/")

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert any(link["case_id"] == "case-789" for link in data)  # Check if the created link is in the list
