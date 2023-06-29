dictionary = {
    "matematicas":10,
    "español": 8,
    "ingles":5,
    "musica":7,
    "sociales":9
}
diccionario={}
for elements in dictionary.items():
    clave= str(elements[0])
    clave_mayuscula= clave.upper()
    nota1= elements[1]
    if nota1<5 and nota1>0:
        vall = "Mal"
    elif nota1<7 and nota1>5:
        vall = "Regular"
    elif nota1<9 and nota1>7:
        vall = "Bueno"
    elif nota1<10 and nota1>10:
        vall = "Muy bueno"
    else:
            vall = "Excelente"
    diccionario[clave_mayuscula]=vall
print(dictionary)
print(diccionario)