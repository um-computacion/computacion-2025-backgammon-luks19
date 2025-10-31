from .checker import Checker
from typing import List

class Player:
    """
    Representa a un jugador del juego.
    Gestiona su nombre, color y el estado de sus 15 fichas.
    """
    def __init__(self, nombre: str, color: str):
        """
        Inicializa un jugador con su nombre y color.
        Automáticamente crea sus 15 fichas.
        """
        self._nombre_: str = nombre
        self._color_: str = color
        
        # Crea las 15 fichas del jugador
        self._fichas_: List[Checker] = [Checker(color=self._color_) for _ in range(15)]
        
        # Listas para gestionar el estado de las fichas durante el juego
        self._fichas_capturadas_: List[Checker] = []
        self._fichas_retiradas_: List[Checker] = []

    def tiene_fichas_en_barra(self) -> bool:
        """
        Devuelve True si el jugador tiene una o más fichas en la barra (capturadas).
        """
        return len(self._fichas_capturadas_) > 0
