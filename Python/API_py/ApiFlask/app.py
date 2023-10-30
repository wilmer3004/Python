from flask import Flask, request, jsonify
import mysql.connector
from flask_cors import CORS
import base64

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
# Configurar la conexión a la base de datos
database = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='',
    database='python1'
)

# Ruta para subir imágenes
@app.route('/upload', methods=['POST'])
def upload_file():
    data = request.json
    nombre = data.get('nombre')
    imagen_data = data.get('imagen')

    if not nombre or not imagen_data:
        return jsonify({'error': 'Datos incompletos'}), 400

    # Guardar el nombre y los datos binarios de la imagen en la base de datos
    try:
        cursor = database.cursor()
        cursor.execute("INSERT INTO usuario (nombre, imagen) VALUES (%s, %s)", (nombre, imagen_data))
        database.commit()
        return jsonify({'message': 'Imagen subida correctamente'}), 200
    except Exception as e:
        database.rollback()
        return jsonify({'error': 'Error al subir la imagen'}), 500
    finally:
        cursor.close()

@app.route('/imagenes', methods=['GET'])
def obtener_imagenes():
    try:
        cursor = database.cursor()
        cursor.execute("SELECT imagen FROM usuario")  # Suponiendo que la columna de imagen se llama 'imagen'
        imagenes = cursor.fetchall()

        # Convierte las imágenes a base64 y devuelve como respuesta
        imagenes_base64 = [base64.b64encode(imagen[0]).decode('utf-8') for imagen in imagenes]
        return jsonify({'imagenes': imagenes_base64}), 200
    except Exception as e:
        print(e)
        return jsonify({'error': 'Error al obtener las imágenes'}), 500
    finally:
        cursor.close()



if __name__ == '__main__':
    app.run(debug=True)
