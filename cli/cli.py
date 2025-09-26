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