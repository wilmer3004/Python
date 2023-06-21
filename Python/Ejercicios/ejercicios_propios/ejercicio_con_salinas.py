# Ejercicio 1
# # Verificar cuantas vocales hay en un texto
# vocales = ["a","e","i","o","u"]
# cont =0
# text = input("Ingrese un texto que desee: ")
# for i in text:
#     if i in vocales:
#         cont +=1
# print(cont)

# Ejercicio 2
word1 = []
word3=[]
word= input("Ingrese una palabra: ")
word2= input("Ingrese otra palabra: ")

for i in range (len(word)):
     word1.append(word[i])
     word3.append(word2[i])
cont = 0
if len(word1)==len(word3):
    print("La palabra puede ser un anagrama")
    for x in range(len(word3)):
        for y in range(len(word3)):
            if word1[x]==word3[y]:
                cont+=1
                word1.pop(x)
if cont == len(word3):
    print("La palabra es un anagrama")
else:
    print("La palabra no es un anagrama")
    
            

