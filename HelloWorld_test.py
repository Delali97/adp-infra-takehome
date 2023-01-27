import pytest

from flask.testing import FlaskClient
from app import app
@pytest.fixture(scope='module')



def client():
    return app.test_client()


def test_get_home(client: FlaskClient):
    """should be a successful GET request"""
    resp = client.get('/')
    assert resp.status_code == 200
    

def test_post_home(client: FlaskClient):
    """should be a successful POST request"""
    resp = client.post('/')
    assert resp.status_code == 200
    assert resp.json["message"] == "Empty POST request"

def test_no_accept_header(client: FlaskClient):
    """a request with header.accept not json/application should return a byte 'Hello, World"""
    resp = client.get('/')
    assert b"Hello, World" in resp.data
    


def test_accept_header_json_application(client: FlaskClient):
    """a request with header.accept = json/application should return a json object {message: Hello World"""
    resp = client.get('/', headers={"Accept": "application/json"})
    assert resp.status_code == 200
    assert resp.json["message"] == "Hello, World"