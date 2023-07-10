cuadricula = [[],[],[]]
# Mostrar la tabla
def mostrar_cuadricula():
    for x in range(len(cuadricula)):
        print(cuadricula[x])

# llenar la tabla con 0
def inicio_juego():
    for x in range(len(cuadricula)):
        for y in range(3):
            cuadricula[x].append(0)
    mostrar_cuadricula()
# Insertar el símbolo
def insert(x,y,a):
    if cuadricula[x][y] == 0:
        cuadricula[x][y] = a
    else:
        print("El campo ya esta ingresado")    
# Preguntar casilla y símbolo
def juego():
    x = int(input("Ingrese la posición en x del campo que usted quiere marcar: "))
    y = int(input("Ingrese la posición en x del campo que usted quiere marcar: "))
    a = int(input(f"""Ingrese su figura:
1. O
2. X
Elija: """))
    if x <3 and y <3 and x>=0 and y >=0 and cuadricula[x][y]==0:
        if a == 1:
            insert(x,y,"O")
        elif  a == 2:
            insert(x,y,"X")
        else:
            return print("Ingreso una eleccion no valida"),mostrar_cuadricula()
    else:
        return print("Ingreso un valor no valido o el campo ya esta ocupado"),mostrar_cuadricula()
    return mostrar_cuadricula()

# -----------------------------------------------------------------------------------------------------
resp = 1
inicio_juego()
while resp == 1:
    cont = 0
    juego()
    for x in range(3):
        if 0 in cuadricula:
            resp = 1
        else:
            cont +=1
    if cont ==0:
        resp = 2

