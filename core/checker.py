class Checker:
    """
    Representa una ficha individual en el tablero de Backgammon.
    Cada ficha tiene un color (blanco o negro).
    """
    def __init__(self, color: str):
        """
        Inicializa una ficha con un color específico.
        """
        self._color_ = color

    def obtener_color(self):
        """
        Devuelve el color de la ficha.
        """
        return self._color_