from infoUsuario import infoUsuario
from deuda import deuda

class usuario:
    '''
    Entidad que representa a un usuario, con sus datos identificativos
    y ademas contiene la informacion de todas las deudas que tiene pendientes
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

    def eliminarDeudaPorId(self,idDeuda):
        '''
        Elimina una deuda al usuario, a traves de su id
        Param idDeuda: id de deuda a Eliminar
        '''
        pass

    #=================================================================

    def obtenerNickUsuario(self):
        '''
        Recupera el nick del usuario
        Return: nick usuario
        '''
        return self.__usuario.nickname

    #=================================================================
    
    def printListaDeudas(self):
        '''
        Imprime la lista de deudas asociadas al usuario
        '''
        pass

    def printCantidadTotalDeber(self):
        '''
        Imprime por pantalla la cantidad total a deber
        '''
        pass

    def __str__(self):
        '''
        Representacion de la clase a formato legible
        '''
        pass

#Test de clase
if __name__ == "__main__":
    pass