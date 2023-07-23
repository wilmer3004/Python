
# Iterando una conjuntos
conjuntos = {"perro", "gato", "loro", "cocodrilo"}
numeros = {10,12,70,32}
# iteramos la conjuntos
for animal in conjuntos:
    print(animal)
    
#iteramos numeros
for numero in numeros:
    print(numero*10)

# iterar dos conjuntos con la función zip()

for  animal,numero in zip(conjuntos,numeros):
    print(f"Recorriendo la conjuntos #1: {animal}")
    print(f"Recorriendo la conjuntos #2: {numero}")
    
    
# Forma correcta de recorrer una conjuntos con su indice

for num in enumerate(numeros):
    print(f"indice = {num[0]}", end=" ")
    print(f"valor = {num[1]} \n")
    
# Todo lo anterior sirve lo mismo para tupla y listas
    