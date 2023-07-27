class Motocicleta:
    __nuevo = "New"
    __motor=False
    __precio=0
    def __init__(self, color, matricula, combustible_litros, numero_ruedas,marca, modelo,fecha_fabricacion,velocidad_punta, peso) :
        self.__color=color
        self.___matricula = matricula
        self.__combustible_litros=combustible_litros
        self.__numero_ruedas=numero_ruedas
        self.__marca=marca
        self.__modelo=modelo
        self.__fecha_fabricacion=fecha_fabricacion
        self.__velocidad_punta=velocidad_punta
        self.__peso=peso


    def getColor(self):
        return self.__color
    def setColor(self,color):
        self.__color=color
    
    def getMatricula(self):
        return self.___matricula
    def setColor(self,matricula):
        self.___matricula=matricula
    
    def getCombustibe_litros(self):
        return self.__combustible_litros
    def setColor(self,combustible_litros):
        self.__combustible_litros=combustible_litros

    def getNumero_ruedas(self):
        return self.__numero_ruedas
    def setNumero_ruedas(self,numero_ruedas):
        self.__numero_ruedas=numero_ruedas

    def getMarca(self):
        return self.__marca
    def setMarca(self,marca):
        self.__marca=marca

    def getModelo(self):
        return self.__modelo
    def setModelo(self,modelo):
        self.__modelo=modelo

    def getFecha_fabricacion(self):
        return self.__fecha_fabricacion
    def setFecha_fabricacion(self,fecha_fabricacion):
        self.__fecha_fabricacion=fecha_fabricacion

    def getVelocidad_punta(self):
        return self.__velocidad_punta
    def setModelo(self,velocidad_punta):
        self.__velocidad_punta=velocidad_punta

    def getPeso(self):
        return self.__peso
    def setPeso(self,peso):
        self.__peso=peso

    def getNuevo(self):
        return self.__nuevo
    def setNuevo(self,nuevo):
        self.__nuevo=nuevo
    
    def getMotor(self):
        return self.__motor
    def setMotor(self,motor):
        self.__motor=motor


    # Arrancar

    def arrancar(self):
        if self.getCombustibe_litros()>0:
            if self.getMotor() == False:
                self.setMotor(True)
                return print("Ha arrancado")
            elif self.getMotor() == True:
                return print("El motor ya estaba en marcha")
            else:
                return("Error")
        else:
            self.setMotor(False)
            return print("La Motocicleta no posee gasolina")
        
    def detener(self):
        if self.getCombustibe_litros()==0:
            self.setMotor(False)
        elif self.getMotor() == True:
            self.setMotor(False)
            return print("El motor Se ha detenido")
        elif self.getMotor() == False:
            return print("El motor ya estaba detenido")
        else:
            return("Error")
    def descripcion(self):
        print(f'El color de la moto es {self.getColor()}')
        print(f'La matricula de la moto es {self.getMatricula()}')
        print(f'El combustible que actualmente posee la moto es de {self.getCombustibe_litros()}')
        print(f'El cantidad de ruedas de la moto es {self.getColor()}')
        print(f'La marca de la moto es {self.getMarca()}')
        print(f'El modelo de la moto es {self.getModelo()}')
        print(f'La fecha de fabricacion de la moto es {self.getFecha_fabricacion()}')
        print(f'La velocidad de punta de la moto es {self.getVelocidad_punta()}')
        print(f'El peso de la moto es  {self.getPeso()}')

    def precio(self,precio):
        self.__precio=precio
        
    def getPrecio(self):
        return print(f"El precio de su moto es {self.__precio:,}")


