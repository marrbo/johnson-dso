import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_secure_data_unauthorized():
    response = client.get("/secure-data")
    assert response.status_code == 401
    assert response.json() == {"detail": "Not authenticated"}