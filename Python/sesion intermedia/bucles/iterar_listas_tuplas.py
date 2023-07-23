
# Iterando una lista
lista = ["perro", "gato", "loro", "cocodrilo"]
numeros = [10,12,70,32]
# iteramos la lista
for animal in lista:
    print(animal)
    
#iteramos numeros
for numero in numeros:
    print(numero*10)

# iterar dos listas con la función zip()

for  animal,numero in zip(lista,numeros):
    print(f"Recorriendo la lista #1: {animal}")
    print(f"Recorriendo la lista #2: {numero}")
    
# iterar con la función range no optima

for num in range(len(numeros)):
    print(numeros[num])
    
    
# Forma correcta de recorrer una lista con su indice

for num in enumerate(numeros):
    print(f"indice = {num[0]}", end=" ")
    print(f"valor = {num[1]} \n")
    
# Todo lo anterior sirve lo mismo para tupla
    