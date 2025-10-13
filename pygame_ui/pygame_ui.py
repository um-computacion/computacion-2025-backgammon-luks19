import pygame
from core.backgammon_game import BackgammonGame

class PygameUI:
    """
    Gestiona la interfaz gráfica del juego utilizando Pygame.
    """
    def __init__(self, ancho: int = 800, alto: int = 600):
        """
        Inicializa Pygame, la ventana y los componentes del juego.
        """
        pygame.init()

        self._ancho_ = ancho
        self._alto_ = alto
        self._pantalla_ = pygame.display.set_mode((self._ancho_, self._alto_))
        pygame.display.set_caption("Backgammon Computación 2025")

        # Creamos una instancia del motor del juego, igual que en la CLI
        self._juego_ = BackgammonGame("Jugador 1 (Negras)", "Jugador 2 (Blancas)")
