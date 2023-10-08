from src.database.db_mysql import get_connection
from src.models.ProgramaModel import ProgramaModel

class ProgramaService():
    @classmethod
    #get
    def get_programa(cls):
        try:
            connection = get_connection()
            programas = []
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM Programa")
                resultPrograma = cursor.fetchall()
                for row in resultPrograma:
                    programa = ProgramaModel(int(row[0]),row[1],row[2],row[3],row[4])
                    programas.append(programa.to_json())
                connection.commit()
                connection.close()
                print(programas)
                return programas
        except Exception as ex:
            print(ex)

    @classmethod
    # Post
    def add_Programa(cls, nombrePrograma, descripcionProgram,versionPrograma,estadoPrograma):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                sql = 'insert into programa values ("",%s,%s,%s,%s);'
                data = (nombrePrograma, descripcionProgram,versionPrograma,estadoPrograma)
                cursor.execute(sql, data)
                
            connection.commit()  # Realizar commit de la transacción
            connection.close()
            return True
        except Exception as ex:
            print(ex)
            return False

    # Put
    @classmethod
    def put_programa(cls, idPrograma,nombrePrograma,descripcionProgram, versionPrograma, estadoPrograma):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                sql = 'UPDATE programa SET nombrePrograma = %s, descripcionProgram = %s, versionPrograma=%s, estadoPrograma=%s WHERE idPrograma = %s'
                data = (nombrePrograma,descripcionProgram,versionPrograma,estadoPrograma, idPrograma)
                cursor.execute(sql,data)
            connection.commit()
            connection.close()
            return True
        except Exception as ex:
            print(ex)
            return False
        
    # Delete
    @classmethod
    def delete_programa(cls, idPrograma):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                sql = 'Delete from Programa Where idPrograma=%s'
                data = (idPrograma,)
                cursor.execute(sql, data)
            connection.commit()
            connection.close()
            return True
        except Exception as ex:
            print(ex)
            return False

# GET PUT
    @classmethod
    def get_update_Programa(cls,idPrograma):
        try:
            connection =  get_connection()
            with connection.cursor() as cursor:
                resultados_get_put = []
                sql = 'SELECT * FROM Programa WHERE idPrograma = %s'
                data = (idPrograma,)
                cursor.execute(sql,data)
                resultado_get_put=cursor.fetchall()
                for row in resultado_get_put:
                    print(row[0])
                    programa = ProgramaModel(int(row[0]),row[1],row[2],row[3],row[4])
                    resultados_get_put.append(programa.to_json())
            connection.commit()
            connection.close
            return resultados_get_put
        except Exception as ex:
            print(ex)
    
    