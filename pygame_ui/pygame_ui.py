import pygame
from core.backgammon_game import BackgammonGame

# --- Constantes Visuales 
ANCHO, ALTO = 1000, 700
MARGEN_X, MARGEN_Y = 40, 40
COLOR_FONDO = (245, 239, 230)
COLOR_TABLERO = (230, 220, 200)
TRIANGULO_A = (170, 120, 90)
TRIANGULO_B = (210, 170, 130)
LINEA = (60, 60, 60)
FICHA_BLANCA = (245, 245, 245)
FICHA_NEGRA = (30, 30, 30)

class PygameUI:
    def __init__(self):
        pygame.init()
        self._pantalla_ = pygame.display.set_mode((ANCHO, ALTO))
        pygame.display.set_caption("Backgammon - L. Valdemoros")
        self._reloj_ = pygame.time.Clock()
        self._fuente_ = pygame.font.SysFont(None, 24)
        self._juego_ = BackgammonGame("Jugador 1", "Jugador 2")

    def _dibujar_triangulo_(self, superficie, rect_tablero, col_vis, fila, color):
        ancho_triangulo = rect_tablero.width / 12.0
        x0 = rect_tablero.left + col_vis * ancho_triangulo
        x1 = x0 + ancho_triangulo
        x_medio = (x0 + x1) / 2.0

        if fila == 'top':
            y_punta = rect_tablero.top + rect_tablero.height * 0.45
            puntos = [(x0, rect_tablero.top), (x1, rect_tablero.top), (x_medio, y_punta)]
        else: # 'bottom'
            y_punta = rect_tablero.bottom - rect_tablero.height * 0.45
            puntos = [(x0, rect_tablero.bottom), (x1, rect_tablero.bottom), (x_medio, y_punta)]
        pygame.draw.polygon(superficie, color, puntos)

    def _dibujar_ficha_(self, superficie, centro, radio, color_rgb):
        pygame.draw.circle(superficie, color_rgb, centro, radio)
        pygame.draw.circle(superficie, LINEA, centro, radio, 2) # Borde

    def _dibujar_tablero_y_fichas_(self):
        self._pantalla_.fill(COLOR_FONDO)
        rect_tablero = pygame.Rect(MARGEN_X, MARGEN_Y, ANCHO - 2 * MARGEN_X, ALTO - 2 * MARGEN_Y)
        pygame.draw.rect(self._pantalla_, COLOR_TABLERO, rect_tablero)
        
        # Dibujar los 24 triángulos
        for i in range(12):
            self._dibujar_triangulo_(self._pantalla_, rect_tablero, i, 'top', TRIANGULO_A if i % 2 == 0 else TRIANGULO_B)
            self._dibujar_triangulo_(self._pantalla_, rect_tablero, i, 'bottom', TRIANGULO_B if i % 2 == 0 else TRIANGULO_A)

        # Dibujar las fichas desde la lógica del core
        ancho_triangulo = rect_tablero.width / 12.0
        radio_ficha = int(ancho_triangulo * 0.4)

        for punto_num, fichas in self._juego_._tablero_._puntos_.items():
            if not fichas:
                continue

            color_ficha = fichas[0].obtener_color()
            color_rgb = FICHA_BLANCA if color_ficha == "blanco" else FICHA_NEGRA
            
            # Convertir punto lógico (1-24) a columna visual (0-11) y fila ('top'/'bottom')
            if 1 <= punto_num <= 12: # Fila inferior
                fila = 'bottom'
                col_vis = punto_num - 1
            else: # Fila superior (13-24)
                fila = 'top'
                col_vis = 24 - punto_num
            
            x_centro = rect_tablero.left + col_vis * ancho_triangulo + ancho_triangulo / 2

            for i, ficha in enumerate(fichas):
                if fila == 'bottom':
                    y_centro = rect_tablero.bottom - radio_ficha - (i * radio_ficha * 2)
                else: # 'top'
                    y_centro = rect_tablero.top + radio_ficha + (i * radio_ficha * 2)
                
                self._dibujar_ficha_(self._pantalla_, (x_centro, y_centro), radio_ficha, color_rgb)

    def run(self):
        self._juego_.iniciar_juego()
        corriendo = True
        while corriendo:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    corriendo = False
                if evento.type == pygame.KEYDOWN and (evento.key == pygame.K_ESCAPE or evento.key == pygame.K_q):
                    corriendo = False

            self._dibujar_tablero_y_fichas_()
            pygame.display.flip()
            self._reloj_.tick(60)
        
        pygame.quit()

