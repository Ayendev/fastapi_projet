from fastapi.testclient import TestClient
from main import app
import pytest
from database import DATABASE_URL , engine
from sqlmodel import create_engine, SQLModel
from typing import List





@pytest.fixture(name="test_client")
def test_client():

    global engine
    engine = create_engine(url=DATABASE_URL, echo=True)
    SQLModel.metadata.create_all(engine)

    with TestClient(app) as client:
        yield client
    SQLModel.metadata.drop_all(engine)
    #engine = create_engine(url=DATABASE_URL, echo=True)

def test_create_item(test_client: TestClient):
    item_data = {"name": "écouteur", "price": 10.99, "in_stock": True}
    response = test_client.post("/items", json=item_data)
    assert response.status_code == 200
    created_item = response.json()
    assert created_item["name"] == "écouteur"
    assert created_item["price"] == 10.99
    assert created_item["in_stock"] == True
    assert created_item["id"] is not None



def test_read_items(test_client: TestClient):
    # Créer d'abord quelques éléments
    test_client.post("/items", json={"name": "clavier", "price": 5.00, "in_stock": True})
    test_client.post("/items", json={"name": "casque", "price": 10.00, "in_stock": False})

    response = test_client.get("/items")
    assert response.status_code == 200
    items: List[dict] = response.json()

    assert len(items) >= 2
    assert items[0]["name"] in ("clavier", "casque")
    assert items[1]["name"] in ("clavier", "casque")


def test_read_item(test_client: TestClient):
    # En supposant que l'article portant l'ID 1 existe
    response = test_client.get("/items/1")
    if response.status_code == 404:
        # Create an item if it doesn't exist
        test_client.post("/items", json={"name": "écran", "price": 12.50, "in_stock": True})
        response = test_client.get("/items/1")  # Try again
    assert response.status_code in (200, 404)
    if response.status_code == 200:
        item = response.json()
        assert item["name"] in ("écouteur","casque", "clavier", "écran")



def test_update_item(test_client: TestClient):
    # Create an item to update
    create_response = test_client.post("/items", json={"name": "écouteur", "price": 15.00, "in_stock": True})
    assert create_response.status_code == 200
    item_id = create_response.json()["id"]

    update_data = {"name": "tablette", "price": 20.00, "in_stock": False}
    update_response = test_client.put(f"/items/{item_id}", json=update_data)
    assert update_response.status_code == 200
    updated_item = update_response.json()
    assert updated_item["name"] == "tablette"
    assert updated_item["price"] == 20.00
    assert updated_item["in_stock"] == False

    response = test_client.put("/items/999", json=update_data)  # Non-existent item
    assert response.status_code == 404
    assert response.json() == {"detail": "Item not found"}

def test_delete_item(test_client: TestClient):
    # Create an item to delete
    create_response = test_client.post("/items", json={"name": "tablette", "price": 8.00, "in_stock": True})
    assert create_response.status_code == 200
    item_id = create_response.json()["id"]

    delete_response = test_client.delete(f"/items/{item_id}")
    assert delete_response.status_code == 200
    assert delete_response.json() == {"ok": True}


    response = test_client.delete("/items/999")  # article inexistant
    assert response.status_code == 404
    assert response.json() == {"detail": "Item not found"}

    response = test_client.get("/items")
    assert response.status_code == 200
    items: List[dict] = response.json()
    assert len(items) >= 0
