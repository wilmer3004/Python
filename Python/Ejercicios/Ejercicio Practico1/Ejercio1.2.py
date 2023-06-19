"""
Teniendo como base

En un segundo se pueden decir 2 palabras
Cuantas palabras se puedes decir en x segundos
 
A) Pedir al usuario que diga cualquier texto real y:
-calcular cuanto tardaría en decir esta frase
-¿Cuantas palabras dijo?

B) si se tarda mas de 1 minuto:
-decirle: "para flaco tampoco te pedí un testamento

C) Dalto habla un 30% mas rápido
-¿Cuanto tardaría el en decirlo?
"""

# A)

# Pedimos datos 
frase = input("Ingresa una frase y te digo cuanto tardarías en decirlo si tuvieras que decirlo:  ")
# Realizamos operaciones
palabras_separadas = frase.split(" ")
cantidad_de_palabras = len(palabras_separadas)
tiempo_en_decir = cantidad_de_palabras/2

# Mostramos resultados

print(f"Digitaste {cantidad_de_palabras} palabras, tardarías en decir esta cantidad de palabras {tiempo_en_decir} segundos.")
print(f"Mientras que dalto tardaría en decir esto {tiempo_en_decir-cantidad_de_palabras * 100 // 2 * 0.3 /100} segundos.")

if cantidad_de_palabras>120:
    print("Para flaco tampoco te pedí un testamento")

