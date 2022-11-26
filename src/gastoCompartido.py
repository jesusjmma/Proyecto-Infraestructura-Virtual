from usuario import usuario
from infoUsuario import infoUsuario
from deuda import deuda
from gasto import gasto

class gastoCompartido:
    '''
    Entidad que representa a un gasto en el que se ven involucrados una serie de
    usuarios de la aplicacion, y donde todos tienen una aportacion, ya sea
    mediante un gasto, o una deuda

    Se define con un nombre identificativo del gasto, una lista de usuarios
    participantes, una lista de gastos cometidos, y una lista de deudas
    '''

    def __init__(self,id,nombre,usuarios=[],gastos=[],deudas=[]):
        self.__id = id
        self.__nombre = nombre
        self.__usuarios = [usuario for usuario in usuarios]
        self.__gastos = [gasto for gasto in gastos]
        self.__deudas = [deuda for deuda in deudas]
        
#Test de clase
if __name__ == "__main__":
    pass