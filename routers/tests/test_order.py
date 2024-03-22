from fastapi.testclient import TestClient
from ...main import app

client = TestClient(app)

def test_create_order():
    response = client.post('/orders', json={'customer_id': 1, 'items': [2, 3]})
    assert response.status_code == 201
    assert response.json().get('data').get('customer_id') == 1
    assert response.json().get('data').get('items') == [2, 3]

def test_get_orders():
    response = client.get('/orders')
    assert response.status_code == 200
    assert len(response.json().get('data')) == 2

def test_process_order():
    response = client.put('/orders/1')
    assert response.status_code == 201
    assert response.json().get('data').get('status') == 'COMPLETED'