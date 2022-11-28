from dataclasses import dataclass

@dataclass(frozen=True)
class gasto:
    '''
    Objeto valor que representa un gasto iniciado por un usuario, y en
    el que participan un conjunto de usuarios, especificando el concepto
    y el importe del mismo
    '''

    nickPagador: str
    concepto: str
    importe: float
    nicksParticipantes: list
