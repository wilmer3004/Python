# iterar diccionarios
diccionario = {
    "nombre": "Wilmer",
    "apellido" : "Capera",
    "edad":18
}

# Iterar la clave del diccionario
for key in diccionario:
    print(key)

# recorrer un diccionario con las claves y los valores
for element in diccionario.items():
    print(f"La clave es {element[0]} y el elemento es {element[1]}")






