from dataclasses import dataclass, field
from datetime import datetime as dt
from usuario import usuario

@dataclass(frozen=False)
class deuda:
    '''
    Clase que representa la deuda de un usuario a otro.
    '''
    id: int
    #Usuario que recibe la deuda
    usuarioDeber: usuario
    #Usuario que debe pagar la deuda
    usuarioDeudor: usuario    

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
        output += " -- Cantidad: " + str(self.importe) + " €\n"
        output += " -- Concepto: " + self.concepto + "\n"
        output += " -- Fecha: " + self.fecha.strftime("%m/%d/%Y") + "\n"

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
        

#Test de clase
if __name__ == "__main__":
    u1 = usuario(1,"danielsp","Daniel","Pérez Ruiz")
    u2 = usuario(2,"pablonl","Pablo","Nieto López")

    d1 = deuda(1,u1,u2,10.5,"test")

    print("Recibe deuda: " + d1.nickUsuarioDeber())
    print("Paga deuda: " + d1.nickUsuarioQuePaga())