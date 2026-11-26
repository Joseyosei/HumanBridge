from fastapi.testclient import TestClient
from main import app
client = TestClient(app)

def test_health():
    assert client.get('/health').json()['status'] == 'ok'

def test_plan():
    for barrier in ['confidence','time','finding_people']:
        response = client.post('/v1/plan',json={'barrier':barrier})
        assert response.status_code == 200
        assert response.json()['mode'] == 'rule_based_demo'

def test_invalid_barrier():
    assert client.post('/v1/plan',json={'barrier':'invalid'}).status_code == 422
