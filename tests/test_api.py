from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_upload():
    response = client.post("/upload", files={"file": ("filename", b"test data")})
    assert response.status_code == 200
    assert "ipfs_hash" in response.json()
