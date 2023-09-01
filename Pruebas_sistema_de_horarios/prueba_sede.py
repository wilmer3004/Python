from flask import jsonify

# Variable global para almacenar los datos de los instructores
datos_personales_instructor = []

# Validación de que en un horario un profesor no pueda estar en dos sedes distintas 
def validation_sede():
    global datos_personales_instructor  # Indica que vamos a utilizar la variable global
    
    instructores_sin_repeticiones = eliminar_instructores_sedes_distintas()
    
    # Actualiza la lista de instructores con la lista filtrada
    datos_personales_instructor = instructores_sin_repeticiones

def eliminar_instructores_sedes_distintas():
    instructores_por_sede = {}  # Diccionario para rastrear los instructores por sede
    instructores_sin_repeticiones = []  # Lista para almacenar instructores sin repeticiones
    
    for instructor in datos_personales_instructor:
        nombre = instructor["name"]
        sede = instructor["sede"]
        
        if nombre not in instructores_por_sede:
            instructores_por_sede[nombre] = sede
        else:
            # Si el instructor ya está en el diccionario, verifica si está en la misma sede
            if instructores_por_sede[nombre] == sede:
                # Muestra una alerta si el instructor ya está en la misma sede
                print(f"Alerta: El instructor {nombre} ya está registrado en la misma sede.")
            else:
                # Si el instructor está en una sede distinta, no lo agregamos a la nueva lista
                continue
        
        instructores_sin_repeticiones.append(instructor)
    
    return instructores_sin_repeticiones

# Solicitud de datos para la validación
def prueba_sede():
    nombre = input("Ingresa el nombre de un profesor: ")
    sede1 = input(f"Ingresa la sede en la cual va a estar el instructor {nombre}: ")
    
    # Verifica si el instructor ya está en la lista y si está en la misma sede
    for instructor in datos_personales_instructor:
        if instructor["name"] == nombre and instructor["sede"] == sede1:
            # Muestra una alerta si el instructor ya está registrado en la misma sede
            print(f"Alerta: El instructor {nombre} ya está registrado en la misma sede.")
            return
    
    # Si el instructor no existe en la lista o está en una sede diferente, agrégalo
    solicitud_datos_instructor = dict(name=nombre, sede=sede1)
    datos_personales_instructor.append(solicitud_datos_instructor)

dato = True
while dato:
    prueba_sede()
    respuesta = input("Desea ingresar otro dato: ")
    dato = respuesta.lower() == "si"

print(datos_personales_instructor)
validation_sede()
print(datos_personales_instructor)
