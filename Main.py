# importar la libreria pydub --> Poner en la terminal: pip install pydub

from pydub import AudioSegment
from pydub.playback import play


class Letra:
    def __init__(self, caracter: str, posicion: int):
        self.caracter: str = caracter.upper()
        self.posicion: int = posicion
        self.estado: str = "oculta"  # "correcta", "contenida", "incorrecta"



class Cancion:
    def __init__(self,titulo: str, fragmentos_audio: dict[int,str]):
        self.titulo: str = titulo
        self.fragmentos_audio: dict[int,str] = fragmentos_audio


class Jugador:
    pass

class WordleMusic:
    pass
