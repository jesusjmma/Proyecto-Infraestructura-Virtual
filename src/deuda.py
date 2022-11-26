from dataclasses import dataclass
from infoUsuario import infoUsuario

@dataclass(frozen=True)
class deuda:
    '''
    Clase que representa la deuda de un usuario a otro.
    '''
    usuarioDeber: infoUsuario
    usuarioDeudor: infoUsuario    

    importe: float
    concepto: str
        
#Test de clase
if __name__ == "__main__":
    pass