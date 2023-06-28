import random
posibilidades = [[1,"piedra"],[2,"papel"],[3,"tijera"]]
def generar_random():
    n_random = random.randrange(1,3)
    return n_random
def comp_piedra(eleccion):
    random1 = generar_random()
    if eleccion == 1:
        if random1 ==1:
            return f"La maquina ha elegido {posibilidades[random1][1]}, por lo tanto empato"
        elif random1 ==2:
            return f"La maquina ha elegido {posibilidades[random1][1]}, por lo tanto perdio"
        elif random1 ==3:
            return f"La maquina ha elegido {posibilidades[random1][1]}, por lo tanto gano"
    if eleccion == 2:
        if random1 ==1:
            return f"La maquina ha elegido {posibilidades[random1][1]}, por lo tanto gano"
        elif random1 ==2:
            return f"La maquina ha elegido {posibilidades[random1][1]}, por lo tanto empato"
        elif random1 ==3:
            return f"La maquina ha elegido {posibilidades[random1][1]}, por lo tanto perdio"
    if eleccion == 3:
        if random1 ==1:
            return f"La maquina ha elegido {posibilidades[random1][1]}, por lo tanto perdio"
        elif random1 ==2:
            return f"La maquina ha elegido {posibilidades[random1][1]}, por lo tanto gano"
        elif random1 ==3:
            return f"La maquina ha elegido {posibilidades[random1][1]}, por lo tanto empato"
    else: return "Ingreso un valor no valido"

# ------------------------------------------------------------------------

resp =1
while resp ==1: 
    print("Elija: ")
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")

    eleccion1 = int(input("Ingrese su eleccion: "))
    print(comp_piedra(eleccion1))
    print("Desea volver a jugar: ")
    print("1. Si")
    print("2. No")
    resp = int(input("Ingrese su eleccion: "))
print("Gracias por usar nuestro programa")



