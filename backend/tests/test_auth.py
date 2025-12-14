
from fastapi.testclient import TestClient
from app.main import app
from app.schemas.user import UserLogin  
import random

client = TestClient(app)

def test_register_user():
    username = f"user{random.randint(1,10000)}"  # unique username every time
    response = client.post("/api/auth/register", json={
        "username": username,
        "password": "mypassword123"
    })
    assert response.status_code == 201
    assert response.json()["username"] == username
    
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
