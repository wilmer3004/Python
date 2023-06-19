diccionario ={
    "nombre":"Wilmer",
    "apellido":"Capera",
    "edad":18
}


# métodos

# Keys sirven para regresar las claves del diccionario y también sirve para iterar al ser devuelto dun objeto tipo dict_item

claves = diccionario.keys()
print(claves)

# get sirve para mostrar un valor

get = diccionario.get("nombre")
print(get)

# Elimina un elemento del diccionario
diccionario.pop("nombre")
print(diccionario)

# Devuelve exactamente lo que se encuentra en el diccionario con el elemento dict_items iterable
diccionario_iterable = diccionario.items()

print(diccionario_iterable)
# clear elimina todos los elementos del diccionario

diccionario.clear()
print(diccionario)

