"""A compact API-testing lab. Run with: pytest -q"""

from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()

@app.get('/v1/items/{item_id}')
def get_item(item_id: int):
    if item_id <= 0:
        return {'error': {'code': 'invalid_id'}}
    return {'id': item_id, 'status': 'active'}

client = TestClient(app)


def test_happy_path():
    response = client.get('/v1/items/42')
    assert response.status_code == 200
    assert response.json() == {'id': 42, 'status': 'active'}


def test_invalid_domain_input():
    response = client.get('/v1/items/0')
    assert response.status_code == 200
    assert response.json()['error']['code'] == 'invalid_id'


def test_validation_boundary():
    response = client.get('/v1/items/not-an-int')
    assert response.status_code == 422


# Exercises:
# - Move the app into src/ and tests into tests/.
# - Replace the function with a service/repository boundary.
# - Mock the repository failure and assert a 5xx response.
# - Add authentication and authorization tests.
# - Add parametrized tests for malformed payloads.
# - Add an integration test using a disposable PostgreSQL instance.
