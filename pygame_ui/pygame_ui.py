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
                if evento.type == pygame.QUIT:
                    corriendo = False
                
                # --- NUEVA LÓGICA: DETECCIÓN DE CLIC ---
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    # Verificamos que fue el clic izquierdo del ratón
                    if evento.button == 1:
                        pos_clic = pygame.mouse.get_pos()
                        punto_clickeado = self._obtener_punto_desde_coordenadas(pos_clic)
                        
                        if punto_clickeado is not None:
                            print(f"Se hizo clic en el punto: {punto_clickeado}")
                        else:
                            print("Se hizo clic fuera de cualquier punto.")

            # 2. Lógica del juego (aún no hay)

            # 3. Dibujar en la pantalla
            self._dibujar_todo_()

        pygame.quit()

    def _obtener_punto_desde_coordenadas(self, pos: tuple[int, int]) -> int | None:
        """
        Toma una tupla de coordenadas (x, y) del ratón y devuelve el número
        del punto del tablero que fue clickeado, o None si no se hizo clic en ningún punto.
        """
        x_clic, y_clic = pos

        for punto_num, (x_punto, y_base_punto) in config.COORDENADAS_PUNTOS.items():
            # Creamos un rectángulo "sensible" para cada punto del tablero.
            # El ancho es el tamaño de la ficha, y el alto es la mitad del tablero.
            ancho_colision = config.TAMANO_FICHA
            alto_colision = config.ALTO_TABLERO / 2

            if y_base_punto > config.ALTO_VENTANA / 2: # Puntos de la fila inferior
                # El rectángulo empieza en la parte superior del tablero y va hacia abajo
                rect_punto = pygame.Rect(
                    x_punto - ancho_colision / 2, 
                    config.OFFSET_Y + alto_colision, 
                    ancho_colision, 
                    alto_colision
                )
            else: # Puntos de la fila superior
                # El rectángulo empieza en el borde y va hacia el centro
                rect_punto = pygame.Rect(
                    x_punto - ancho_colision / 2, 
                    config.OFFSET_Y, 
                    ancho_colision, 
                    alto_colision
                )

            # Verificamos si el clic ocurrió dentro de este rectángulo
            if rect_punto.collidepoint(x_clic, y_clic):
                return punto_num
        
        # Si el bucle termina y no se encontró ningún punto
        return None