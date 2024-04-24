import logging
from flask import Blueprint, request, jsonify, make_response
from src.commands.seguridad.obtener_token import ObtenerToken
from src.commands.seguridad.validar_token import ValidarToken


logger = logging.getLogger(__name__)
seguridad_blueprint = Blueprint('seguridad', __name__)


@seguridad_blueprint.route('/generar-token', methods=['POST'])
def generar_token():
    body = request.get_json()
    info = {
        'email': body.get('email', None),
        'subscripcion': body.get('subscripcion', None),
        'tipo_usuario': body.get('tipo_usuario', None)
    }
    result = ObtenerToken(**info).execute()
    return make_response(jsonify({'token': result}), 200)


@seguridad_blueprint.route('/validar-token', methods=['POST'])
def validar_token():
    body = request.get_json()
    result = ValidarToken(body.get('token', None)).execute()
    return make_response(jsonify(result), 200)
