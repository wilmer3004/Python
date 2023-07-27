from Vehiculo import *
class Automovil(Vehiculo):
    # Constructor
    def __init__(self, color, placa, cant_llantas,cant_asientos):
        super().__init__(color, placa, cant_llantas)
        self.__cant_asientos=cant_asientos
    
    def getCant_asientos(self):
        return self.__cant_asientos
    def setCant_asientos(self,cant_asientos):
        self.__cant_asientos = cant_asientos

    #  Caracteristicas
    def caracteristicas(self):
        print(f"llantas: {self.getCant_llantas()}")
        print(f"Color: {self.getColor()}")
        print(f"Placa: {self.getPlaca()}")
        print(f"Cantidad de asientos: {self.getCant_asientos()}")
    
    
    # Acelerar el automovil
    def acelerar(self):
        print("Se esta acelerando el automovil")

    # Frenar el automovil
    def frenar(self):
        print("Se esta frenando el automovil")    