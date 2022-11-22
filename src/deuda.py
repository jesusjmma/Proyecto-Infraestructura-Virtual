from dataclasses import dataclass, field
from datetime import datetime as dt
from usuario import usuario

@dataclass(frozen=False)
class deuda:
    '''
    Clase que representa la deuda de un usuario a otro.
    '''
    id: int
    #Usuario que debe pagar la deuda
    usuarioDeudor: usuario
    #Usuario que recibe la deuda
    usuarioDeber: usuario

    importe: float
    concepto: str

    #Fecha en la que se produce la deuda (generada tras inicializacion)
    fecha: dt = field(init=False, repr=True)

    def __post_init__(self):
        self.fecha = dt.today()

    

#Test de clase
if __name__ == "__main__":
    u1 = usuario(1,"danielsp","Daniel","Pérez Ruiz")
    u2 = usuario(2,"pablonl","Pablo","Nieto López")

    d1 = deuda(1,u1,u2,10.5,"test")

    print(d1)

    