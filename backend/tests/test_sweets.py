from fastapi.testclient import TestClient
from app.main import app
from app.schemas.sweet import SweetCreate

client = TestClient(app)

def test_create_sweet():
    sweet_data = {
        "name": "Chocolate",
        "category": "Candy",
        "price": 10.5,
        "quantity": 100
    }
    response = client.post("/api/sweets", json=sweet_data)
    assert response.status_code == 201
    assert response.json()["name"] == "Chocolate"
