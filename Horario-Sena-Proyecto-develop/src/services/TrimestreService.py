from src.database.db_mysql import get_connection
from src.models.TrimestreModel import TrimestreModel
from datetime import datetime


class TrimestreService():
    # Get
    @classmethod
    def get_timestre(cls):
        try:
            connection = get_connection()
            trimestres = []
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM Trimestre")
                resultTrimestre = cursor.fetchall()
                for row in resultTrimestre:
                    fecha_inicio = row[2].strftime('%Y-%m-%d')
                    fecha_fin = row[3].strftime('%Y-%m-%d')
                    trimestre = TrimestreModel(int(row[0]),row[1],fecha_inicio,fecha_fin,row[4])
                    trimestres.append(trimestre.to_json())
                connection.commit()
                connection.close()
                return trimestres
        except Exception as ex:
            print(ex)


    # Post
    @classmethod
    def add_trimestre(cls, nombreTrimestre, fechaInicio, fechaFin, estadoTrimestre):
        try:
             # Convertir las cadenas de fecha a objetos datetime
            fechaInicio_obj = datetime.strptime(fechaInicio, '%Y-%m-%d').date()
            fechaFin_obj = datetime.strptime(fechaFin, '%Y-%m-%d').date()
            connection = get_connection()
            try:
                with connection.cursor() as cursor:
                    sql = 'INSERT INTO Trimestre VALUES ("", %s, %s, %s, %s)'
                    data = (nombreTrimestre, fechaInicio_obj, fechaFin_obj, estadoTrimestre,)
                    cursor.execute(sql, data)
                connection.commit()
                connection.close()
                return True
            except Exception as ex:
                print(ex)
                return False
        except Exception as ex:
            print(ex)
            return False

    # Put
    @classmethod
    def put_trimestre(cls,idTrimestre, nombreTrimestre, fechaInicio, fechaFin, estadoTrimestre):
        try:
             # Convertir las cadenas de fecha a objetos datetime
            fechaInicio_obj = datetime.strptime(fechaInicio, '%Y-%m-%d').date()
            fechaFin_obj = datetime.strptime(fechaFin, '%Y-%m-%d').date()
            connection = get_connection()
            try:
                with connection.cursor() as cursor:
                    sql = 'UPDATE Trimestre SET nombreTrimestre = %s, fechaInicio = %s, fechaFin = %s, estadoTrimestre = %s WHERE idTrimestre = %s  '
                    data = (nombreTrimestre, fechaInicio_obj, fechaFin_obj, estadoTrimestre,idTrimestre,)
                    cursor.execute(sql, data)
                connection.commit()
                connection.close()
                return True
            except Exception as ex:
                print(ex)
                return False
        except Exception as ex:
            print(ex)
            return False
    # Delete
    @classmethod
    def delete_trimestre(cls, idTrimestre):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                sql = 'Delete from Trimestre Where idTrimestre=%s'
                data = (idTrimestre,)
                cursor.execute(sql, data)
            connection.commit()
            connection.close()
            return True
        except Exception as ex:
            print(ex)
            return False
    
    # GET PUT
    @classmethod
    def get_update_Trimestre(cls,idTrimestre):
        try:
            connection =  get_connection()
            with connection.cursor() as cursor:
                resultados_get_put = []
                sql = 'SELECT * FROM Trimestre WHERE idTrimestre = %s'
                data = (idTrimestre,)
                cursor.execute(sql,data)
                resultado_get_put=cursor.fetchall()
                for row in resultado_get_put:
                    fecha_inicio = row[2].strftime('%Y-%m-%d')
                    fecha_fin = row[3].strftime('%Y-%m-%d')
                    ambiente = TrimestreModel(int(row[0]),row[1],fecha_inicio,fecha_fin,row[4])
                    resultados_get_put.append(ambiente.to_json())
            connection.commit()
            connection.close
            return resultados_get_put
        except Exception as ex:
            print(ex)
    
    
    
    