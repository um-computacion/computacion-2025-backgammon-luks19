import pygame
from core.backgammon_game import BackgammonGame
from .board_renderer import BoardRenderer

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

        # Asumimos que la imagen se llama 'board.png' y está en 'assets/'
        self._board_renderer_ = BoardRenderer("assets/board.png")
    

    def _dibujar_todo_(self):
        """
        Dibuja todos los elementos del juego en la pantalla usando la configuración.
        """
        color_fondo = (0, 51, 0)
        self._pantalla_.fill(color_fondo)
        self._board_renderer_.dibujar(self._pantalla_)

        # --- LÓGICA PARA DIBUJAR LAS FICHAS ---
        tablero_logico = self._juego_._tablero_
        for punto_num, fichas in tablero_logico._puntos_.items():
            if not fichas:
                continue
            
            # Obtenemos las coordenadas base desde tu config
            x, y_base = config.COORDENADAS_PUNTOS[punto_num]
            color_ficha = fichas[0].obtener_color()
            
            # Apilamos las fichas
            for i, ficha in enumerate(fichas):
                # Corrección de la dirección de apilamiento
                if y_base > config.ALTO_VENTANA / 2: # Fila inferior
                    # Apilamos hacia ARRIBA (restando y)
                    y = y_base - (i * config.ESPACIADO_FICHAS)
                else: # Fila superior
                    # Apilamos hacia ABAJO (sumando y)
                    y = y_base + (i * config.ESPACIADO_FICHAS)
                
                self._checker_renderer_.dibujar(self._pantalla_, color_ficha, x, y)
        
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