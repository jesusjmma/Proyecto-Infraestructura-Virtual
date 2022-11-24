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
        nicks = []
        for usuario in self.__usuarios:
            nicks.append(usuario.nickname.lower())

        return nicks
    
    def __buscarUsuarioPorNick(self,nick):
        '''
        Para la lista de usuarios que participan en el gasto compartido,
        se permite buscar un usuario a traves de su nick
        Param nick: nickname del usuario a buscar
        Return: copia del usuario a buscar. None en otro caso
        '''
        usuarioCandidato = [usuario for usuario in self.__usuarios if usuario.nickname == nick]

        if(usuarioCandidato):
            return usuarioCandidato
        else:
            return None

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
        ultimoIndice = max([gasto.id for gasto in self.__gastos])

        return ultimoIndice+1
    

    def __generarIDDeuda(self):
        '''
        Metodo que permite obtener un identificador unico para una deuda
        generada para este gasto compartido
        Return: numero identificador
        '''
        ultimoIndice = max([deuda.id for deuda in self.__deudas])

        return ultimoIndice+1

    def __generarIDUsuario(self):
        '''
        Metodo que permite obtener un identificador unico para un usaurio
        participante en este gasto compartido
        Return: numero identificador
        '''
        ultimoIndice = max([usuario.id for usuario in self.__usuarios])

        return ultimoIndice+1

    #============================================================================

    def __obtenerListaUsuariosString(self):
        '''
        Metodo que permite obtener en formato string la lista de usuarios
        participantes del gasto compartido
        Return: lista de usuarios en string
        '''
        output = ""

        for usuario in self.__usuarios:
            output += "Id: " + usuario.id + " || "
            output += "Nickname: " + usuario.nickname + " || "
            output += "Nombre: " + usuario.nickname + " || "
            output += "Apellidos: " + usuario.nickname + "\n"

        output += "\n"

        return output
    
    def __obtenerListaGastosString(self):
        '''
        Metodo que permite obtener en formato string la lista de gastos
        realizados por los participantes en el gasto compartido
        Return: lista de gastos en string
        '''
        output = ""

        for gasto in self.__gastos:
            output += "Id: " + gasto.id + " || "
            output += "Pagado por: " + gasto.nickUsuarioGasto() + " || "
            output += "Importe: " + gasto.importe + " || "
            output += "Concepto: " + gasto.concepto + "\n"

        output += "\n"

    def __obtenerListaDeudasString(self):
        '''
        Metodo que permite obtener en formato string la lista de deudas
        realizadas por los participantes en el gasto compartido
        Return: lista de deudas en string
        '''
        output = ""

        for deuda in self.__deudas:
            output += "Id: " + deuda.id + " || "
            output += "Fecha: " + deuda.obtenerFechaDeuda() + " || "
            output += "Importe: " + str(deuda.importe) + " || "
            output += "Concepto: " + deuda.concepto + " || "
            output += "Pagar A: " + deuda.nickUsuarioDeber() + " || "
            output += "Quien Paga: " + deuda.nickUsuarioQuePaga() + "\n"

        output += "\n"
    
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
            
    def imprimirListaUsuarios(self):
        '''
        Metodo que imprime la lista de usuarios participantes en este gasto
        compartido.
        '''
        output = ""
        output += "=========================================================\n"
        output += "Lista de usuarios:\n"
        output += "=========================================================\n"
        output += self.__obtenerListaUsuariosString()
        print(output)

    def imprimitListaGastos(self):
        '''
        Metodo que imprime la lista de gastos realizados en este gasto compartido
        '''
        output = ""
        output += "=========================================================\n"
        output += "Lista de gastos:\n"
        output += "=========================================================\n"
        output += self.__obtenerListaGastosString()
        print(output)

    def imprimirListaDeudas(self):
        '''
        Metodo que imprime la lista de de deudas realizadas en este gasto compartido
        '''
        output = ""
        output += "=========================================================\n"
        output += "Lista de deudas:\n"
        output += "=========================================================\n"
        output += self.__obtenerListaDeudasString()
        print(output)

    def __str__(self):
        '''
        Representacion de la clase a formato legible
        '''
        pass
        
#Test de clase
if __name__ == "__main__":
    pass
