# Creando diccionarios con dict
diccionario = dict(nombre = "Wilmer",apellido="Capera")

print(diccionario)

# Creando diccionarios con dict.fromkeys() esto crea unicamente las claves y deja todos los valores como nulos
diccionario = dict.fromkeys(("nombre","apellido"))
print(diccionario)
# El primero es un iterable y el segundo es el valor por defecto que tendrán
diccionario= dict.fromkeys(["nombre","apellido"],"no se")
print(diccionario)





 
