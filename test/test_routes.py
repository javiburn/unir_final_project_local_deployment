import pytest

import sys
import os

# Agrega la carpeta raíz del proyecto al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.routes import db
from app.models import Data
from app import create_app


@pytest.fixture
def client():
    app = create_app("testing")
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URI")
    
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def test_insert_data_success(client):
    response = client.post("/data", json={"name": "Test Item"})
    assert response.status_code == 200
    assert response.get_json()["message"] == "Data inserted successfully"


def test_insert_duplicate_data(client):
    client.post("/data", json={"name": "Duplicate Item"})
    response = client.post("/data", json={"name": "Duplicate Item"})
    assert response.status_code == 409
    assert response.get_json()["message"] == "Data already exists"


def test_get_all_data(client):
    client.post("/data", json={"name": "Item 1"})
    client.post("/data", json={"name": "Item 2"})
    response = client.get("/data")
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) == 2


def test_delete_data_success(client):
    client.post("/data", json={"name": "To Delete"})
    response = client.get("/data")
    item_id = response.get_json()[0]["id"]

    delete_response = client.delete(f"/data/{item_id}")
    assert delete_response.status_code == 200
    assert delete_response.get_json()["message"] == "Data deleted successfully"


def test_delete_data_not_found(client):
    response = client.delete("/data/999")
    assert response.status_code == 404
    assert response.get_json()["message"] == "Data not found"