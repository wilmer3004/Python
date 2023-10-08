from src.database.db_mysql import get_connection
from src.models.JornadaModel import JornadaModel

class JornadaService():
    # Get
    @classmethod
    def get_jornada(cls):
        try:
            connection = get_connection()
            jornadas = []
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM jornada")
                resultTypeDoc = cursor.fetchall()
                for row in resultTypeDoc:
                    typeDoc = JornadaModel(int(row[0]),row[1],row[2],row[3],row[4])
                    jornadas.append(typeDoc.to_json())
            connection.commit()
            connection.close()
            return jornadas
        except Exception as ex:
            print (ex)

     # Post
    @classmethod
    def add_Jornada(cls, nameJornada, diaIniJor,diaFinJor,estadoJornada):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                sql = 'INSERT INTO jornada VALUES ("", %s, %s,%s,%s)'
                data = (nameJornada, diaIniJor,diaFinJor,estadoJornada)
                cursor.execute(sql, data)
                
            connection.commit()  # Realizar commit de la transacción
            connection.close()
            return True
        except Exception as ex:
            print(ex)
            return False

    # Put
    @classmethod
    def put_jornada(cls, idJornada,nameJornada, diaIniJor, diaFinJor,estadoJornada):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                sql = 'UPDATE jornada SET nombreJornada = %s, diaIniJor = %s, diaFinJor=%s, estadoJornada=%s WHERE idJornada = %s'
                data = (nameJornada,diaIniJor,diaFinJor,estadoJornada,idJornada)
                cursor.execute(sql,data)
            connection.commit()
            connection.close()
            return True
        except Exception as ex:
            print(ex)
            return False
        

    # Delete 
    @classmethod
    def delete_jornada(cls, id):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                sql = 'Delete from jornada Where idJornada=%s'
                data = (id,)
                cursor.execute(sql, data)
            connection.commit()
            connection.close()
            return True
        except Exception as ex:
            print(ex)
            return False