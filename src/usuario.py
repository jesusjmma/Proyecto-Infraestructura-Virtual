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

#Test de clase
if __name__ == "__main__":
    pass