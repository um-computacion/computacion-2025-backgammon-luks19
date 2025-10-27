import pygame

class CheckerRenderer:
    """
    Se encarga de cargar y dibujar las fichas (checkers).
    """
    def __init__(self, ruta_ficha_negra: str, ruta_ficha_blanca: str, tamaño_ficha: int):
        """
        Inicializa el renderer cargando las imágenes de las fichas.
        """
        self._tamaño_ficha_ = tamaño_ficha
        try:
            # Cargamos las imágenes de las fichas
            img_negra = pygame.image.load(ruta_ficha_negra)
            img_blanca = pygame.image.load(ruta_ficha_blanca)

            # Las escalamos al tamaño deseado para que encajen en el tablero
            self._imagen_ficha_negra_ = pygame.transform.scale(img_negra, (tamaño_ficha, tamaño_ficha))
            self._imagen_ficha_blanca_ = pygame.transform.scale(img_blanca, (tamaño_ficha, tamaño_ficha))
        
        except pygame.error as e:
            print(f"Error al cargar las imágenes de las fichas: {e}")
            self._imagen_ficha_negra_ = pygame.Surface((0, 0))
            self._imagen_ficha_blanca_ = pygame.Surface((0, 0))

    def dibujar(self, pantalla: pygame.Surface, color: str, x: int, y: int):
        """
        Dibuja una ficha de un color específico en las coordenadas (x, y) de la pantalla.
        """
        if color == "negro":
            imagen = self._imagen_ficha_negra_
        else:
            imagen = self._imagen_ficha_blanca_
        
        if imagen.get_width() > 0:
            # Creamos un rectángulo para la ficha y lo centramos en (x, y)
            rect = imagen.get_rect(center=(x, y))
            pantalla.blit(imagen, rect)
