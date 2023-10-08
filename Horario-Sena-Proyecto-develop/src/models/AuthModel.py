class AuthModel:
    def __init__(self,idUsuario,idTipoDocFK,numeroIdent,contrasenaUsuario)->None:
        self.idUsuario = idUsuario
        self.idTipoDocFK = idTipoDocFK
        self.numeroIdent = numeroIdent
        self.contrasenaUsuario = contrasenaUsuario
    
    def to_json(self):
        return {
            "idUsuario":self.idUsuario,
            "idTipoDocFK":self.idTipoDocFK,
            "numeroIdent":self.numeroIdent,
            "contrasenaUsuario":self.contrasenaUsuario
        }
    
    
        
        
        
        