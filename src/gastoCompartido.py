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
        
    def __buscarGastosPorNick(self,nick):
        '''
        Para la lista de usuarios que participan en el gasto compartido,
        se permite buscar todos los gastos asociados a un usuario a traves de su nick
        Param nick: nicnkame del usuario del que queremos sus gastos
        Return: lista de gastos asociados al usuario.
        '''
        return [gasto for gasto in self.__gastos if gasto.nickUsuarioGasto() == nick]
    
    def __generarIDGasto(self):
        '''
        Metodo que permite obtener un identificador unico para un
        gasto generado para este gasto compartido
        Return: numero identificador
        '''
        ultimoIndice = 0
        
        indices = [gasto.id for gasto in self.__gastos]
        if indices:
            ultimoIndice = max(indices)

        return ultimoIndice+1
    

    def __generarIDDeuda(self):
        '''
        Metodo que permite obtener un identificador unico para una deuda
        generada para este gasto compartido
        Return: numero identificador
        '''
        ultimoIndice = 0

        indices = [deuda.id for deuda in self.__deudas]
        if indices:
            ultimoIndice = max(indices)

        return ultimoIndice+1

    def __generarIDUsuario(self):
        '''
        Metodo que permite obtener un identificador unico para un usaurio
        participante en este gasto compartido
        Return: numero identificador
        '''
        ultimoIndice = 0
        
        indices = [usuario.obtenerInfoUsuario().id for usuario in self.__usuarios]
        if indices:
            ultimoIndice = max(indices)

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
            infoUsuario = usuario.obtenerInfoUsuario()
            output += "Id: " + str(infoUsuario.id) + " || "
            output += "Nickname: " + infoUsuario.nickname + " || "
            output += "Nombre: " + infoUsuario.nombre + " || "
            output += "Apellidos: " + infoUsuario.apellidos + "\n"

        output += "\n"

        return output
    
    def __obtenerListaGastosString(self,nickname=""):
        '''
        Metodo que permite obtener en formato string la lista de gastos
        realizados por los participantes en el gasto compartido
        Param nickname: Si se especifica un nick de usuario, se recuperan
        los gastos unicamente de una persona. Si el nick no pertenece a ningun
        usuario, entonces se devuelve la lista general
        Return: lista de gastos en string (todos o de un usuario concreto)
        '''
        output = ""

        if nickname != "" and self.__buscarUsuarioPorNick(nickname) is not None:
            gastos = self.__buscarGastosPorNick(nickname)
        else:
            gastos = self.__gastos

        for gasto in gastos:
            output += "Id: " + str(gasto.id) + " || "
            output += "Pagado por: " + gasto.nickUsuarioGasto() + " || "
            output += "Importe: " + str(gasto.importe) + "€ || "
            output += "Concepto: " + gasto.concepto + "\n"

        output += "\n"

        return output

    def __obtenerListaDeudasString(self):
        '''
        Metodo que permite obtener en formato string la lista de deudas
        realizadas por los participantes en el gasto compartido
        Return: lista de deudas en string
        '''
        output = ""

        for deuda in self.__deudas:
            output += "Id: " + str(deuda.id) + " || "
            output += "Fecha: " + deuda.obtenerFechaDeuda() + " || "
            output += "Importe: " + str(deuda.importe) + " || "
            output += "Concepto: " + deuda.concepto + " || "
            output += "Pagar A: " + deuda.nickUsuarioDeber() + " || "
            output += "Quien Paga: " + deuda.nickUsuarioQuePaga() + "\n"

        output += "\n"

        return output
    
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

    def imprimirListaGastos(self,nickname=""):
        '''
        Metodo que imprime la lista de gastos realizados en este gasto compartido.
        Si se especifica un nickname, permite ver los gastos asociados a un usuario
        en concreto participante

        Param nickname: nick del usuario a buscar la lista de gastos
        '''
        output = ""
        output += "=========================================================\n"
        output += "Lista de gastos:\n"
        output += "=========================================================\n"
        output += self.__obtenerListaGastosString(nickname)
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
        
#Test de clase
if __name__ == "__main__":
    #Objeto de prueba
    gastoC1 = gastoCompartido(1, "Test")

    #Test de insercion/Impresion de usuarios
    gastoC1.registrarUsuario("danielsp","Daniel","Pérez Ruiz")
    gastoC1.registrarUsuario("pnl","Pablo","Nieto López")
    gastoC1.registrarUsuario("jac","Jose","Abela Canovas")
    #gastoC1.registrarUsuario("manaya","Martin","Anaya Quesada")


    gastoC1.imprimirListaUsuarios()

    #Test de generacion de gastos

    gastoC1.generarGasto("danielsp",5.75,"Comida")
    gastoC1.generarGasto("pnl",20,"Alquiler")
    gastoC1.generarGasto("jac",3,"Kebab")
    gastoC1.generarGasto("danielsp",11,"Gasolina")
    gastoC1.generarGasto("danielsp",0.50,"Peaje")
    gastoC1.generarGasto("manaya",100,"Fiesta")


    gastoC1.imprimirListaGastos()

    gastoC1.generarDeuda("danielsp","pnl",20,"Test")

    gastoC1.imprimirListaDeudas()
