from gasto import gasto

class usuario:
    '''
    Entidad que representa a un usuario, a través de un identificador
    unívoco mediante nickname y un conjunto de gastos pendientes de pago
    '''

    def __init__(self,nickname,gastos=[]):
        self.__nickname = nickname.lower()
        self.__gastos = [gasto for gasto in gastos if self.__nickname in gasto.nicksParticipantes]

    
    def getNickname(self):
        return self.__nickname
    
    def getGastos(self):
        return self.__gastos.copy()