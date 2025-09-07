from .checker import Checker

class Board:
    """
    Representa el tablero de Backgammon.
    Gestiona la posición de las fichas en los 24 puntos, la barra y el área de fuera.
    """
    def __init__(self):
        """
        Inicializa el tablero con 24 puntos vacíos, una barra y un área de fichas fuera.
        """
        # Usamos un diccionario para los puntos, con claves de 1 a 24
        self._puntos_ = {i: [] for i in range(1, 25)}
        
        self._barra_ = {
            "blanco": [],
            "negro": []
        }
        self._fichas_fuera_ = {
            "blanco": [],
            "negro": []
        }

    def configurar_tablero_inicial(self):
        """
        Coloca las 30 fichas en sus posiciones de inicio según las reglas estándar.
        """
        # Limpiamos el tablero por si acaso
        self.__init__()

        # Colocación de fichas negras
        self.agregar_ficha(Checker(color="negro"), 1, cantidad=2)
        self.agregar_ficha(Checker(color="negro"), 12, cantidad=5)
        self.agregar_ficha(Checker(color="negro"), 17, cantidad=3)
        self.agregar_ficha(Checker(color="negro"), 19, cantidad=5)

        # Colocación de fichas blancas
        self.agregar_ficha(Checker(color="blanco"), 24, cantidad=2)
        self.agregar_ficha(Checker(color="blanco"), 13, cantidad=5)
        self.agregar_ficha(Checker(color="blanco"), 8, cantidad=3)
        self.agregar_ficha(Checker(color="blanco"), 6, cantidad=5)

    def agregar_ficha(self, ficha: Checker, punto: int, cantidad: int = 1):
        """
        Agrega una o más fichas de un tipo a un punto específico.
        """
        if cantidad == 1:
            # Para una sola ficha, usamos la ficha pasada como parámetro
            ficha.establecer_posicion(punto)
            self._puntos_[punto].append(ficha)
        else:
            # Para múltiples fichas, creamos nuevas instancias
            for _ in range(cantidad):
                nueva_ficha = Checker(color=ficha.obtener_color(), posicion_inicial=punto)
                self._puntos_[punto].append(nueva_ficha)

    def agregar_a_barra(self, ficha: Checker):
        """
        Agrega una ficha capturada a la barra, en la sección de su color.
        """
        color = ficha.obtener_color()
        self._barra_[color].append(ficha)