from dataclasses import dataclass

@dataclass(frozen=True)
class infoUsuario:
    '''
    Clase que representa a un usuario. Contiene todos los datos de identificación del usuario.
    '''
    nickname: str
    nombre: str
    apellidos: str

    def __str__(self):
        output = ""
        output += " -- Nickname: " + self.nickname + "\n"
        output += " -- Nombre: " + self.nombre + "\n"
        output += " -- Apellidos: " + self.apellidos + "\n"

        return output
    
#Test de clase
if __name__ == "__main__":
    pass
