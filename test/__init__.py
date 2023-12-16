from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

__all__ = (
    client
)