import os
import jwt
import logging
from src.commands.base_command import BaseCommand


jwt_secret_key = os.getenv('JWT_SECRET_KEY', 'laad')
logger = logging.getLogger(__name__)


class ObtenerToken(BaseCommand):
    def __init__(self, email: str):
        self.email = email
        pass

    def execute(self):
        token = jwt.encode({'email': self.email},
                           jwt_secret_key, algorithm='HS256')
        logging.info(f'Token generado para {self.email}')
        return token
