from fastapi.testclient import TestClient

from api.main import app


client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "DataForge API is running"
    }


def test_get_customer():
    response = client.get("/customers/101")

    assert response.status_code == 200

    data = response.json()

    assert data["customer_id"] == 101
    assert data["name"] == "Rahul Patil"
    assert data["city"] == "Pune"


def test_customer_not_found():
    response = client.get("/customers/999999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Customer not found"