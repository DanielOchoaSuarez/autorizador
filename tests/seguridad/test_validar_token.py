import json
from faker import Faker
from src.main import app


fake = Faker()


class TestValidarToken():

    def test_validar_token_valido(self):
        with app.test_client() as test_client:
            email_random = fake.email()
            body_get_token = {
                "email": email_random,
                "subscripcion": 'Premium',
                "tipo_usuario": 'deportista',
            }

            response = test_client.post(
                '/autorizador/seguridad/generar-token', json=body_get_token)
            response_token = json.loads(response.data)
            body = {"token": response_token['token']}

            resp = test_client.post(
                '/autorizador/seguridad/validar-token', json=body)
            response_json = json.loads(resp.data)

            assert resp.status_code == 200
            assert 'token_valido' in response_json
            assert response_json['token_valido'] == True
            assert 'email' in response_json
            assert response_json['email'] == email_random

    def test_validar_token_invalido(self):
        with app.test_client() as test_client:
            body = {"token": "token_invalido"}

            response = test_client.post(
                '/autorizador/seguridad/validar-token', json=body)

            response_json = json.loads(response.data)
            assert response.status_code == 200
            assert 'token_valido' in response_json
            assert response_json['token_valido'] == False
