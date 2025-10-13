from .board import Board
from .player import Player
from .dice import Dice
from .checker import Checker
import random

class BackgammonGame:
    """
    Clase orquestadora que gestiona el estado y el flujo de una partida de Backgammon.
    """
    def __init__(self, nombre_jugador1: str, nombre_jugador2: str):
        """
        Inicializa el juego con sus componentes principales.
        """
        self._tablero_ = Board()
        # Por convención, el jugador 1 suele ser el negro y empieza
        self._jugador1_ = Player(nombre=nombre_jugador1, color="negro")
        self._jugador2_ = Player(nombre=nombre_jugador2, color="blanco")
        self._dados_ = Dice()
        
        self._jugador_actual_ = None
        self._juego_terminado_ = False
        self._ganador_ = None

    def iniciar_juego(self):
        """
        Prepara el tablero para una nueva partida y elige al azar quién empieza.
        """
        self._tablero_.configurar_tablero_inicial()
        # Asignamos las 15 fichas a cada jugador
        self._jugador1_._fichas_ = [Checker(color="negro") for _ in range(15)]
        self._jugador2_._fichas_ = [Checker(color="blanco") for _ in range(15)]
        
        # Elegimos al azar qué jugador empieza
        self._jugador_actual_ = random.choice([self._jugador1_, self._jugador2_])

    def cambiar_jugador(self):
        """
        Cambia el turno al siguiente jugador.
        """
        if self._jugador_actual_ == self._jugador1_:
            self._jugador_actual_ = self._jugador2_
        else:
            self._jugador_actual_ = self._jugador1_

    def _verificar_ganador_(self):
        """
        Comprueba si alguno de los jugadores ha sacado todas sus fichas.
        Si es así, actualiza el estado del juego para declararlo terminado.
        """
        # Verificamos si el jugador 1 (negras) ha ganado
        if len(self._tablero_._fichas_fuera_["negro"]) == 15:
            self._juego_terminado_ = True
            self._ganador_ = self._jugador1_
            return

        # Verificamos si el jugador 2 (blancas) ha ganado
        if len(self._tablero_._fichas_fuera_["blanco"]) == 15:
            self._juego_terminado_ = True
            self._ganador_ = self._jugador2_
            return        

