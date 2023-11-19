import json

class DisponibilidadValidationService:
    @classmethod
    def get_bloque(cls):
        return [
            {
                "estadoBloque": 1,
                "idAmbienteFK": 1,
                "idBloque": 34,
                "idFichaFK": 1,
                "idInstructorFK": 1,
                "idJornadaFK": 1,
                "idPosicion": "[1, 2, 3]",
                "idSedeFK": 1,
                "idTematicaFK": 2,
                "idTrimestreFK": 1
            },
            {
                "estadoBloque": 1,
                "idAmbienteFK": 1,
                "idBloque": 35,
                "idFichaFK": 2,
                "idInstructorFK": 1,
                "idJornadaFK": 1,
                "idPosicion": "[4, 5, 6]",
                "idSedeFK": 1,
                "idTematicaFK": 2,
                "idTrimestreFK": 1
            },
            {
                "estadoBloque": 1,
                "idAmbienteFK": 1,
                "idBloque": 36,
                "idFichaFK": 3,
                "idInstructorFK": 1,
                "idJornadaFK": 1,
                "idPosicion": "[7, 8, 9]",
                "idSedeFK": 1,
                "idTematicaFK": 2,
                "idTrimestreFK": 1
            }
        ]

    @classmethod
    def validar_horarios_semana(cls, horarios, dia):
        return any(posicion in dia for posicion in horarios)

    @classmethod
    def validar_horarios_semana2(cls, horarios, dia):
        coincidencias = [posicion for posicion in horarios if posicion in dia]
        return len(coincidencias) > 0, coincidencias

def validar_instructor_en_distintas_sedes(instructor_id, sede_id, dia, datosBloque, bloques):
    for bloque in bloques:
        if bloque['idInstructorFK'] == instructor_id and bloque['idSedeFK'] != sede_id and \
                bloque['idBloque'] != datosBloque['idBloque'] and dia in json.loads(bloque['idPosicion']):
            return True
    return False

def validar_fichas_en_mismo_ambiente(datosBloque, bloques):
    for bloque in bloques:
        if bloque['idAmbienteFK'] == datosBloque['idAmbienteFK'] and \
                json.loads(bloque['idPosicion']) == json.loads(datosBloque['idPosicion']) and \
                bloque['idFichaFK'] != datosBloque['idFichaFK']:
            return True
    return False

def validar_posiciones_ya_asignadas(posiciones_a_validar, datosBloque, bloques):
    for bloque in bloques:
        if bloque['idBloque'] != datosBloque['idBloque'] and \
                posiciones_a_validar and any(posicion in json.loads(bloque['idPosicion']) for posicion in posiciones_a_validar):
            return {'message': 'SUCCESS', 'Lunes': True,
                    "posiciones-ya-asignadas": True,
                    "posiciones-asignadas": posiciones_a_validar}
    return {'message': 'SUCCESS', 'Lunes': False}

def validacion_posicion_sede(posicionesUsuario, datos):
    semana = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

    bloques = DisponibilidadValidationService.get_bloque()
    datosBloque = datos[0]
    posiciones_a_validar = json.loads(datosBloque['idPosicion']) if datosBloque['idPosicion'] else []

    # Validación de posiciones ya asignadas
    resultado_posiciones_ya_asignadas = validar_posiciones_ya_asignadas(posiciones_a_validar, datosBloque, bloques)
    if resultado_posiciones_ya_asignadas['Lunes']:
        return resultado_posiciones_ya_asignadas

    for bloque in bloques:
        posiciones = bloque['idPosicion']
        if posiciones == posicionesUsuario and bloque['idFichaFK'] == datosBloque['idFichaFK'] and \
                bloque['idAmbienteFK'] == datosBloque['idAmbienteFK'] and bloque['idTrimestreFK'] == datosBloque['idTrimestreFK'] and \
                bloque['idInstructorFK'] == datosBloque['idInstructorFK'] and \
                bloque['idSedeFK'] == datosBloque['idSedeFK'] and bloque['idTematicaFK'] == datosBloque['idTematicaFK'] and \
                bloque['idBloque'] != datosBloque['idBloque']:
            return "Posiciones-ya-asignadas"

        if posiciones_a_validar and any(posicion in json.loads(posiciones) for posicion in posiciones_a_validar):
            return {'message': 'SUCCESS', 'Lunes': True,
                    "posiciones-ya-asignadas": True,
                    "posiciones-asignadas": json.loads(posiciones)}

        if bloque['idAmbienteFK'] == datosBloque['idAmbienteFK'] and bloque['idSedeFK'] == datosBloque['idSedeFK']:
            # Validación para evitar que en un mismo ambiente estén al mismo tiempo dos fichas distintas
            if bloque['idFichaFK'] != datosBloque['idFichaFK']:
                return "Mismo-ambiente-con-dos-fichas-distintas"

        if bloque['idAmbienteFK'] == datosBloque['idAmbienteFK']:
            return "Ambiente-ya-ocupado"

        if bloque['idInstructorFK'] == datosBloque['idInstructorFK'] and \
                bloque['idFichaFK'] == datosBloque['idFichaFK'] and \
                bloque['idTrimestreFK'] == datosBloque['idTrimestreFK'] and \
                bloque['idTematicaFK'] == datosBloque['idTematicaFK'] and \
                bloque['idPosicion'] == datosBloque['idPosicion']:
            return "Instructor-ya-asignado-en-la-misma-tematica"

        if validar_instructor_en_distintas_sedes(datosBloque['idInstructorFK'], datosBloque['idSedeFK'],
                                                 json.loads(datosBloque['idPosicion']), datosBloque, bloques):
            return "Instructor-ya-asignado-en-otra-sede"

        if validar_fichas_en_mismo_ambiente(datosBloque, bloques):
            return "Mismo-ambiente-con-dos-fichas-distintas"

    for bloque_posicion in bloques:
        posicionesValidar = json.loads(bloque_posicion['idPosicion']) if bloque_posicion['idPosicion'] else []

        if bloque_posicion['idFichaFK'] == datosBloque['idFichaFK'] and \
                bloque_posicion['idAmbienteFK'] == datosBloque['idAmbienteFK'] and \
                bloque_posicion['idTrimestreFK'] == datosBloque['idTrimestreFK'] and \
                bloque_posicion['idInstructorFK'] == datosBloque['idInstructorFK'] and \
                bloque_posicion['idSedeFK'] == datosBloque['idSedeFK'] and \
                bloque_posicion['idTematicaFK'] == datosBloque['idTematicaFK'] and \
                bloque_posicion['idBloque'] != datosBloque['idBloque']:
            validacion_posicion_bloque_usuario = DisponibilidadValidationService.validar_horarios_semana2(
                posiciones_a_validar, posicionesValidar)
            if validacion_posicion_bloque_usuario[0]:
                return {'message': 'SUCCESS', 'Lunes': True,
                        "posiciones-ya-asignadas": True,
                        "posiciones-asignadas": validacion_posicion_bloque_usuario[1]}

        if posicionesValidar and any(posicion in json.loads(posiciones) for posicion in posicionesValidar):
            return {'message': 'SUCCESS', 'Lunes': True,
                    "posiciones-ya-asignadas": True,
                    "posiciones-asignadas": posicionesValidar}

    return {'message': 'SUCCESS', 'Lunes': False}

def ejecutar_todas_las_validaciones():
    # Datos de prueba
    data = [{
        "estadoBloque": 1,
        "idAmbienteFK": 1,
        "idBloque": 35,
        "idFichaFK": 2,
        "idInstructorFK": 1,
        "idJornadaFK": 1,
        "idPosicion": "[1, 2, 4, 5]",
        "idSedeFK": 1,
        "idTematicaFK": 2,
        "idTrimestreFK": 1
    }]

    # Ejemplo 1: Validación de posiciones ya asignadas
    resultado_ejemplo_1 = validacion_posicion_sede("[12,13]", data)

    # Ejemplo 2: Validación de mismo ambiente y sede con fichas distintas y posiciones iguales
    resultado_ejemplo_2 = validacion_posicion_sede("[4,5,6]", data)

    # Ejemplo 3: Validación de mismo ambiente con dos fichas distintas
    resultado_ejemplo_3 = validacion_posicion_sede("[7,8,9]", data)

    # Ejemplo 4: Validación de instructor ya asignado en la misma temática
    resultado_ejemplo_4 = validacion_posicion_sede("[1,2,3]", data)

    # Ejemplo 5: Validación de instructor ya asignado en otra sede
    resultado_ejemplo_5 = validacion_posicion_sede("[1,2,3]", data)

    return {
        "Resultado Ejemplo 1": resultado_ejemplo_1,
        "Resultado Ejemplo 2": resultado_ejemplo_2,
        "Resultado Ejemplo 3": resultado_ejemplo_3,
        "Resultado Ejemplo 4": resultado_ejemplo_4,
        "Resultado Ejemplo 5": resultado_ejemplo_5
    }

# Ejecutar todas las validaciones
resultados_validaciones = ejecutar_todas_las_validaciones()

# Mostrar los resultados
for key, value in resultados_validaciones.items():
    print(f"{key}: {value}")
