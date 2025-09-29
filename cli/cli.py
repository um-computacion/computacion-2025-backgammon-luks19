from core.backgammon_game import BackgammonGame

class CLI:
    """
    Gestiona la interacción con el usuario a través de la línea de comandos.
    """
    def __init__(self):
        """
        Inicializa la CLI creando una instancia del juego.
        """
        # Por ahora, los nombres de los jugadores están fijos.
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
            char = f"{len(fichas)}{fichas[0].obtener_color()[0]}" if fichas else "·"
            linea_superior += f" {char:<3}"
        print(f" 12 a 1: {linea_superior}")

        # Puntos 13 a 24
        linea_inferior = ""
        for i in range(13, 25):
            fichas = tablero._puntos_.get(i, [])
            char = f"{len(fichas)}{fichas[0].obtener_color()[0]}" if fichas else "·"
            linea_inferior += f" {char:<3}"
        print(f" 13 a 24: {linea_inferior}")

        # Imprimir información de la barra
        barra_negras = len(tablero._barra_["negro"])
        barra_blancas = len(tablero._barra_["blanco"])
        print(f"Barra: Negras[{barra_negras}] | Blancas[{barra_blancas}]")
        print("="*40)

    def _obtener_movimiento_del_usuario(self) -> tuple[int, int] | None:
        """
        Pide al usuario el origen y el destino del movimiento.
        Devuelve una tupla (origen, destino) o None si el usuario quiere salir.
        """
        try:
            origen_str = input("Mover desde el punto (o 'salir'): ")
            if origen_str.lower() == 'salir':
                return None

            # Permitimos 'barra' como origen
            if origen_str.lower() == 'barra':
                origen = 0
            else:
                origen = int(origen_str)

            destino_str = input("Mover al punto: ")
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
            while tiradas:
                movimiento = self._obtener_movimiento_del_usuario()
                if movimiento is None: # El usuario escribió 'salir' o hubo un error
                    # Por ahora, simplemente pasamos de turno en caso de error/salida
                    print("Pasando de turno...")
                    break 

                origen, destino = movimiento

                # --- Conexión con el CORE ---
                # 1. Validar si el movimiento es legal
                if self._juego_._tablero_.es_movimiento_valido(jugador_actual, origen, destino):
                    # 2. Calcular la distancia del movimiento
                    distancia = abs(destino - origen)
                    
                    # 3. Verificar si la distancia corresponde a una tirada disponible
                    if distancia in tiradas:
                        print(f"Movimiento válido. Moviendo de {origen} a {destino}.")
                        self._juego_._tablero_.mover_ficha(origen, destino)
                        
                        # 4. Usar la tirada
                        tiradas.remove(distancia)
                        self._dibujar_tablero_() # Volver a dibujar para ver el cambio
                        print(f"Tiradas restantes: {tiradas}")
                    else:
                        print(f"Error: La distancia del movimiento ({distancia}) no corresponde a ninguna tirada disponible {tiradas}.")
                else:
                    print("Error: Movimiento inválido según las reglas del juego.")