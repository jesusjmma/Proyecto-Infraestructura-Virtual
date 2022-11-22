from dataclasses import dataclass

@dataclass(frozen=True)
class usuario:
    '''
    Clase que representa a un usuario. Contiene todos los datos de identificación del usuario.
    '''
    id: int
    nickname: str
    nombre: str
    apellidos: str

    def __str__(self):
        '''
        Representacion de la clase a formato legible
        '''
        output = ""
        output += "=============================================\n"
        output += "ID Usuario: " + str(self.id) + "\n"
        output += "=============================================\n"
        output += " -- Nickname: " + self.nickname + "\n"
        output += " -- Nombre: " + self.nombre + "\n"
        output += " -- Apellidos: " + self.apellidos + "\n"

        return output
    
#Test de clase
if __name__ == "__main__":
    pass
