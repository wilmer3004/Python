cuadricula = [[],[],[]]
def inicio_juego():
    for x in range(len(cuadricula)):
        for y in range(3):
            cuadricula[x].append(0)
    print(cuadricula)
inicio_juego()
def insert(x,y,a):
    if cuadricula[x][y] == 0:
        cuadricula[x][y] = a
    else:
        print("El campo ya esta ingresado")    
def juego():
    x = int(input("Ingrese la posición en x del campo que usted quiere marcar: "))
    y = int(input("Ingrese la posición en x del campo que usted quiere marcar: "))
    a = int(input(f"""Ingrese su figura:
1. O
2. X
Elija: """))
    if x <3 and y <3 and x>=0 and y >=0:
        if a == 1:
            insert(x,y,"O")
        elif  a == 2:
            insert(x,y,"X")
        else:
            return print("Ingreso una eleccion no valida")
    else:
        return print("Ingreso un valor no valido")
    return print(cuadricula)

juego()