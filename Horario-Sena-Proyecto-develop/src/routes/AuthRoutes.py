from flask import Blueprint,request, jsonify

# Entities
from src.models.AuthModel import AuthModel
# Models
from src.services.AuthService import AuthService
# Security
from src.utils.Security import Security

main = Blueprint('auth_Blueprint',__name__)

@main.routes('/',methods=['POST'])
def login():
    tipoDocumento = request.json['idTipoDocFK']
    numeroIdent = request.json['numeroIdent']
    contrasena = request.json['contrasenaUsuario']
    
    _autenticacion = AuthModel(0,tipoDocumento,numeroIdent,contrasena)
    autenticacion_usuario = AuthService.login_user(_autenticacion)
    
    if (autenticacion_usuario != None):
        generar_token = Security.generar_token(autenticacion_usuario)
        return jsonify({'success':True ,'token':generar_token})
    else:
        return jsonify({'success':False})
    




