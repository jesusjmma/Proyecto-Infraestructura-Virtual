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

    def __str__(self):
        output = ""
        output += "=============================================\n"
        output += "Pagado por: " + self.nickUsuarioGasto() + "\n"
        output += "=============================================\n"
        output += " -- Importe: " + str(self.importe) + " €\n"
        output += " -- Concepto: " + self.concepto + "\n"

        return output
    
    # ===============================================================
    
    def nickUsuarioGasto(self):
        return self.usuario.nickname

#Test de clase
if __name__ == "__main__":
    pass