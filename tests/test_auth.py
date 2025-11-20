import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_register_and_login():
    # Register a new user
    import uuid
    unique_email = f"pytestuser_{uuid.uuid4().hex[:8]}@example.com"
    response = client.post("/api/v1/auth/register", json={
        "email": unique_email,
        "password": "pytestpass123"
    })
    print(response.json())
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    token = data["access_token"]

    # Login with the same user
    response = client.post("/api/v1/auth/login", json={
        "email": unique_email,
        "password": "pytestpass123"
    })
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert isinstance(data["access_token"], str)
