from fastapi.testclient import TestClient
from app.main import app
from app.schemas.sweet import SweetCreate
import random
client = TestClient(app)

def test_create_sweet():
    sweet_name = f"Chocolate{random.randint(1,10000)}"
    sweet_data = {
        "name": sweet_name,
        "category": "Candy",
        "price": 10.5,
        "quantity": 100
    }
    response = client.post("/api/sweets", json=sweet_data)
    assert response.status_code == 201
    assert response.json()["name"] == sweet_name

def test_search_sweet():
    response = client.get("/api/sweets/search?name=Chocolate")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_update_sweet():
    # First, create a sweet
    sweet_name = f"Chocolate{random.randint(1,10000)}"
    response = client.post("/api/sweets", json={"name": sweet_name, "category": "Candy", "price":10, "quantity":10})
    sweet_id = response.json()["id"]
    
    sweet_data = {"price": 12.0}
    response = client.put(f"/api/sweets/{sweet_id}", json=sweet_data)
    assert response.status_code == 200
    assert response.json()["price"] == 12.0


def test_delete_sweet():
    create_response = client.post("/api/sweets", json={
        "name": "Ladoo",
        "category": "Indian",
        "price": 10,
        "quantity": 5
    })

    sweet_id = create_response.json()["id"]

    response = client.delete(f"/api/sweets/{sweet_id}")
    assert response.status_code == 204


def test_purchase_sweet():
    sweet_name = f"Candy{random.randint(1,10000)}"
    response = client.post("/api/sweets", json={"name": sweet_name, "category": "Candy", "price":5.0, "quantity":10})
    sweet_id = response.json()["id"]
    
    response = client.post(f"/api/sweets/{sweet_id}/purchase")
    assert response.status_code == 200
    assert response.json()["quantity"] == 9


def test_restock_sweet():
    sweet_name = f"Candy{random.randint(1,10000)}"
    response = client.post("/api/sweets", json={"name": sweet_name, "category": "Candy", "price":5.0, "quantity":10})
    sweet_id = response.json()["id"]
    
    response = client.post(f"/api/sweets/{sweet_id}/restock", params={"quantity":5})
    assert response.status_code == 200
    assert response.json()["quantity"] == 15

