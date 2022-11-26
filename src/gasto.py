from dataclasses import dataclass
from infoUsuario import infoUsuario

@dataclass(frozen=True)
class gasto:
    '''
    Clase que representa el gasto realizado por un usuario.
    '''
    usuario: infoUsuario

    importe: float
    concepto: str