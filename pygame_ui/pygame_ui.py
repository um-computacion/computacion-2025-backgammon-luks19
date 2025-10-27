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

        # --- NUEVA VARIABLE DE ESTADO PARA LA UI ---
        # Guarda el punto de origen del primer clic del jugador
        self._punto_origen_seleccionado_ = None
    

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
        Inicia y gestiona el bucle principal del juego con selección y movimiento.
        """
        self._juego_.iniciar_juego()
        corriendo = True

        while corriendo:
            jugador_actual = self._juego_._jugador_actual_
            
            # 1. Manejo de Eventos
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    corriendo = False
                
                if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                    pos_clic = pygame.mouse.get_pos()
                    punto_clickeado = self._obtener_punto_desde_coordenadas(pos_clic)

                    if punto_clickeado is not None:
                        # --- LÓGICA DE SELECCIÓN Y MOVIMIENTO ---
                        
                        if self._punto_origen_seleccionado_ is None:
                            # PRIMER CLIC: El jugador selecciona una ficha de origen.
                            print(f"Primer clic: Origen seleccionado en el punto {punto_clickeado}.")
                            # Aquí podríamos añadir lógica para verificar si hay fichas del jugador
                            self._punto_origen_seleccionado_ = punto_clickeado
                        
                        else:
                            # SEGUNDO CLIC: El jugador selecciona un destino.
                            punto_destino = punto_clickeado
                            print(f"Segundo clic: Destino seleccionado en el punto {punto_destino}.")
                            
                            # --- Conexión con el CORE ---
                            origen = self._punto_origen_seleccionado_
                            
                            if self._juego_._tablero_.es_movimiento_valido(jugador_actual, origen, punto_destino):
                                # Aquí faltaría la lógica para validar contra los dados.
                                # Por ahora, si es válido según el tablero, lo movemos.
                                print(f"Movimiento válido. Moviendo de {origen} a {punto_destino}.")
                                self._juego_._tablero_.mover_ficha(origen, punto_destino)
                            else:
                                print("Movimiento inválido según las reglas del tablero.")
                            
                            # Reiniciamos la selección para el próximo movimiento
                            self._punto_origen_seleccionado_ = None

            # 2. Lógica del juego (por ahora, no cambia de turno automáticamente)

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