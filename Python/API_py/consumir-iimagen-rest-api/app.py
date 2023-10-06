from flask import Flask, request
import pymysql
import base64

app = Flask(__name__)

def establecer_conexion():
    return pymysql.connect(host='localhost', user='root', password='', database='prubas')

@app.route('/subir_imagen', methods=['POST'])
def subir_imagen():
    try:
        data = request.json
        imagen_cifrada = data.get("imagenCifrada")

        # Decodificar la imagen cifrada desde base64
        imagen_bytes = base64.b64decode(imagen_cifrada)

        # Establecer conexión a la base de datos
        connection = establecer_conexion()

        # Insertar la imagen cifrada en la base de datos
        with connection.cursor() as cursor:
            sql = "INSERT INTO imagenes_cifradas (imagen_cifrada) VALUES (%s)"
            cursor.execute(sql, (imagen_bytes,))
            connection.commit()

        connection.close()

        return "Imagen cifrada almacenada correctamente en la base de datos", 200
    except Exception as e:
        print(str(e))
        return "Error al almacenar la imagen cifrada en la base de datos", 500

if __name__ == '__main__':
    app.run(debug=True, port=4000)