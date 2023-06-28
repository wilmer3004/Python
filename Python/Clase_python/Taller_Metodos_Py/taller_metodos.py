pasajeros = [["Manuel Suárez",19823451,"Armenia"],
             ["Gloria Galvis",45789234,"Cali"],
             ["Rosa Ortiz",4546234,"Medellin"],
             ["Eduardo Carrasquilla",79844677,"Cali"]
]
ciudad = [["Armenia","Quindio"],
          ["Cali","Valle"],
          ["Medellin","Antioquia"]
          ]

def agregar_pasajeros():
    nombre = input("Ingrese el nombre del nuevo pasajero: ")
    identificacion = int(input(f"Ingrese el numero de identificación de {nombre}: "))
    destino = input(f"Ingrese el destino de viaje de {nombre}: ")
    pasajeros.append((nombre, identificacion,destino))
    # pasajeros[len(pasajeros)-1][0]
def agregar_ciudades():
    ciudad = input("Ingrese el nombre de la ciudad: ")
    departamento = input(f"Ingrese el nombre del departamento de {ciudad}: ")
def ciudad_destino():
    c_destino = int(input("Ingrese el numero de identificacion del pasajero que desea consultar: "))
    for i in range(len(pasajeros)):
        if c_destino == pasajeros[i][1]:
            return (f"La ciudad de destino del pasajero identificado con {c_destino} es: {pasajeros[i][2]}")
    return "El pasajero que usted ingreso es invalido" 
    
print(ciudad_destino())
print(pasajeros)


