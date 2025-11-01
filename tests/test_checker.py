class Checker:
    """
    Representa una única ficha de Backgammon (Checker).
    Solo almacena su color. La posición es gestionada por la clase Board.
    """
    def __init__(self, color: str):
        """
        Inicializa una ficha con un color.
        """
        self._color_ = color

    def obtener_color(self) -> str:
        """
        Devuelve el color de la ficha.
        """
        return self._color_
