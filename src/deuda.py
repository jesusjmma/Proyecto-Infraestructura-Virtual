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

    def __str__(self):
        '''
        Representacion de la clase a formato legible
        '''
        output = ""
        output += "=============================================\n"
        output += "Deber a: " + self.usuarioDeber.nickname + "\n"
        output += "Paga la deuda: " + self.usuarioDeudor.nickname + "\n"
        output += "=============================================\n"
        output += " -- Importe: " + str(self.importe) + " €\n"
        output += " -- Concepto: " + self.concepto + "\n"

        return output

    # ===============================================================

    def nickUsuarioDeber(self):
        return self.usuarioDeber.nickname

    def nickUsuarioQuePaga(self):
        return self.usuarioDeudor.nickname
        
#Test de clase
if __name__ == "__main__":
    pass