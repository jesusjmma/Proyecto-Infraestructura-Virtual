from dataclasses import dataclass

@dataclass(frozen=True)
class gasto:
    '''
    Objeto que representa el gasto realizado por un usuario. Contiene
    un identificador del usuario que paga, un importe, un concepto, y
    una lista de usuarios involucrados en este gasto
    '''
    usuarioPagador: str
    concepto: str
    importe: float
    participantes: list