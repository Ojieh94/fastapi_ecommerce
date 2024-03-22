from fastapi.testclient import TestClient
from ...main import app

client = TestClient(app)

def test_create_product():
    response = client.post('/products', json={'name': 'Pampers', 'price': '150.00' , 'quantity_available': 5})
    assert response.status_code == 201
    assert response.json().get('data').get('name') == 'Pampers'
    assert response.json().get('data').get('price') == '150.00'

def test_get_product():
    response = client.get('/products')
    assert response.status_code == 200
    assert len(response.json().get('data')) == 5
    
def test_edit_product():
    response = client.put('/products/3', json={'name': 'Biscuit', 'price': '50.00', 'quantity_available': 25})
    assert response.status_code == 200
    assert response.json().get('data').get('name') == 'Biscuit'
    assert response.json().get('data').get('price') == '50.00'