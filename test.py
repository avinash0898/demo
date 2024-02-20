# tests/test_app.py
from app import app

def test_index_route_success_status():
    response = app.test_client().get('/')
    assert response.status_code == 200
    
def test_index_route_success_text():
    response = app.test_client().get('/')
    assert response.data.decode('utf-8') == 'Hello, Docker!'
