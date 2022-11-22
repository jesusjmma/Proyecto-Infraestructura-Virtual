from usuario import usuario
from deuda import deuda
from datetime import datetime as dt

class gastoCompartido:
    '''
    Entidad que representa a un gasto en el que se ven involucrados una serie de
    usuarios de la aplicacion, y donde todos tienen una aportacion

    Se define con un nombre identificativo del gasto, una lista de usuarios
    participantes, y una lista de deudas
    '''
    
    #============================================================================

    def __init__usuarios(self, usuarios):
        '''
        Copia una lista de usuarios en otra lista
        (evita duplicado de punteros)
        Return: copia de usuarios
        '''
        listaUsuarios = []
        for usuario in usuarios:
            usuarios.append(usuario)

        return listaUsuarios
    
    #============================================================================

    def __init__(self,id,nombre,usuarios):
        '''
        Constructor de la clase. Se define un numero identificador del gasto
        compartido, un nombre, una fecha en la que se produjo el gasto compartido,
        una lista de usuarios y una lista comun de deudas
        '''
        self.__id = id
        self.__nombre = nombre
        self.__fecha = dt.today()
        self.__usuarios = self.__init__usuarios(usuarios)
        self.__deudas = []

    #============================================================================

    def __str__(self):
        '''
        Representacion de la clase a formato legible
        '''
        pass
        
#Test de clase
if __name__ == "__main__":
    pass