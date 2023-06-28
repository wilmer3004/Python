import random
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
# # Funciones
# def create_list (word1,word2):
#     word3= word1.split()
#     word4= word2.split()

#     return word3,word4
            
# # word1 = input("Digite una palabra: ")
# # word2 = input("Digite una palabra: ")
# print(create_list("Hola", "aloH"))


# Black-Jack

def azar():
    dictionary={
        1:{"a":1,"A":11},
        2:2,
        3:3,
        4:4,
        5:5,
        6:6,
        7:7,
        8:8,
        9:9,
        10:["J","K","Q"],
    }
    azar = random.randrange(1,11,1)
    
    resp1 = 1
    get = dictionary.get(azar) 
    calc = get
    while resp1 ==1 and azar == 1:
        if azar == 1:
            res = int(input("Ingrese cuanto quiere que su A valga 11 o 1: "))
            if res == 1:
                resp1 =0
                calc = dictionary[1]["a"]
                get = "A:1"
            elif res ==11:
                resp1 =0
                get = "A:11"
                calc = dictionary[1]["A"]
            else:
                print("Ingreso un valor invalido, debe ingresar un valor valido ")
    
    if azar ==10:
        azar1 = random.randrange(1,3,1)
        get = dictionary[10][azar1]
        calc=10
    worth = [get,calc]
    return worth


def show_card():
    worth1=azar()
    data=worth1[0]
    data1=worth1[1]
    sum1 = 0
    sum1 = sum1+data1
    worth=[data,sum1]
    return worth
def win_lose (n1,n2):
    if n1 ==21:
        return   "La mesa acaba de ganar"
    elif n2 == 21:
        return    "El usuario acaba de ganar"
    elif n2>n1 and n2<21:
        return    "El usuario va ganando"
    elif n1>n2 and n1<21:
        return    "La mesa va ganando"
    elif n1>21:
        return    "La mesa perdió"
    elif n2>21:
        return    "El usuario perdió"










# ---------------------------------------------------------------
sum2 = 0

cont = 0
print("Cartas de la mesa: ")
for i in range(2):
    cont+=1
    show_table = show_card()
    print(f"Carta {cont}: {show_table[0]}")
    sum2 = sum2+show_table[1]
print(f"La suma actual de las cartas de la mesa es: {sum2}\n")
sum3 = 0

cont1 = 0
print("Cartas del usuario: ")
for i in range(2):
    cont1+=1
    show_usu = show_card()
    print(f"Carta {cont1}: {show_usu[0]}")
    sum3 = sum3+show_usu[1]
print(f"La suma actual de las cartas del usuario es: {sum3}\n")

print(win_lose(sum2,sum3))
win_or_lose  = win_lose(sum2,sum3)

continue_play ="pedir"
while sum2 <=21 and sum3<=21 and continue_play=="pedir":
    if win_or_lose =="El usuario va ganando":
            continue_play = input("La mesa desea pedir otra carta o se retira: ")
            if continue_play == "pedir":
                show_table = show_card()
                print(f"Carta {cont}: {show_table[0]}")
                sum2 = sum2+show_table[1]
                print(f"La suma actual de las cartas de la mesa es: {sum2}\n")
                win_or_lose  = win_lose(sum2,sum3)
                
            
    elif win_or_lose =="La mesa va ganando":
            continue_play = input("El usuario desea pedir otra carta o se retira: ")
            if continue_play == "pedir":
                show_usu = show_card()
                print(f"Carta {cont1}: {show_usu[0]}")
                sum3 = sum3+show_usu[1]
                print(f"La suma actual de las cartas del usuario es: {sum3}\n")
                win_or_lose  = win_lose(sum2,sum3)
    elif win_or_lose =="El usuario acaba de ganar" or win_or_lose =="La mesa acaba de ganar" :
        print(win_or_lose)
        continue_play=="fin"
    print(win_or_lose)
print("Fin del juego")


        
   