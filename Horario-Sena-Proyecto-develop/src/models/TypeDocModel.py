class TypeDocModel:
    
    def __init__(self,idTipoIdent,nombreTipoIdent,estadoTipoIdent)->None:
        self.idTipoIdent=idTipoIdent
        self.nombreTipoIdent=nombreTipoIdent
        self.estadoTipoIdent=estadoTipoIdent
    
    def to_json(self):
        return{
            'idTipoIdent':self.idTipoIdent,
            'nombreTipoIdent':self.nombreTipoIdent,
            'estadoTipoIdent':self.estadoTipoIdent
        }
        