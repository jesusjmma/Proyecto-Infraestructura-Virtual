from dataclasses import dataclass

@dataclass(frozen=True)
class gasto:
    nickPagador: str
    concepto: str
    importe: float
    nicksParticipantes: list
