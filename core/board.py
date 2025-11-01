from .checker import Checker
from .player import Player

class Board:
    """
    Representa el tablero de Backgammon.
    Gestiona la posición de las fichas en los 24 puntos, la barra y el área de fuera.
    """
    def __init__(self):
        """
        Inicializa el tablero con 24 puntos vacíos, una barra y un área de fichas fuera.
        """
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
        self._puntos_ = {i: [] for i in range(1, 25)}
        self._barra_ = {"blanco": [], "negro": []}
        self._fichas_fuera_ = {"blanco": [], "negro": []}

        # Colocación de fichas negras
        for _ in range(2): self.agregar_ficha(Checker(color="negro"), 1)
        for _ in range(5): self.agregar_ficha(Checker(color="negro"), 12)
        for _ in range(3): self.agregar_ficha(Checker(color="negro"), 17)
        for _ in range(5): self.agregar_ficha(Checker(color="negro"), 19)

        # Colocación de fichas blancas
        for _ in range(2): self.agregar_ficha(Checker(color="blanco"), 24)
        for _ in range(5): self.agregar_ficha(Checker(color="blanco"), 13)
        for _ in range(3): self.agregar_ficha(Checker(color="blanco"), 8)
        for _ in range(5): self.agregar_ficha(Checker(color="blanco"), 6)

    def agregar_ficha(self, ficha: Checker, punto: int):
        """
        Agrega UNA ficha a un punto específico del tablero.
        """
        if punto not in self._puntos_:
            return
        
        self._puntos_[punto].append(ficha)

    def agregar_a_barra(self, ficha: Checker):
        """
        Agrega una ficha capturada a la barra, en la sección de su color.
        """
        color = ficha.obtener_color()
        self._barra_[color].append(ficha)

    def mover_ficha(self, punto_origen: int, punto_destino: int):
        """
        Mueve la ficha superior de un punto de origen a un punto de destino.
        Si el destino es un 'blot' (una sola ficha enemiga), la captura.
        """
        # Caso especial: mover desde la barra (origen=0)
        if punto_origen == 0:
            # Determinamos el color buscando en ambas barras
            if self._barra_["negro"]:
                ficha_a_mover = self._barra_["negro"].pop()
            elif self._barra_["blanco"]:
                ficha_a_mover = self._barra_["blanco"].pop()
            else:
                return
        else:
            # Movimiento normal desde un punto
            if not self._puntos_[punto_origen]:
                return
            ficha_a_mover = self._puntos_[punto_origen].pop()

        color_jugador_actual = ficha_a_mover.obtener_color()

        # LÓGICA DE CAPTURA
        fichas_en_destino = self._puntos_[punto_destino]
        if (len(fichas_en_destino) == 1 and 
            fichas_en_destino[0].obtener_color() != color_jugador_actual):
            
            ficha_capturada = self._puntos_[punto_destino].pop()
            self.agregar_a_barra(ficha_capturada)

        self._puntos_[punto_destino].append(ficha_a_mover)

    def es_movimiento_valido(self, jugador: Player, punto_origen: int, punto_destino: int) -> bool:
        """
        Verifica si un movimiento es válido, incluyendo reingreso y bear-off.
        """
        color_jugador = jugador._color_

        # REGLA: REINGRESO OBLIGATORIO
        if self._barra_[color_jugador]:
            return punto_origen == 0 and 1 <= punto_destino <= 24

        # REGLA: BEAR OFF (SACAR FICHAS)
        if (color_jugador == "blanco" and punto_destino == 0) or \
           (color_jugador == "negro" and punto_destino == 25):
            return self.puede_sacar_fichas(jugador)

        # VALIDACIONES ESTÁNDAR
        if not (1 <= punto_origen <= 24 and 1 <= punto_destino <= 24):
            return False
        
        fichas_en_origen = self._puntos_[punto_origen]
        if not fichas_en_origen or fichas_en_origen[-1].obtener_color() != color_jugador:
            return False

        if color_jugador == "blanco":
            if punto_destino >= punto_origen: return False
        else:
            if punto_destino <= punto_origen: return False

        fichas_en_destino = self._puntos_[punto_destino]
        if len(fichas_en_destino) > 1 and fichas_en_destino[0].obtener_color() != color_jugador:
            return False

        return True
    
    def puede_sacar_fichas(self, jugador: Player) -> bool:
        """
        Verifica si un jugador puede sacar fichas del tablero.
        """
        color = jugador._color_
        if self._barra_[color]:
            return False

        if color == "blanco":
            rango_fuera_de_casa = range(7, 25)
        else:
            rango_fuera_de_casa = range(1, 19)

        for i in rango_fuera_de_casa:
            for ficha in self._puntos_[i]:
                if ficha.obtener_color() == color:
                    return False
    
        return True

    def sacar_ficha(self, punto_origen: int):
        """
        Mueve una ficha desde un punto del tablero al área de fuera.
        """
        if not self._puntos_[punto_origen]:
            return
        
        ficha = self._puntos_[punto_origen].pop()
        color = ficha.obtener_color()
        self._fichas_fuera_[color].append(ficha)

    def obtener_cantidad_fichas_fuera(self, color: str) -> int:
        """
        Devuelve cuántas fichas de un color han sido retiradas del tablero.
        """
        if color in self._fichas_fuera_:
            return len(self._fichas_fuera_[color])
        return 0