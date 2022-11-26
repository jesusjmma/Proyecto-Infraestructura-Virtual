from usuario import usuario
from infoUsuario import infoUsuario
from deuda import deuda
from gasto import gasto

class gastoCompartido:
    '''
    Entidad que representa a un gasto en el que se ven involucrados una serie de
    usuarios de la aplicacion, y donde todos tienen una aportacion

    Se define con un nombre identificativo del gasto, una lista de usuarios
    participantes, y una lista de deudas
    '''
    
    #============================================================================

    def __obtenerNicksUsuarios(self):
        '''
        Para la lista de usuarios que participan en el gasto compartido,
        se genera una lista con los nicks de los usuarios
        Return: lista de nicks de usuario participantes
        '''
        nicks = [usuario.obtenerInfoUsuario().nickname.lower() for usuario in self.__usuarios]

        return nicks
    
    
    #============================================================================

    def __init__(self,id,nombre,usuarios=[]):
        '''
        Constructor de la clase. Se define un numero identificador del gasto
        compartido, un nombre, una fecha en la que se produjo el gasto compartido,
        una lista de usuarios, una lista comun de gastos realizados por los usuarios,
        y una lista de deudas entre usuarios
        '''
        self.__id = id
        self.__nombre = nombre
        self.__usuarios = [usuario for usuario in usuarios]
        self.__gastos = []
        self.__deudas = []
        
#Test de clase
if __name__ == "__main__":
    pass
