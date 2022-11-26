from usuario import usuario
from infoUsuario import infoUsuario
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
        nicks = [usuario.obtenerInfoUsuario().nickname.lower() for usuario in self.__usuarios]

        return nicks
    
    def __buscarUsuarioPorNick(self,nick):
        '''
        Para la lista de usuarios que participan en el gasto compartido,
        se permite buscar un usuario a traves de su nick
        Param nick: nickname del usuario a buscar
        Return: copia del usuario a buscar. None en otro caso
        '''
        usuarioCandidato = [usuario for usuario in self.__usuarios if usuario.obtenerInfoUsuario().nickname == nick.lower()]

        if(usuarioCandidato):
            return usuarioCandidato[0]
        else:
            return None
    
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
        self.__fecha = dt.today()
        self.__usuarios = self.__init__usuarios(usuarios)
        self.__gastos = []
        self.__deudas = []

    #============================================================================
        
    def registrarUsuario(self,nickname,nombre,apellidos):
        '''
        Metodo para registrar usuarios participantes en este gasto compartido
        Param nickname: Nick del nuevo usuario participante
        Param nombre: Nombre del nuevo usuario participante
        Param apellidos: Apellidos del nuevo usuario participante

        Precond: Si el nickname del usuario ya existe, no se registra
        '''
        if(self.__buscarUsuarioPorNick(nickname) is None):
            idNuevoUsuario = self.__generarIDUsuario()
            self.__usuarios.append(usuario(infoUsuario(idNuevoUsuario,nickname,nombre,apellidos)))


    def eliminarUsuario(self,nickname):
        '''
        Metodo para eliminar usuarios participantes en el gasto a traves de nick
        Param nickname: Nick del usuario a eliminar

        Precond: Si el nick no pertenece a ningun usuario presente, no se borra nada
        '''

        usuarioCandidato = self.__buscarUsuarioPorNick(nickname)
        if(usuarioCandidato is not None):
            self.__usuarios.remove(usuarioCandidato)

    #============================================================================
        
    def generarGasto(self,nickname,importe,concepto):
        '''
        Metodo para generar un gasto realizado por un usuario
        Param nickname: Nickname del usuario que genera el gasto
        Param importe: Cantidad del gasto
        Param concepto: Descripcion del gasto

        Precond: si el nick del usuario no se encuentra dentro de los usuarios
        participantes, no se almacenara el nuevo gasto
        '''
        usuarioCandidato = self.__buscarUsuarioPorNick(nickname)
        if(usuarioCandidato is not None):
            idNuevoGasto = self.__generarIDGasto()
            self.__gastos.append(gasto(idNuevoGasto,usuarioCandidato.obtenerInfoUsuario(),importe,concepto))

    def obtenerGastosPorNick(self,nickname):
        '''
        Metodo que permite buscar todos los gastos realizados por un
        usuario especificado por su nick
        Param nick: Nick de usuario
        Return: Lista de gastos asociados al usuario. Si usuario no participa
        en este gastoCompartido, se devuelve None
        '''
        usuarioCandidato = self.__buscarUsuarioPorNick(nickname)
        if(usuarioCandidato is not None):
            return self.__buscarGastosPorNick(nickname)
        
    def obtenerUsuarios(self):
        '''
        Metodo que devuelve una copia de la lista de usuarios del gasto
        compartido.
        Return: Lista de usuarios (copia)
        '''
        return [usuario for usuario in self.__usuario]
        
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
            usuarioDeber = self.__buscarUsuarioPorNick(nickURecibe).obtenerInfoUsuario()
            usuarioDeudor = self.__buscarUsuarioPorNick(nickUPaga).obtenerInfoUsuario()
            
            self.__deudas.append(deuda(idDeuda,usuarioDeber,usuarioDeudor,importe,concepto))
        
#Test de clase
if __name__ == "__main__":
    pass
