import os
import jwt
import logging
from src.commands.base_command import BaseCommand


jwt_secret_key = os.getenv('JWT_SECRET_KEY', 'laad')
logger = logging.getLogger(__name__)


class ObtenerToken(BaseCommand):
    def __init__(self, **info):
        self.email = info['email']
        self.subscripcion = info['subscripcion']
        self.tipo_usuario = info['tipo_usuario']

    def execute(self):
        informacion_token = {
            'email': self.email,
        }

        if self.subscripcion:
            informacion_token['subscripcion'] = self.subscripcion

        if self.tipo_usuario:
            informacion_token['tipo_usuario'] = self.tipo_usuario

        token = jwt.encode(informacion_token,
                           jwt_secret_key, algorithm='HS256')

        logger.info(f'Token generado para {self.email}')
        return token
