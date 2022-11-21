from dataclasses import dataclass
from datetime import datetime
import usuario

@dataclass
class deuda:
    '''
    Clase que representa la deuda de un usuario frente a otro.
    '''
    id: int
    #Usuario que debe pagar la deuda
    usuarioDeudor: usuario
    #Usuario que recibe la deuda
    usuarioDeber: usuario

    importe: float
    fecha: datetime
    concepto: str