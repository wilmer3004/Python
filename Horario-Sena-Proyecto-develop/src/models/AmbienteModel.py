class AmbienteModel:
    def __init__(self,idAmbiente,numeroAmbiente,horasDisponibles,estadoAmbiente,idSedeFK) -> None:
        self.idAmbiente=idAmbiente
        self.numeroAmbiente = numeroAmbiente
        self.horasDisponibles = horasDisponibles
        self.estadoAmbiente = estadoAmbiente
        self.idSedeFK = idSedeFK

    def to_json(self):
        return{
            "idAmbiente":self.idAmbiente,
            "numeroAmbiente":self.numeroAmbiente,
            "horasDisponibles":self.horasDisponibles,
            "estadoAmbiente":self.estadoAmbiente,
            "idSedeFK":self.idSedeFK
        }