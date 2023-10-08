class JornadaModel :
    
    def __init__(self,idJornada,nombreJornada,diaIniJor,diaFinJor,estadoJornada) -> None:
        self.idJornada=idJornada
        self.nombreJornada=nombreJornada
        self.diaIniJor=diaIniJor
        self.diaFinJor=diaFinJor
        self.estadoJornada=estadoJornada

    def to_json(self):
        return {
            'idJornada':self.idJornada,
            'nombreJornada':self.nombreJornada,
            'diaIniJor':self.diaIniJor,
            'diaFinJor':self.diaFinJor,
            'estadoJornada':self.estadoJornada
        }
