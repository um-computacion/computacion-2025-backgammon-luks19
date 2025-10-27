import pygame

class BoardRenderer:
    """
    Se encarga de cargar y dibujar el tablero de Backgammon.
    """
    def __init__(self, ruta_imagen_tablero: str):
        """
        Inicializa el renderer cargando la imagen del tablero.
        """
        try:
            # Cargamos la imagen del tablero desde la ruta proporcionada
            self._imagen_tablero_ = pygame.image.load(ruta_imagen_tablero)
        except pygame.error as e:
            print(f"Error al cargar la imagen del tablero: {e}")
            # Si la imagen no se puede cargar, creamos una superficie vacía para evitar que el programa se caiga
            self._imagen_tablero_ = pygame.Surface((0, 0))

    def dibujar(self, pantalla: pygame.Surface):
        """
        Dibuja el tablero en la superficie de la pantalla proporcionada.
        """
        if self._imagen_tablero_.get_width() > 0:
            # Obtenemos el rectángulo de la pantalla para centrar el tablero
            rect_pantalla = pantalla.get_rect()
            rect_tablero = self._imagen_tablero_.get_rect(center=rect_pantalla.center)
            
            # Dibujamos la imagen del tablero en la pantalla, centrada
            pantalla.blit(self._imagen_tablero_, rect_tablero)