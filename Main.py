# importar la libreria pydub --> Poner en la terminal: pip install pydub

from pydub import AudioSegment
from pydub.playback import play
import random


class Letra:
    pass

class Cancion:
    pass

class Jugador:
    def __init__(self, nombre: str):
        self.nombre: str = nombre
        self.intentos_realizados: int = 0
        self.aciertos: list[int] = []

    def ingresar_intento(self, palabra: str) -> str:
        self.intentos_realizados += 1
        return palabra

    def obtener_aciertos(self) -> list[int]:
        return self.aciertos

class WordleMusic:
    def __init__(self, canciones: list[Cancion], max_intentos: int = 6):
        self.canciones: list[Cancion] = canciones
        self.cancion_actual: Cancion = None
        self.jugador: Jugador = None
        self.intentos_restantes: int = max_intentos
        self.max_intentos: int = max_intentos

    def registrar_jugador(self, nombre: str) -> None:
        self.jugador: Jugador = Jugador(nombre)

    def seleccionar_cancion(self) -> None:                  # Este metodo elige aleatoriamente una canción de la lista.
        self.cancion_actual = random.choice(self.canciones)
        self.intentos_restantes = self.max_intentos

    def inicializar_tablero(self) -> int:                   # Devuelve el número de letras de la canción actual.
        if not self.cancion_actual:
            raise ValueError("No hay canción seleccionada.")
        return len(self.cancion_actual.titulo)

    def validar_intento(self, palabra: str) -> list[Letra]:    # Valida un intento contra el título actual.
        if not self.cancion_actual:
            raise ValueError("No hay canción seleccionada.")

        intento = self.jugador.ingresar_intento(palabra)
        self.intentos_restantes -= 1
        return self.cancion_actual.comparar_letras(intento)

    def finalizar_juego(self) -> str:                         # Retorna el título correcto de la canción.
        if not self.cancion_actual:
            raise ValueError("No hay canción seleccionada.")
        return self.cancion_actual.mostrar_titulo_correcto()