import random

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
        self._tablero_ = Board()
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
        """
        if self._tablero_.obtener_cantidad_fichas_fuera("negro") == 15:
            self._juego_terminado_ = True
            self._ganador_ = self._jugador1_
            return

        if self._tablero_.obtener_cantidad_fichas_fuera("blanco") == 15:
            self._juego_terminado_ = True
            self._ganador_ = self._jugador2_
            return

    def realizar_movimiento(self, origen: int, destino: int):
        """
        Intenta realizar un movimiento completo: valida, mueve y consume la tirada.
        Devuelve un código de estado.
        """
        jugador_actual = self._jugador_actual_
        
        if not self._tablero_.es_movimiento_valido(jugador_actual, origen, destino):
            return "MOVIMIENTO_ILEGAL"

        if origen == 0:
            distancia = destino
        elif destino == 25:
            distancia = 25 - origen
        else:
            distancia = abs(destino - origen)

        tiradas_disponibles = self._dados_._tiradas_disponibles_
        
        if distancia in tiradas_disponibles:
            if destino == 25:
                self._tablero_.sacar_ficha(origen)
            else:
                self._tablero_.mover_ficha(origen, destino)
            
            tiradas_disponibles.remove(distancia)
            self._verificar_ganador_() 
                
            return "OK"
        else:
            return "TIRADA_NO_DISPONIBLE"