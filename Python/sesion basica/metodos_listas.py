# Métodos de listas
lista1 = [76,4,65,2,1,3,34,32]
# creando una lista con list

lista = list(["Hola", "Wilmer","Edad", 18])
print(lista)

# Len regresa la longitud de la lista

resultado = len(lista)
print(resultado)

# append Agregar  elementos a la lista

agregar_append = lista.append("Altura")

print(lista)

# insert  Agregar un elemento a una lista en un indice especifico

agregar_insert = lista.insert(6,1.70)

print(lista)

# extend  Agregar varios elementos a una lista 

agregar_extend = lista.extend([True, "Sexo", "Masculino"])

print(lista)

# pop Elimina un elemento de la lista con un indice

lista.pop(0)

print(lista)

# remove remueve un elemento de la lista con el nombre del elemento

lista.remove("Sexo")
lista.remove("Masculino")
print(lista)



# Sort ordena los elementos de la lista en forma ascendente

lista1.sort()

print(lista1)

# Sort (reverse=True) ordena los elementos de la lista en forma descendente

lista1.sort(reverse=True)

print(lista1)

# reverse invierte los elementos de una lista

lista.reverse()

print(lista)


# clear Elimina todos los elementos de la lista 

lista.clear()

print(lista)
