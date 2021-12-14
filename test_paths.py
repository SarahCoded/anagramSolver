from flask import Flask, request
from main import app as create_app
import pytest

app = Flask(__name__)

def test_start():
    assert b'Path testing is running'

@pytest.fixture
def client():
    with create_app.test_client() as client:
        yield client

with app.test_request_context('/'):
    assert request.path == '/'

with app.test_request_context('/submit'):
    assert request.path == '/submit'

def test_call_is_200(client):
    r = client.get('/')
    assert r.status_code == 200

def test_call_is_404(client):
    r = client.get('/invalid_url')
    assert r.status_code == 404

def test_call_is_405(client):
    r = client.post('/')
    assert r.status_code == 405
    