from dataclasses import dataclass

@dataclass(frozen=True)
class infoUsuario:
    '''
    Clase que representa a un usuario. Contiene todos los datos de identificación del usuario.
    '''
    nickname: str
    nombre: str
    apellidos: str
    
#Test de clase
if __name__ == "__main__":
    pass
