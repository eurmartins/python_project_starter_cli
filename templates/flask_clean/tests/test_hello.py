import pytest
from app import create_app

@pytest.fixture
def app():
    app = create_app()
    return app

def test_hello(client):
    response = client.get('/hello')
    assert response.status_code == 200
    assert b'Hello, World!' in response.data