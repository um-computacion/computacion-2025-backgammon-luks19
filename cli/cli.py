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
