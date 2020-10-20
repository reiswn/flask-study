import pytest
from app import create_app

@pytest.fixture
def app():
    app = create_app()
    app.testing = True
    return app

def test_hello_world_route_200(client):
    resp = client.get('/')
    assert resp.status_code == 200

def test_hello_world_content(client):
    resp = client.get('/')
    assert resp.get_data(as_text=True) == 'Hello, World!'

def test_redirect_route(client):
    resp = client.get('/redirect', follow_redirects=True)
    assert resp.get_data(as_text=True) == 'Hello, World!'