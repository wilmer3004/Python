class TrimestreModel:
    
    def __init__(self,idTrimestre,nombreTrimestre,fechaInicio,fechaFin,estadoTrimestre):
        self.idTrimestre = idTrimestre
        self.nombreTrimestre = nombreTrimestre
        self.fechaInicio = fechaInicio
        self.fechaFin = fechaFin
        self.estadoTrimestre = estadoTrimestre
    
    def to_json(self):
        return {
             "idTrimestre":self.idTrimestre,
             "nombreTrimestre":self.nombreTrimestre,
             "fechaInicio":self.fechaInicio,
             "fechaFin":self.fechaFin,
             "estadoTrimestre":self.estadoTrimestre 
             
        }
        
    


