pasajeros = [["Manuel Suárez",19823451,"Armenia","Colombia"],
             ["Gloria Galvis",45789234,"Cali","Colombia"],
             ["Rosa Ortiz",4546234,"Medellin","Colombia"],
             ["Eduardo Carrasquilla",79844677,"Cali","Colombia"]
]
ciudad = [["Armenia","Quindio"],
          ["Cali","Valle"],
          ["Medellin","Antioquia"]
          ]

def agregar_pasajeros():
    nombre = input("Ingrese el nombre del nuevo pasajero: ")
    identificacion = int(input(f"Ingrese el numero de identificación de {nombre}: "))
    destino = input(f"Ingrese el destino de viaje de {nombre}: ")
    pais = input(f"Ingrese el nombre del pais en que se encuentra {destino}: ")
    pasajeros.append((nombre, identificacion,destino,pais))
    return "Se ingresaron los valores"
    # pasajeros[len(pasajeros)-1][0]

def agregar_ciudades():
    ciudad1 = input("Ingrese el nombre de la ciudad: ")
    departamento = input(f"Ingrese el nombre del departamento de {ciudad1}: ")
    ciudad.append((ciudad1,departamento))
    return "Se ingresaron los valores"

def ciudad_destino():
    c_destino = int(input("Ingrese el numero de identificacion del pasajero que desea consultar: "))
    for i in range(len(pasajeros)):
        if c_destino == pasajeros[i][1]:
            return (f"La ciudad de destino del pasajero identificado con {c_destino} es: {pasajeros[i][2]}")
    return "El pasajero que usted ingreso es invalido" 

def pasajeros_ciudad():
    ciudad_p = input("Ingrese el nombre de la ciudad que desea consultar: ")
    cont = 0
    for i in range(len(pasajeros)):
        if ciudad_p == pasajeros[i][2]:
            cont+=1
    return cont

def pais_destino():
    c_destino = int(input("Ingrese el numero de identificacion del pasajero que desea consultar: "))
    for i in range(len(pasajeros)):
        if c_destino == pasajeros[i][1]:
            return (f"El pais de destino del usuario con numero de identificacion {c_destino} ingresado es: {pasajeros[i][3]}")
    return "El pasajero que usted ingreso es invalido"

def pasajeros_pais():
    pais_p = input("Ingrese el nombre del pais que desea consultar: ")
    cont1 = 0
    for i in range(len(pasajeros)):
        if pais_p == pasajeros[i][3]:
            cont1+=1
    return cont1 





# ------------------------------------------------------------------------------------
while True:
    print("1. Agregar pasajeros")
    print("2. Agregar ciudades")
    print("3. Buscar ciudad destino por la identificación")
    print("4. Cantidad de pasajeros que viajan a una cuidad")
    print("5. Buscar país destino mediante la identificación")
    print("6. Cantidad de pasajeros que viajan a un pais")
    print("7. Salir del programa")
    opcion = int(input("Acción a ejecutar: "))
    if opcion == 1:
        print("Agregar pasajeros")
        print(agregar_pasajeros())
    elif opcion == 2:
        print("Agregar ciudades")
        print(agregar_ciudades())
    elif opcion == 3:
        print("Buscar ciudad destino por la identificación")
        print(ciudad_destino())
    elif opcion == 4:
        print("Cantidad de pasajeros que viajan a una cuidad")
        print(f"La cantidad de pasajeros de su ciudad consultada es: {pasajeros_ciudad()}")  
    elif opcion == 5:
        print("Buscar país destino mediante la identificación")
        print(pais_destino())
    elif opcion == 6:
        print("Cantidad de pasajeros que viajan a un pais")
        print(f"La cantidad de pasajeros de su pais consultado es: {pasajeros_pais()}")

    elif opcion == 7:
        break
    else:
        print("Opción invalida")

print("Gracias por utilizar nuestro programa")
print(ciudad)
print(pasajeros)




