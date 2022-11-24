from usuario import usuario
from deuda import deuda
from gasto import gasto
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
        Return: copia del usuario a buscar. None en otro caso
        '''
        pass

    def __obtenerTotalGastos(self):
        '''
        Para este gasto compartido, se devuelve el numero total de
        gastos existentes
        Return: numero total de gastos
        '''
        return len(self.__gastos)
    
    def __generarIDGasto(self):
        '''
        Metodo que permite obtener un identificador unico para un
        gasto generado para este gasto compartido
        Return: numero identificador
        '''
        pass
    

    def __generarIDDeuda(self):
        '''
        Metodo que permite obtener un identificador unico para una deuda
        generada para este gasto compartido
        Return: numero identificador
        '''
        pass

    def __generarIDUsuario(self):
        '''
        Metodo que permite obtener un identificador unico para un usaurio
        participante en este gasto compartido
        Return: numero identificador
        '''
        pass
    
    #============================================================================

    def __init__(self,id,nombre,usuarios):
        '''
        Constructor de la clase. Se define un numero identificador del gasto
        compartido, un nombre, una fecha en la que se produjo el gasto compartido,
        una lista de usuarios, una lista comun de gastos realizados por los usuarios,
        y una lista de deudas entre usuarios
        '''
        self.__id = id
        self.__nombre = nombre
        self.__fecha = dt.today()
        self.__usuarios = self.__init__usuarios(usuarios)
        self.__gastos = []

    #============================================================================
        
    def registrarUsuario(self,nickname,Nombre,Apellidos):
        '''
        Metodo para registrar usuarios participantes en este gasto compartido
        Param nickname: Nick del nuevo usuario participante
        Param nombre: Nombre del nuevo usuario participante
        Param apellidos: Apellidos del nuevo usuario participante

        Precond: Si el nickname del usuario ya existe, no se registra
        '''
        pass

    def eliminarUsuario(self,nick):
        '''
        Metodo para eliminar usuarios participantes en el gasto a traves de nick
        Param nick: Nick del usuario a eliminar

        Precond: Si el nick no pertenece a ningun usuario presente, no se borra nada
        '''
        pass

    #============================================================================
        
    def generarGasto(self,infoUsuario,importe,concepto):
        '''
        Metodo para generar un gasto realizado por un usuario
        Param infoUsuario: Informacion de usuario que realiza gasto
        Param importe: Cantidad del gasto
        Param concepto: Descripcion del gasto
        '''
        pass

    def borrarGastoPorNick(self,nick):
        '''
        Metodo para borrar todos los gastos realizados por un usuari
        especificado por su nick
        Param nick: Nick de usuario
        '''
        pass

    def buscarGastosPorNick(self,nick):
        '''
        Metodo que permite buscar todos los gastos realizados por un
        usuario especificado por su nick
        Param nick: Nick de usuario
        Return: Lista de gastos asociados al usuario. Si usuario no participa
        en este gastoCompartido, se devuelve array vacio
        '''
        pass
        
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