from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_register_user():
    response = client.post("/api/auth/register", json={
    "username": "sakhi",
    "password": "mypassword123"  # <= short, safe password
})

    assert response.status_code == 201
    assert response.json()["username"] == "sakhi"
    assert response.json()["role"] == "user"
