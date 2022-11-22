from infoUsuario import infoUsuario
from deuda import deuda

class usuario:
    '''
    Entidad que representa a un usuario, con sus datos identificativos
    y con la informacion de todas las deudas que tiene pendientes
    '''
    
    def __init__(self, u):
        '''
        Constructor de la clase
        Param u : informacion de un usuario
        '''
        #Informacion del usuario
        self.__usuario = u
        #Listado de deudas pendientes
        self.__deudas = []

    #=================================================================
    
    def insertarDeuda(self, deuda):
        '''
        Asigna una nueva deuda al usuario
        Param deuda: nueva deuda
        '''

        #Se inserta sii la deuda corresponde con el usuario
        if(deuda.nickUsuarioQuePaga() == self.obtenerNickUsuario()):
            self.__deudas.append(deuda)

    def eliminarDeuda(self, deuda):
        '''
        Elimina una deuda al usuario, a traves del objeto
        Param deuda: deuda a eliminar
        '''
        self.__deudas.remove(deuda)

    def eliminarDeudaPorId(self,idDeuda):
        '''
        Elimina una deuda al usuario, a traves de su id
        Param idDeuda: id de deuda a Eliminar
        '''
        pass

    #=================================================================

    def obtenerNickUsuario(self):
        '''
        Recupera el nick del usuario
        Return: nick usuario
        '''
        return self.__usuario.nickname

    #=================================================================
    
    def printListaDeudas(self):
        '''
        Imprime la lista de deudas asociadas al usuario
        '''
        output = ""
        output += "=========================================================\n"
        if self.__deudas:
            for deuda in self.__deudas:
                output += "-> Fecha: " + deuda.obtenerFechaDeuda() + " || "
                output += "Importe: " + str(deuda.importe) + " || "
                output += "Concepto: " + deuda.concepto + " || "
                output += "Pagar A: " + deuda.nickUsuarioDeber() + "\n"

            output += "\n"
        else:
            output += "-> No hay deudas pendientes de pago.\n"

        print(output)

    def printCantidadTotalDeber(self):
        '''
        Imprime por pantalla la cantidad total a deber
        '''
        pass

    def __str__(self):
        '''
        Representacion de la clase a formato legible
        '''
        pass

#Test de clase
if __name__ == "__main__":
    infU1 = infoUsuario(1,"danielsp","Daniel","Pérez Ruiz")
    infU2 = infoUsuario(2,"pnl","Pablo","Nieto López")
    infU3 = infoUsuario(3,"jac","Jose","Abela Cánovas")

    d1 = deuda(1,infU2,infU1,10.5,"test deuda1")
    d2 = deuda(2,infU2,infU3,5.5,"test deuda2")

    u1 = usuario(infU1)

    u1.insertarDeuda(d1)
    u1.insertarDeuda(d2)

    u1.printListaDeudas()

    u1.eliminarDeuda(d1)

    u1.printListaDeudas()
