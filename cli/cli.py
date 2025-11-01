from core.backgammon_game import BackgammonGame

class CLI:
    """
    Gestiona la interacción con el usuario a través de la línea de comandos.
    """
    def __init__(self):
        self._juego_ = BackgammonGame("Jugador 1 (Negras)", "Jugador 2 (Blancas)")
    
    def _dibujar_tablero_(self):
        """
        Dibuja una representación textual simple del estado actual del tablero.
        """
        tablero = self._juego_._tablero_
        print("\n" + "="*40)

        # Puntos 12 a 1
        linea_superior = ""
        for i in range(12, 0, -1):
            fichas = tablero._puntos_.get(i, [])
            char = f"{len(fichas)}{fichas[0].obtener_color()[0].upper()}" if fichas else "·"
            linea_superior += f" {char:<3}"
        print(f" 12 a 1: {linea_superior}")

        # Puntos 13 a 24
        linea_inferior = ""
        for i in range(13, 25):
            fichas = tablero._puntos_.get(i, [])
            char = f"{len(fichas)}{fichas[0].obtener_color()[0].upper()}" if fichas else "·"
            linea_inferior += f" {char:<3}"
        print(f" 13 a 24: {linea_inferior}")

        # Información de la barra y fuera
        barra_negras = len(tablero._barra_["negro"])
        barra_blancas = len(tablero._barra_["blanco"])
        fuera_negras = tablero.obtener_cantidad_fichas_fuera("negro")
        fuera_blancas = tablero.obtener_cantidad_fichas_fuera("blanco")
        
        print(f"Barra: Negras[{barra_negras}] | Blancas[{barra_blancas}]")
        print(f"Fuera: Negras[{fuera_negras}] | Blancas[{fuera_blancas}]")
        print("="*40)

    def _obtener_movimiento_del_usuario(self):
        try:
            origen_str = input("Mover desde el punto (o 'salir'): ")
            if origen_str.lower() == 'salir':
                return None

            if origen_str.lower() == 'barra':
                origen = 0
            else:
                origen = int(origen_str)

            destino_str = input("Mover al punto: ")
            if destino_str.lower() == 'fuera':
                destino = 25 
            else:
                destino = int(destino_str)

            return origen, destino
        except ValueError:
            print("Error: Por favor, introduce números válidos para los puntos.")
            return None  

    def run(self):
        """
        Inicia y gestiona el bucle principal del juego con interacción del usuario.
        """
        print("¡Bienvenido a Backgammon!")
        self._juego_.iniciar_juego()

        while not self._juego_._juego_terminado_:
            self._dibujar_tablero_()
            
            jugador_actual = self._juego_._jugador_actual_
            print(f"\nTurno de: {jugador_actual._nombre_}")

            # Tirar los dados
            self._juego_._dados_.lanzar()
            tiradas = self._juego_._dados_._tiradas_disponibles_
            print(f"Tiradas disponibles: {tiradas}")    

            # Bucle para los movimientos del turno actual
            while self._juego_._dados_._tiradas_disponibles_:
                movimiento = self._obtener_movimiento_del_usuario()
                
                if movimiento is None:
                    print("Pasando de turno...")
                    break 

                origen, destino = movimiento

                resultado = self._juego_.realizar_movimiento(origen, destino)
                
                if resultado == "OK":
                    print(f"Movimiento exitoso de {origen} a {destino}.")
                    self._dibujar_tablero_()
                    print(f"Tiradas restantes: {self._juego_._dados_._tiradas_disponibles_}")
                elif resultado == "MOVIMIENTO_ILEGAL":
                    print("Error: Movimiento inválido según las reglas del juego.")
                elif resultado == "TIRADA_NO_DISPONIBLE":
                    print(f"Error: La distancia del movimiento no corresponde a ninguna tirada disponible: {self._juego_._dados_._tiradas_disponibles_}.")
                elif resultado == "FICHA_NO_PERTENECE":
                    print("Error: No puedes mover una ficha que no es tuya.")
                else:
                    print(f"Error desconocido: {resultado}")

            # Verificar ganador antes de cambiar de jugador
            self._juego_._verificar_ganador_()
            
            if not self._juego_._juego_terminado_:
                self._juego_.cambiar_jugador()

        print("¡Juego terminado!")
        if self._juego_._ganador_:
            print(f"El ganador es: {self._juego_._ganador_._nombre_}") 