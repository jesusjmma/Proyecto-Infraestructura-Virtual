from gasto import gasto

class usuario:

    def __init__(self,nickname,gastos=[]):
        self.__nickname = nickname.lower()
        self.__gastos = [gasto for gasto in gastos if self.__nickname in gasto.nicksParticipantes]

    
    def getNickname(self):
        return self.__nickname
    
    def getGastos(self):
        return self.__gastos.copy()