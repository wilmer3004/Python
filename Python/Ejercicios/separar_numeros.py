respuesta = 1
# Ciclo para que el programa se ejecute mas de una vez
while respuesta ==1:
    # Esta lista servirá para agregar el numero que queremos descomponer
    number = []
    # En esta lista almacenaremos el numero para multiplicar lo que deseamos
    number_in_zero = []
    # Capturamos el numero que desea el usuario
    number1 = input("Ingrese el numero que desea: \n")
# Comprobamos que sea un dato unicamente numérico
    if number1.isnumeric():
        # Le asignamos a la lista el dato capturado
        number = number1
        # Creamos un bucle para asignar el orden y la cantidad de ceros por lo cuales vamos a multiplicar el numero ingresado por el usuario 
        for i in range(len(number)):
            # Se crea una condicional para que solo cuando se encuentre la iteración en 0 se le asigne un uno a la lista en la posición 0
            if i == 0:
                number_in_zero.append("1")
            # De lo contrario se empezaran a agregar 0
            else:
                number_in_zero.append("0")
        # Fuera del bucle vamos a crear un contador que se encargue de la posición final que tiene nuestra lista
        cont= len(number_in_zero)-1
        # Creamos un bucle para empezar a descomponer
        for j in range(len(number)):
            # a num se le va a asignar lo que tenga la lista en la posición de la iteración para asi poderla parsear
            num = int (number[j])
            # Unificamos lo que se encuentre en la lista de ceros para poderla multiplicar con num 
            ope = "".join(number_in_zero)
            # parseamos lo que acabamos de unificar para poderlo multiplicar 
            num2=int(ope)
            # Multiplicamos los números para poder sacar el numero descompuesto
            result = num*num2
            print(result)
            # Eliminamos la ultima posición de la lista para que se multiplique con un cero menos y se pueda organizar en forma descendiente
            # es decir de centenas a descends y finalmente a unidades aunque se puede hacer con valores mas grandes
            number_in_zero.pop(cont)
            # Le vamos restando al contador uno para que se vaya eliminando una posición menos 
            cont -=1
    # Si no es un numero el dato ingresado por el usuario se muestra el mensaje a continuación
    else: 
        print("En el numero que usted ingreso hay un dato invalido, es decir no es un numero")
    # Se le captura la respuesta al usuario y en caso de ser asertiva se vuelve a ejecutar el código
    respuesta=int(input("Desea descomponer otro numero: \n1. si\n2.no\nElija: "))
print("Gracias por usar nuestro programa")