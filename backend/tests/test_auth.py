
from fastapi.testclient import TestClient
from app.main import app
from app.schemas.user import UserLogin  


client = TestClient(app)

def test_register_user():
    response = client.post("/api/auth/register", json={
    "username": "username",
    "password": "mypassword123"  
})

    assert response.status_code == 201
    assert response.json()["username"] == "username"
    assert response.json()["role"] == "user"
def test_login_user():
    # First, register the user
    client.post("/api/auth/register", json={
        "username": "loginuser",
        "password": "mypassword123"
    })
    
    # Attempt login
    response = client.post("/api/auth/login", json={
        "username": "loginuser",
        "password": "mypassword123"
    })
    
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"
