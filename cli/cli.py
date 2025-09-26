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

    def run(self):
        """
        Inicia y gestiona el bucle principal del juego.
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

            # --- Lógica de movimiento (simplificada por ahora) ---
            # En el futuro, aquí pediremos los movimientos al usuario.
            # Por ahora, solo cambiamos de turno para ver el bucle funcionar.
            input("Presiona Enter para pasar al siguiente turno...")
            
            self._juego_.cambiar_jugador()

        print("¡Juego terminado!")
        if self._juego_._ganador_:
            print(f"El ganador es: {self._juego_._ganador_._nombre_}")    