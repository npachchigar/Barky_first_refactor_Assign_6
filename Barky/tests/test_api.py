import pytest
import requests

from flask import url_for

from api.flaskapi import FlaskBookmarkAPI

LOCALHOST = 'http://127.0.0.1:5000/'

def test_api_can_connect():
    res = requests.get(LOCALHOST)
    assert res != None

def test_api_index():
    res = requests.get(LOCALHOST)
    assert res != None

@pytest.fixture
def api():
    return FlaskBookmarkAPI()

def test_index(api):
    response = requests.get(LOCALHOST + '')
    assert response.status_code == 200
    assert response.data == b'Barky API'

def test_one(api):
    response = requests.get(LOCALHOST + 'api/one/123')
    assert response.status_code == 200
    assert response.data == f'The provided id is 123'

def test_all(api):
    with app.test_client() as client:
        response = client.get('/api/all')
        assert response.status_code == 200
        assert response.data == b'all records'

def test_first(api):
    with app.test_client() as client:
        response = client.get('/api/first/property/value/sort')
        assert response.status_code == 200
        assert response.data == b'the first '

def test_many(api):
    with app.test_client() as client:
        response = client.get('/api/many/property/value/sort')
        assert response.status_code == 200
        assert response.data == b'many records'