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
    
    def _dibujar_todo_(self):
        """
        Dibuja todos los elementos del juego en la pantalla.
        (Por ahora, solo pinta el fondo).
        """
        # Pintamos el fondo de un color (ej. un verde oscuro tipo fieltro)
        color_fondo = (0, 51, 0)
        self._pantalla_.fill(color_fondo)

        # --- Aquí irá el código para dibujar el tablero, fichas, etc. ---

        # Actualizamos la pantalla para mostrar los cambios
        pygame.display.flip()

    def run(self):
        """
        Inicia y gestiona el bucle principal de la interfaz gráfica.
        """
        self._juego_.iniciar_juego()
        corriendo = True

        while corriendo:
            # 1. Manejo de Eventos
            for evento in pygame.event.get():
                # Si el usuario cierra la ventana
                if evento.type == pygame.QUIT:
                    corriendo = False    

            # 2. Lógica del juego (por ahora no hay)

            # 3. Dibujar en la pantalla
            self._dibujar_todo_()

        # Cuando el bucle termina, salimos de Pygame
        pygame.quit()