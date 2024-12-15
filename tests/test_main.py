from fastapi.testclient import TestClient
import pytest
from app.main import app
from app.database import Base, engine

client = TestClient(app)

@pytest.fixture(scope="module")
def setup_database():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

def test_add_purchases(setup_database):
    response = client.post("/purchases", json={
        "user_id": "user123",
        "cart": [
            {"item_id": "item123", "category": "fruits"},
            {"item_id": "item456", "category": "dairy"}
        ]
    })
    assert response.status_code == 200
    assert response.json() == {"status": "purchases_added"}

def test_generate_recommendations(setup_database):
    response = client.post("/generate_recommendations", json={"user_id": "user123"})
    assert response.status_code == 200
    assert response.json() == {"status": "recommendations_generation_started"}

def test_get_recommendations(setup_database):
    response = client.get("/recommendations", params={"user_id": "user123"})
    assert response.status_code == 200
    assert "recommendations" in response.json()
