from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Mock User Management API"}

def test_read_user_success():
    response = client.get("/users/42")
    assert response.status_code == 200
    user = response.json()
    assert user["id"] == 42
    assert user["username"] == "fastapi_dev"
    assert user["email"] == "py@example.com"
    assert user["is_active"] is True

def test_read_user_not_found():
    response = client.get("/users/1")
    assert response.status_code == 404
    assert response.json() == {"detail": "User not found"}

def test_create_user():
    user_data = {
        "id": 100,
        "username": "testuser",
        "email": "test@example.com",
        "is_active": True
    }
    response = client.post("/users/", json=user_data)
    assert response.status_code == 201
    assert response.json() == user_data
