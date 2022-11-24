from dataclasses import dataclass, field
from datetime import datetime as dt
from infoUsuario import infoUsuario

@dataclass(frozen=True)
class deuda:
    '''
    Clase que representa la deuda de un usuario a otro.
    '''
    id: int
    #Usuario que recibe la deuda
    usuarioDeber: infoUsuario
    #Usuario que debe pagar la deuda
    usuarioDeudor: infoUsuario    

    importe: float
    concepto: str

    #Fecha en la que se produce la deuda (generada tras inicializacion)
    fecha: dt = field(init=False, repr=True)

    def __post_init__(self):
        '''
        Tras inicializar la clase, se inicializa la fecha (hoy)
        '''
        self.fecha = dt.today()

    def __str__(self):
        '''
        Representacion de la clase a formato legible
        '''
        output = ""
        output += "=============================================\n"
        output += "ID Deuda: " + str(self.id) + "\n"
        output += "=============================================\n"
        output += "Deber a: " + self.usuarioDeber.nickname + "\n"
        output += "Paga la deuda: " + self.usuarioDeudor.nickname + "\n"
        output += "=============================================\n"
        output += " -- Importe: " + str(self.importe) + " €\n"
        output += " -- Concepto: " + self.concepto + "\n"
        output += " -- Fecha: " + self.obtenerFechaDeuda() + "\n"

        return output

    # ===============================================================

    def nickUsuarioDeber(self):
        '''
        Metodo para obtener el nickname del usuario a quien debe
        esta deuda
        Return: nickname de usuario a deber
        '''
        return self.usuarioDeber.nickname

    def nickUsuarioQuePaga(self):
        '''
        Metodo para obtener el nickname del usuario que paga
        esta deuda
        Return: nickname del usuario que paga
        '''
        return self.usuarioDeudor.nickname
    
    def obtenerFechaDeuda(self):
        '''
        Metodo para obtener la fecha de la deuda en formato string
        Return: fecha en string
        '''
        return self.fecha.strftime("%m/%d/%Y")
        

#Test de clase
if __name__ == "__main__":
    pass