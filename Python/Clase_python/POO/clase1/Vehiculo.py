class Vehiculo:
    def __init__(self,color,placa,cant_llantas):
        self.__color=color
        self.__placa=placa
        self.__cant_llantas = cant_llantas
    def getColor(self):
        return self.__color
    def setColor(self,color):
        self.__color = color
    def getPlaca(self):
        return self.__placa
    def setPlaca(self,placa):
        self.__placa= placa
    def getCant_llantas(self):
        return self.__cant_llantas
    def setCant_llanatas(self,cant_llantas):
        self.__cant_llantas = cant_llantas