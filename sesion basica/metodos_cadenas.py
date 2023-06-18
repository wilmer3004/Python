cadena = "Hola Wilmer como estas"

#function dir

# # El método dir devuelve todos los métodos que pueden intervenir con el tipo de dato que le demos
# print(dir(cadena))

# Upper
resultado =cadena.upper()

print(resultado)


# Lower

resultado =cadena.lower()

print(resultado)

# capitalize

resultado =cadena.capitalize()

print(resultado)

# Retornar un tipo de valor

# find buscar una cadena en otra en caso de que no este el valor regresa un -1

resultado =cadena.find("H")

print(resultado)

# index buscamos una cadena en otra aca nos lanza un error

resultado =cadena.index("o")

print(resultado)


# Se consulta si el dato indicado es numérico

numero = "23243"
is_number = numero.isnumeric()

print(is_number)


# Comprobar si es alpha numérico

numero = "buenas"
is_alpha = numero.isalpha()

print(is_alpha)

# Count buscamos una cadena en otra cadena y nos devuelve la cantidad de veces que esta en coincidencias

resultado =cadena.count("o")

print(resultado)

# function len para contar la cantidad de datos de una cadena

resultado=len(cadena)

print(resultado)

# endswith verificamos si una cadena termina con otra cadena dada si es asi devuelve true
resultado1 = cadena.endswith("s")
print(resultado1)

# startswith verificamos si una cadena empieza con otra cadena dada si es asi devuelve true
resultado1 = cadena.startswith("H")
print(resultado1)

# replace Se remplaza un pedazo de la cadena
cadena1 = "Hola"
cadena_nueva = cadena1.replace("Hola", "Hola como estas")

print(cadena_nueva)


# Split sirve para separar y devolver una lista
cadena_separada = cadena_nueva.split()

print(cadena_separada)
