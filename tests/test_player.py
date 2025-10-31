import pytest
from core.player import Player
from core.checker import Checker

def test_creacion_player():
    """
    Verifica que un Player se crea con su nombre, color y 15 fichas.
    """
    jugador = Player(nombre="Lucas", color="blanco")

    assert jugador._nombre_ == "Lucas"
    assert jugador._color_ == "blanco"
    
    # Verificamos que se crearon exactamente 15 fichas
    assert len(jugador._fichas_) == 15
    
    # Verificamos que todas las fichas creadas son del color correcto
    assert all(ficha.obtener_color() == "blanco" for ficha in jugador._fichas_)
    
    # Verificamos que las otras listas están vacías al inicio
    assert jugador._fichas_capturadas_ == []
    assert jugador._fichas_retiradas_ == []

def test_tiene_fichas_en_barra_vacia():
    """
    Verifica que el método devuelve False cuando no hay fichas en la barra.
    """
    jugador = Player(nombre="Ana", color="negro")
    assert jugador.tiene_fichas_en_barra() is False

def test_tiene_fichas_en_barra_con_fichas():
    """
    Verifica que el método devuelve True cuando hay una o más fichas en la barra.
    """
    jugador = Player(nombre="Ana", color="negro")
    
    # Simulamos una captura moviendo una ficha a la lista de capturadas
    # NOTA: Accedemos a atributos "privados" para preparar el estado del test.
    ficha_capturada = jugador._fichas_.pop()
    jugador._fichas_capturadas_.append(ficha_capturada)
    
    assert jugador.tiene_fichas_en_barra() is True
