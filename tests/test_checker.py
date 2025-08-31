import pytest
from core.checker import Checker

# Test para la creación e inicialización de la Ficha
def test_creacion_checker():
    """
    Verifica que una instancia de Checker se crea correctamente
    con los atributos _color_ y _posicion_ en español.
    """
    ficha = Checker(color="blanco", posicion_inicial=1)
    assert ficha._color_ == "blanco"
    assert ficha._posicion_ == 1

def test_creacion_checker_sin_posicion():
    """
    Verifica que la posición inicial puede ser None si no se especifica.
    """
    ficha = Checker(color="negro")
    assert ficha._color_ == "negro"
    assert ficha._posicion_ is None

# Test para el método obtener_color
def test_obtener_color():
    """
    Verifica que el método obtener_color() devuelve el color correcto.
    """
    ficha = Checker(color="blanco", posicion_inicial=1)
    assert ficha.obtener_color() == "blanco"

# Test para el método obtener_posicion
def test_obtener_posicion():
    """
    Verifica que el método obtener_posicion() devuelve la posición correcta.
    """
    ficha = Checker(color="negro", posicion_inicial=12)
    assert ficha.obtener_posicion() == 12

# Test para el método establecer_posicion
def test_establecer_posicion():
    """
    Verifica que el método establecer_posicion() actualiza el atributo _posicion_.
    """
    ficha = Checker(color="blanco", posicion_inicial=1)
    ficha.establecer_posicion(5)
    assert ficha._posicion_ == 5
    assert ficha.obtener_posicion() == 5
