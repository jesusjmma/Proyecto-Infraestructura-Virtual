from infoUsuario import infoUsuario
from deuda import deuda

class usuario:
    '''
    Entidad que representa a un usuario, con sus datos identificativos
    y con la informacion de todas las deudas que tiene pendientes
    '''
    
    def __init__(self, u):
        '''
        Constructor de la clase
        Param u : informacion de un usuario
        '''
        #Informacion del usuario
        self.__usuario = u
        #Listado de deudas pendientes
        self.__deudas = []

    #=================================================================
    
    def insertarDeuda(self, deuda):
        '''
        Asigna una nueva deuda al usuario
        Param deuda: nueva deuda
        '''

        #Se inserta sii la deuda corresponde con el usuario
        if(deuda.nickUsuarioQuePaga() == self.obtenerNickUsuario()):
            self.__deudas.append(deuda)

    def eliminarDeuda(self, deuda):
        '''
        Elimina una deuda al usuario, a traves del objeto
        Param deuda: deuda a eliminar
        '''
        self.__deudas.remove(deuda)

    #=================================================================
        
    def obtenerInfoUsuario(self):
        '''
        Recupera la informacion completa asociada a un usuario
        Return: informacion completa del usuario
        '''
        return self.__usuario
    
    def obtenerListaDeudasString(self):
        '''
        Obtiene en formato string la lista de deudas del usuario
        Return: String con la lista de deudas de usuario
        '''
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
    
    def obtenerCantidadTotalDeberString(self):
        '''
        Calcula el total de dinero que debe el usuario (sin distincion de
        a quien debe pagar)
        Return suma de dinero de todas las deudas (en String)
        '''
        total = 0.0

        if self.__deudas:
            for deuda in self.__deudas:
                total += deuda.importe

        return str(total) + " €"

    #=================================================================
    
    def printListaDeudas(self):
        '''
        Imprime la lista de deudas asociadas al usuario
        '''
        print(self.obtenerListaDeudasString())

    def printCantidadTotalDeber(self):
        '''
        Imprime por pantalla la cantidad total a deber
        '''
        print("-> Dinero total a deber: " + self.obtenerCantidadTotalDeberString())

    def __str__(self):
        '''
        Representacion de la clase a formato legible
        '''
        output = ""
        output += self.__usuario.__str__() + "\n"
        output += self.obtenerListaDeudasString()
        output += "-> Dinero total a deber: " + self.obtenerCantidadTotalDeberString()

        return output


#Test de clase
if __name__ == "__main__":
    pass