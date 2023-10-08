from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import base64

def cifrar_imagen(imagen_path, clave):
    with open(imagen_path, 'rb') as file:
        imagen_bytes = file.read()

    # Generar un vector de inicialización (IV) aleatorio
    iv = b'1234567890123456'  # 16 bytes para AES

    # Crear un objeto AES con la clave y el IV
    cipher = Cipher(algorithms.AES(clave), modes.CFB(iv), backend=default_backend())

    # Cifrar la imagen
    encryptor = cipher.encryptor()
    imagen_cifrada = encryptor.update(imagen_bytes) + encryptor.finalize()

    # Convertir la imagen cifrada a base64
    imagen_base64 = base64.b64encode(imagen_cifrada).decode('utf-8')

    return imagen_base64

# Ejemplo de uso
if __name__ == "__main__":
    # Ruta de la imagen que deseas cifrar
    imagen_path = 'imagen.jpg'

    # Clave secreta para cifrar la imagen (debe tener 16, 24 o 32 bytes para AES-128, AES-192 o AES-256 respectivamente)
    clave = b'mi_clave_secreta_de_16_bytes'

    # Cifrar la imagen
    imagen_cifrada_base64 = cifrar_imagen(imagen_path, clave)

    # Imprimir la imagen cifrada en base64
    print(imagen_cifrada_base64)