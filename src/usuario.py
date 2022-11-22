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

    

#Test de clase
if __name__ == "__main__":
    pass