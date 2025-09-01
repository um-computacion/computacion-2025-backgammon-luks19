class Checker:
    """
    Representa una única ficha de Backgammon (Checker).
    Almacena su color y su posición actual en el tablero.
    """
    def __init__(self, color: str, posicion_inicial: int = None):
        """
        Inicializa una ficha con un color y una posición opcional.
        Los atributos y métodos siguen la convención de nombres en español.
        """
        self._color_ = color
        self._posicion_ = posicion_inicial

    def obtener_color(self) -> str:
        """
        Devuelve el color de la ficha.
        """
        return self._color_

    def obtener_posicion(self) -> int:
        """
        Devuelve la posición actual de la ficha.
        """
        return self._posicion_

    def establecer_posicion(self, nueva_posicion: int):
        """
        Actualiza la posición de la ficha.
        """
        self._posicion_ = nueva_posicion
