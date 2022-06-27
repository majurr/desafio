from urllib import response

import pytest
from app.api.main import app
from starlette.testclient import TestClient

client = TestClient(app)


@pytest.fixture(scope="module")
def test_root():
    response = client.get("/")
    assert response.status_code == 200
