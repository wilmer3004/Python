# Database
from src.database.db_mysql import get_connection
# Errors
from src.utils.errors.ManejoExcepciones import ManejoExcepciones
# Models
from src.models.AuthModel import AuthModel

class AuthService():
    
    @classmethod
    def login_user(cls,usuario):
        try:
            connection = get_connection()
            autenticacion_usuario = None
            with connection.cursor() as cursor:
                sql = 'call sp_verificacion_usuario(%s,%s,%s)'
                data = (usuario.tipoDocumento,usuario.numeroIdent,usuario.constrasena)
                cursor.execute()

                
        except Exception as ex:
            print(ex)








