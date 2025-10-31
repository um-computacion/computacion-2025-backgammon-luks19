import random
from typing import Union

from .board import Board
from .player import Player
from .dice import Dice

class BackgammonGame:
    """
    Clase orquestadora que gestiona el estado y el flujo de una partida de Backgammon.
    """
    def __init__(self, nombre_jugador1: str, nombre_jugador2: str):
        """
        Inicializa el juego con sus componentes principales.
        """
        # --- Atributos con Tipos para Máxima Claridad ---
        self._tablero_: Board = Board()
        self._jugador1_: Player = Player(nombre=nombre_jugador1, color="negro")
        self._jugador2_: Player = Player(nombre=nombre_jugador2, color="blanco")
        self._dados_: Dice = Dice()
        
        self._jugador_actual_: Union[Player, None] = None
        self._juego_terminado_: bool = False
        self._ganador_: Union[Player, None] = None

    def iniciar_juego(self):
        """
        Prepara el tablero para una nueva partida y elige al azar quién empieza.
        """
        self._tablero_.configurar_tablero_inicial()
        
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
        # --- Lógica mejorada usando el nuevo método de Board ---
        # Verificamos si el jugador 1 (negras) ha ganado
        if self._tablero_.obtener_cantidad_fichas_fuera("negro") == 15:
            self._juego_terminado_ = True
            self._ganador_ = self._jugador1_
            return

        # Verificamos si el jugador 2 (blancas) ha ganado
        if self._tablero_.obtener_cantidad_fichas_fuera("blanco") == 15:
            self._juego_terminado_ = True
            self._ganador_ = self._jugador2_
            return
