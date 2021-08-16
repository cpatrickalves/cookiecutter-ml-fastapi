from starlette.testclient import TestClient
from pprint import pprint
from src.api.main import api
from myproject import settings

# TODO: should I use settings.py
# TODO Use dotenv ou decouple package?

client = TestClient(api)

def test_status():
    response = client.get("/status")
    assert response.status_code == 200
    assert response.json() == {"status": "online", "api_version": settings.API_VERSION}

