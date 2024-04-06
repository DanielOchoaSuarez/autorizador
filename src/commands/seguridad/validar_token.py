import os
import jwt
import logging
from src.commands.base_command import BaseCommand


jwt_secret_key = os.getenv('JWT_SECRET_KEY', 'laad')
logger = logging.getLogger(__name__)


class ValidarToken(BaseCommand):
    def __init__(self, token: str):
        self.token = token

    def execute(self):
        logger.info(f'Validando Token {self.token}')

        try:
            data = jwt.decode(self.token, jwt_secret_key, algorithms=["HS256"])
            logger.info(f'Token válido para {data.get("email")}')
            return {'token_valido': True, 'email': data.get('email')}
        except Exception as e:
            logger.error(f'Error al validar token {e}')
            return {'token_valido': False}
