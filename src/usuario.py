
class usuario:
    '''
    Entidad que representa a un usuario, mediante un identificador único (nickname)
    y una lista de deudas
    '''
    
    def __init__(self,nick,deudas):
        self.__nick = nick.lower()
        self.__deudas = [deuda for deuda in deudas]