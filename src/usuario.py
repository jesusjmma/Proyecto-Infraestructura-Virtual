from infoUsuario import infoUsuario
from deuda import deuda

class usuario:
    '''
    Entidad que representa a un usuario, con sus datos identificativos
    y con la informacion de todas las deudas que tiene pendientes
    '''
    
    def __init__(self, u):
        self.__usuario = u
        self.__deudas = []

    #=================================================================
    
    def insertarDeuda(self, deuda):
        if(deuda.nickUsuarioQuePaga() == self.obtenerNickUsuario()):
            self.__deudas.append(deuda)

    def eliminarDeuda(self, deuda):
        self.__deudas.remove(deuda)

    #=================================================================
        
    def obtenerInfoUsuario(self):
        return self.__usuario
    
    def obtenerListaDeudasString(self):
        output = ""
        output += "=========================================================\n"
        output += "Lista de deudas:\n"
        output += "=========================================================\n"
        if self.__deudas:
            for deuda in self.__deudas:
                output += "-> Fecha: " + deuda.obtenerFechaDeuda() + " || "
                output += "Importe: " + str(deuda.importe) + " || "
                output += "Concepto: " + deuda.concepto + " || "
                output += "Pagar A: " + deuda.nickUsuarioDeber() + "\n"

            output += "\n"
        else:
            output += "-> No hay deudas pendientes de pago.\n"

        return output

    #=================================================================
    
    def printListaDeudas(self):
        print(self.obtenerListaDeudasString())

    def __str__(self):
        output = ""
        output += self.__usuario.__str__() + "\n"
        output += self.obtenerListaDeudasString()

        return output


#Test de clase
if __name__ == "__main__":
    pass