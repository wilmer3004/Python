from src.database.db_mysql import get_connection
from src.models.AmbienteModel import AmbienteModel

class AmbienteService():

    # Get
    @classmethod
    def get_ambiente(cls):
        try:
            connection = get_connection()
            ambientes = []
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM Ambiente")
                resultAmbiente = cursor.fetchall()
                for row in resultAmbiente:
                    ambiente = AmbienteModel(int(row[0]),row[1],row[2],row[3],row[4])
                    ambientes.append(ambiente.to_json())
            connection.commit()
            connection.close()
            return ambientes
        except Exception as ex:
            print(ex)
    
    # Post
    @classmethod
    def add_ambiente(cls,numeroAmbiente,horasDisponibles,estadoAmbiente,idSedeFK):
        try:
            connection1 = get_connection()
            with connection1.cursor() as cursor1:
                sql1='call SP_CodSedeAmbiente (%s)'
                data1=(idSedeFK,)
                cursor1.execute(sql1,data1)
                resultadoSede = cursor1.fetchone()
                print(resultadoSede)
            connection1.commit()
            connection1.close()    
            connection = get_connection()
            if resultadoSede != None:
                try:
                    with connection.cursor() as cursor:
                        sql = 'INSERT INTO Ambiente VALUES ("", %s, %s,%s,%s)'
                        data= (numeroAmbiente,horasDisponibles,estadoAmbiente,idSedeFK,)
                        cursor.execute(sql,data)
                    connection.commit()
                    connection.close()
                    return True
                except Exception as ex:
                    print(ex)
                    return False
            else:
                return 404
        except Exception as ex:
            print (ex)
            return False
    
    
    # Put
    @classmethod
    def put_ambiente(cls,idAmbiente,numeroAmbiente,horasDisponibles,estadoAmbiente,idSedeFK):
        try:
            connection1 = get_connection()
            with connection1.cursor() as cursor1:
                sql1='call SP_CodSedeAmbiente (%s)'
                data1=(idSedeFK,)
                cursor1.execute(sql1,data1)
                resultadoSede1 = cursor1.fetchone()
                print(resultadoSede1)
            connection1.commit()
            connection1.close()    
            connection = get_connection()
            if resultadoSede1 != None:
                try:
                    connection = get_connection()
                    with connection.cursor() as cursor:
                        sql = 'UPDATE Ambiente SET numeroAmbiente = %s, horasDisponibles = %s, estadoAmbiente = %s, idSedeFK= %s WHERE idAmbiente = %s'
                        data= (numeroAmbiente,horasDisponibles,estadoAmbiente,idSedeFK,idAmbiente)
                        cursor.execute(sql,data)
                    connection.commit()
                    connection.close()
                    return True
                except Exception as ex:
                    print(ex)
                    return False
            else:
                return 404
        except Exception as ex:
            print (ex)
            return False
        
    # Delete
    @classmethod
    def delete_ambiente(cls,idAmbiente):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                sql = 'Delete from Ambiente Where idAmbiente=%s'
                data= (idAmbiente,)
                cursor.execute(sql,data)
            connection.commit()
            connection.close()
            return True
        except Exception as ex:
            print(ex)
            return False
    # GET PUT
    @classmethod
    def get_update_ambiente(cls,idAmbiente):
        try:
            connection =  get_connection()
            with connection.cursor() as cursor:
                resultados_get_put = []
                sql = 'SELECT * FROM Ambiente WHERE idAmbiente = %s'
                data = (idAmbiente,)
                cursor.execute(sql,data)
                resultado_get_put=cursor.fetchall()
                for row in resultado_get_put:
                    print(row[0])
                    ambiente = AmbienteModel(int(row[0]),row[1],row[2],row[3],row[4])
                    resultados_get_put.append(ambiente.to_json())
            connection.commit()
            connection.close
            return resultados_get_put
        except Exception as ex:
            print(ex)



