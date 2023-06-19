"""

time
mínimo 2.5 horas
promedio 4 horas
máximo 7 horas
soy Dalto 1.5 horas
1. Diferencia en porcentajes entre en curso actual y:
a)
- el mas rápido de otros cursos
-el mas lento de otros cursos 
-el promedio de los cursos

b) Porcentaje de material inservible que se reduce en:
crudo = 5 horas
-el promedio de los cursos
crudo 3.5 horas
-el curso actual

c) ver 10 horas de este curso a cuantas de otros cursos equivale?y al revés

"""
# A)


otros_cursos_min =2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5

# Diferencias de duración

diferencia_con_min = 100 - dalto_curso/otros_cursos_min*100
diferencia_con_max = 100 - dalto_curso*1000//otros_cursos_max/10
diferencia_con_promedio = 100 - dalto_curso/otros_cursos_promedio*100

# Mostramos los datos
print("----------------------------------------------------")

print(f"El curso de Dalto dura un {diferencia_con_min}% menos que el mas rápido.")
print(f"El curso de Dalto dura un {diferencia_con_max}% menos que el mas lento.")
print(f"El curso de Dalto dura un {diferencia_con_promedio}% menos que el mas promedio.")
print("----------------------------------------------------\n")
# B)

# Crudos del video
crudo_promedio = 5
crudo_dalto = 3.5

# Material inservible

material_inservible_promedio = 100 - otros_cursos_promedio/crudo_promedio * 100 
material_inservible_dalto = 100 - dalto_curso * 1000 //crudo_dalto /10

# Mostramos datos
print("----------------------------------------------------")

print(f"El material inservible que se tiene en los cursos promedios es de: {material_inservible_promedio}%")
print(f"El material inservible que se tiene en los cursos de dalto es de: {material_inservible_dalto}%")
print("----------------------------------------------------\n")

# C)
horas_diferencia_dalto = otros_cursos_promedio * 100 // dalto_curso/10
horas_diferencia_otros_cursos = dalto_curso * 100 // otros_cursos_promedio/10

# Mostrando diferencias si los cursos duraran 10 horas
print("----------------------------------------------------")

print(f"Ver 10 horas de es este curso de Dalto equivale a ver {horas_diferencia_dalto} horas de otros cursos")
print(f"Ver 10 horas de otros cursos equivale a ver {horas_diferencia_otros_cursos} horas de cursos de dalto")

print("----------------------------------------------------\n")


