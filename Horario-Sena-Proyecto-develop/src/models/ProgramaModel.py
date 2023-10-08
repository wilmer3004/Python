class ProgramaModel:
    def __init__(self,idPrograma,nombrePrograma,descripcionProgram,versionPrograma,estadoPrograma) -> None:
        self.idPrograma=idPrograma
        self.nombrePrograma=nombrePrograma
        self.descripcionProgram=descripcionProgram
        self.versionPrograma=versionPrograma
        self.estadoPrograma=estadoPrograma

    def to_json(self):
        return {
            "idPrograma":self.idPrograma,
            "nombrePrograma":self.nombrePrograma,
            "descripcionProgram":self.descripcionProgram,
            "versionPrograma":self.versionPrograma,
            "estadoPrograma":self.estadoPrograma 
        }