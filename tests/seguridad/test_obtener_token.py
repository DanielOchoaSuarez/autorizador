import json
from faker import Faker
from src.main import app


fake = Faker()


class TestObtenerToken():

    def test_health(self):
        with app.test_client() as test_client:
            body = {"email": fake.email()}

            response = test_client.post(
                '/autorizador/seguridad/generar-token', json=body)
            response_json = json.loads(response.data)

            assert response.status_code == 200
            assert 'token' in response_json
