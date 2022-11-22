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

    def __obtenerNicksUsuarios(self):
        '''
        Para la lista de usuarios que participan en el gasto compartido,
        se genera una lista con los nicks de los usuarios
        Return: lista de nicks de usuario participantes
        '''
        nicks = []
        for usuario in self.__usuarios:
            nicks.append(usuario.nickname)

        return nicks
    
    def __buscarUsuarioPorNick(self,nick):
        '''
        Para la lista de usuarios que participan en el gasto compartido,
        se permite buscar un usuario a traves de su nick
        Param nick: nickname del usuario a buscar
        Return: copia del usuario a buscar. NULL en otro caso
        '''
        pass

    def __obtenerTotalDeudas(self):
        '''
        Para este gasto compartido, se devuelve el numero total de
        deudas existentes
        Return: numero total de deudas
        '''
        return len(self.__deudas)
    
    def __generarIDDeuda(self):
        '''
        
        '''
        pass

    
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

    def generarDeuda(self,nickURecibe,nickUPaga,importe,concepto):
        '''
        Dentro de los usuarios que participan en el gasto compartido, este
        metodo permite generar una deuda comun que se insertara a la lista
        de deudas
        Param nickURecibe: nickname del usuario al que hay que pagar
        Param nickUPaga: nickname del usuario que paga la deuda
        Param importe: importe de la deuda
        Param concepto: concepto de la deuda

        Precond: Si alguno de los dos nicks son de usuarios que no participan,
        la insercion de la deuda no sera realizada
        '''
        if nickURecibe in self.__obtenerNicksUsuarios() and nickUPaga in self.__obtenerNicksUsuarios():
            idDeuda = self.__generarIDDeuda()
            usuarioDeber = self.__buscarUsuarioPorNick(nickURecibe)
            usuarioDeudor = self.__buscarUsuarioPorNick(nickUPaga)
            
            self.__deudas.append(deuda(idDeuda,usuarioDeber,usuarioDeudor,importe,concepto))

            
    #============================================================================

    def __str__(self):
        '''
        Representacion de la clase a formato legible
        '''
        pass
        
#Test de clase
if __name__ == "__main__":
    pass