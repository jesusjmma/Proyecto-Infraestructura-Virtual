from dataclasses import dataclass, field
from datetime import datetime as dt
from infoUsuario import infoUsuario

@dataclass(frozen=True)
class gasto:
    '''
    Clase que representa el gasto realizado por un usuario.
    '''
    id: int
    #Usuario que paga el gasto
    usuario: infoUsuario

    importe: float
    concepto: str

    #Fecha en la que se produce la deuda (generada tras inicializacion)
    fecha: dt = field(init=False, repr=True)

    def __str__(self):
        '''
        Representacion de la clase a formato legible
        '''
        output = ""
        output += "=============================================\n"
        output += "ID Gasto: " + str(self.id) + "\n"
        output += "=============================================\n"
        output += "Pagado por: " + self.usuario.nickname + "\n"
        output += "=============================================\n"
        output += " -- Importe: " + str(self.importe) + " €\n"
        output += " -- Concepto: " + self.concepto + "\n"

        return output

#Test de clase
if __name__ == "__main__":
    pass