from infoUsuario import infoUsuario
from deuda import deuda

class usuario:
    '''
    Entidad que representa a un usuario, con sus datos identificativos
    y con la informacion de todas las deudas que tiene pendientes
    '''
    
    def __init__(self, u, deudas=[]):
        self.__usuario = u
        self.__deudas = [deuda for deuda in deudas if deuda.nickUsuarioQuePaga() == self.__usuario.nickname]

#Test de clase
if __name__ == "__main__":
    pass