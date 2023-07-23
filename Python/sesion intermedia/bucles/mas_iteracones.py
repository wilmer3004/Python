
frutas = ["banana","manzana","ciruela","pera","naranja","granada","durazno"]
cadena = "Hola Wilmer"
numeros = [2,5,8,10]
# Recorrer una lista con especificaciones de continue para saltar con la sentencia continue
for fruta in frutas:
    if fruta == "granada":
        continue
    print(f"Me voy a comer una {fruta}")

# Evitar para que el bucle siga ejecutándose
for fruta in frutas:
   
    print(f"Me voy a comer una {fruta}")
    if fruta == "pera":
        break
    
print("El bucle acaba de finalizar")


# recorrer una cadena de texto
for letra in cadena:
    print(letra)

# bucles en una sola linea de código
numeros_duplicados =[ x*2 for x in numeros]

print(numeros_duplicados)