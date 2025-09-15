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

    def mover_ficha(self, punto_origen: int, punto_destino: int):
        """
        Mueve la ficha superior de un punto de origen a un punto de destino.
        Asume que el movimiento ya ha sido validado.
        Si el destino es un 'blot' (una sola ficha enemiga), la captura.
        """
        if not self._puntos_[punto_origen]:
            return

        ficha_a_mover = self._puntos_[punto_origen].pop()
        color_jugador_actual = ficha_a_mover.obtener_color()

        # --- LÓGICA DE CAPTURA ---
        fichas_en_destino = self._puntos_[punto_destino]
        if (len(fichas_en_destino) == 1 and 
            fichas_en_destino[0].obtener_color() != color_jugador_actual):
            
            # Es un 'blot', capturamos la ficha enemiga
            ficha_capturada = self._puntos_[punto_destino].pop()
            self.agregar_a_barra(ficha_capturada)
        # --- FIN DE LÓGICA DE CAPTURA ---

        # Actualizamos la posición interna de nuestra ficha
        ficha_a_mover.establecer_posicion(punto_destino)
        
        # La agregamos al punto de destino
        self._puntos_[punto_destino].append(ficha_a_mover)

    def es_movimiento_valido(self, jugador: Player, punto_origen: int, punto_destino: int) -> bool:
        """
        Verifica si un movimiento es válido, incluyendo reingreso y bear-off.
        """
        color_jugador = jugador._color_

        # --- REGLA: REINGRESO OBLIGATORIO ---
        if self._barra_[color_jugador]:
            return punto_origen == 0 and 1 <= punto_destino <= 24

        # --- REGLA: BEAR OFF (SACAR FICHAS) ---
        # Usamos 0 para blancas y 25 para negras como destino "fuera"
        if (color_jugador == "blanco" and punto_destino == 0) or \
           (color_jugador == "negro" and punto_destino == 25):
            return self.puede_sacar_fichas(jugador)

        # --- VALIDACIONES ESTÁNDAR ---
        if not (1 <= punto_origen <= 24 and 1 <= punto_destino <= 24):
            return False
        
        fichas_en_origen = self._puntos_[punto_origen]
        if not fichas_en_origen or fichas_en_origen[-1].obtener_color() != color_jugador:
            return False

        if color_jugador == "blanco":
            if punto_destino >= punto_origen: return False
        else: # "negro"
            if punto_destino <= punto_origen: return False

        fichas_en_destino = self._puntos_[punto_destino]
        if len(fichas_en_destino) > 1 and fichas_en_destino[0].obtener_color() != color_jugador:
            return False

        return True
    
    def puede_sacar_fichas(self, jugador: Player) -> bool:
        """
        Verifica si el jugador tiene todas sus fichas en su home board.
        """
        color = jugador._color_
        fichas_en_juego = 0
        fichas_en_home_board = 0

        if color == "blanco":
            # Home board de las blancas: puntos 1-6
            home_board_range = range(1, 7)
        else: # "negro"
            # Home board de las negras: puntos 19-24
            home_board_range = range(19, 25)

        for i in range(1, 25):
            for ficha in self._puntos_[i]:
                if ficha.obtener_color() == color:
                    fichas_en_juego += 1
                    if i in home_board_range:
                        fichas_en_home_board += 1
        
        # Todas las fichas en juego deben estar en el home board.
        # También nos aseguramos de que no haya fichas en la barra.
        return fichas_en_juego == fichas_en_home_board and not self._barra_[color]

    def sacar_ficha(self, punto_origen: int):
        """
        Mueve una ficha desde un punto del tablero al área de fuera.
        """
        if not self._puntos_[punto_origen]:
            return
        
        ficha = self._puntos_[punto_origen].pop()
        color = ficha.obtener_color()
        self._fichas_fuera_[color].append(ficha)