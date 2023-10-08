from src.database.db_mysql import get_connection
from src.models.TypeDocModel import TypeDocModel

class TypeDocService():
    # Get
    @classmethod
    def get_typeDoc(cls):
        try:
            connection = get_connection()
            typeDocs = []
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM TipoIdentificacion")
                resultTypeDoc = cursor.fetchall()
                for row in resultTypeDoc:
                    typeDoc = TypeDocModel(int(row[0]),row[1],row[2])
                    typeDocs.append(typeDoc.to_json())
            connection.commit()
            connection.close()
            return typeDocs
        except Exception as ex:
            print (ex)

    # Post
    @classmethod
    def add_typeDoc(cls, nameTypeDoc, stateTypeDoc):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                sql = 'INSERT INTO TipoIdentificacion VALUES ("", %s, %s)'
                data = (nameTypeDoc, stateTypeDoc,)
                cursor.execute(sql, data)
                
            connection.commit()  # Realizar commit de la transacción
            connection.close()
            return True
        except Exception as ex:
            print(ex)
            return False
        
    #Put
    @classmethod
    def put_typeDoc(cls, idTypeDoc, nameTypeDoc, stateTypeDoc):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                sql = 'UPDATE TipoIdentificacion SET nombreTipoIdentificacion = %s, estadoTipoIdentificacion = %s WHERE idTipoIdentificacion = %s'
                data = (nameTypeDoc, stateTypeDoc,idTypeDoc)
                cursor.execute(sql,data)
            connection.commit()
            connection.close()
            return True
        except Exception as ex:
            print(ex)
            return False


    # Delete 
    @classmethod
    def delete_typeDoc(cls, id):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                sql = 'Delete from TipoIdentificacion Where idTipoIdentificacion=%s'
                data = (id,)
                cursor.execute(sql, data)
            connection.commit()
            connection.close()
            return True
        except Exception as ex:
            print(ex)
            return False
        
