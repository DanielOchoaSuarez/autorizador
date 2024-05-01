import json
from faker import Faker
from src.main import app


fake = Faker()


class TestObtenerToken():

    def test_obtener_token_email(self):
        with app.test_client() as test_client:
            body = {"email": fake.email()}

            response = test_client.post(
                '/autorizador/seguridad/generar-token', json=body)
            response_json = json.loads(response.data)

            assert response.status_code == 200
            assert 'token' in response_json

    def test_obtener_token_todos_los_campos(self):
        with app.test_client() as test_client:
            body = {
                "email": fake.email(),
                "subscripcion": 'Premium',
                "tipo_usuario": 'deportista',
            }

            response = test_client.post(
                '/autorizador/seguridad/generar-token', json=body)
            response_json = json.loads(response.data)

            assert response.status_code == 200
            assert 'token' in response_json
