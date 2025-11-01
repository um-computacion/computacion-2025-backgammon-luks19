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

def realizar_movimiento(self, origen: int, destino: int) -> str:
    """
    Intenta realizar un movimiento completo: valida, mueve y consume la tirada.
    Devuelve un código de estado (e.g., "OK", "MOVIMIENTO_ILEGAL").
    """
    jugador_actual = self._jugador_actual_
    
    # 1. Validar si el movimiento es legal según las reglas del tablero
    if not self._tablero_.es_movimiento_valido(jugador_actual, origen, destino):
        return "MOVIMIENTO_ILEGAL"

    # 2. Calcular la distancia del movimiento
    # La lógica de distancia es compleja debido a la barra (origen=0) y la retirada (destino=25)
    if origen == 0: # Moviendo desde la barra
        # Distancia es el punto de destino (1 a 6)
        distancia = destino
    elif destino == 25: # Retirando una ficha
        # La distancia es el punto de origen (19 a 24)
        # En Backgammon, la tirada usada es la que cubre la distancia al punto 25
        # Para simplificar, asumimos que la tirada es igual al punto de origen
        distancia = origen
    else: # Movimiento normal
        distancia = abs(destino - origen)

    # 3. Verificar si la distancia corresponde a una tirada disponible
    tiradas_disponibles = self._dados_._tiradas_disponibles_
    
    # Buscamos la tirada que coincide con la distancia
    if distancia in tiradas_disponibles:
        # 4. Mover la ficha (el Board se encarga de la lógica de captura, etc.)
        self._tablero_.mover_ficha(origen, destino)
        
        # 5. Consumir la tirada
        tiradas_disponibles.remove(distancia)
        
        # 6. Actualizar el estado del juego (verificar si se retiró una ficha)
        if destino == 25:
            jugador_actual._fichas_fuera_ += 1
            # También se debe verificar si se ha ganado
            self._verificar_ganador_() 
            
        return "OK"
    else:
        return "TIRADA_NO_DISPONIBLE"
