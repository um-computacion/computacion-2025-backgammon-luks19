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
        Coloca las 30 fichas en sus posiciones de inicio según las reglas estándar,
        utilizando el método simplificado agregar_ficha.
        """
        # Limpiamos el tablero por si acaso
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
        Actualiza la posición interna de la ficha.
        """
        # Validamos que el punto sea correcto para evitar errores
        if punto not in self._puntos_:
            return  # O lanzar un error, pero por ahora es suficiente con no hacer nada

        ficha.establecer_posicion(punto)
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
        color = jugador._color_
        if self._barra_[color]: # Si hay fichas en la barra, no puede sacar
            return False

        if color == "blanco":
        # Para las blancas, revisar puntos 7 a 24
           rango_fuera_de_casa = range(7, 25)
        else: # "negro"
        # Para las negras, revisar puntos 1 a 18
           rango_fuera_de_casa = range(1, 19)

        # Si encuentra UNA SOLA ficha de su color fuera del home board, no puede sacar.
        for i in rango_fuera_de_casa:
            for ficha in self._puntos_[i]:
                if ficha.obtener_color() == color:
                   return False # Encontramos una ficha fuera de lugar
    
        return True # Si el bucle termina, todas las fichas están en casa

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
        Devuelve cuántas fichas de un color específico han sido retiradas del tablero.
        """
        if color in self._fichas_fuera_:
            return len(self._fichas_fuera_[color])
        return 0