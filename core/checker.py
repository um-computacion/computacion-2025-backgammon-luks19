import pytest
from core.checker import Checker

# Test para la creación e inicialización de la Ficha
def test_creacion_checker():
    """
    Verifica que una instancia de Checker se crea correctamente
    con el atributo _color_ y sin el atributo _posicion_.
    """
    ficha = Checker(color="blanco")
    assert ficha._color_ == "blanco"
    # Se verifica que el atributo de posición no existe, o que la inicialización
    # no requiere ni acepta un argumento de posición.
    with pytest.raises(AttributeError):
        _ = ficha._posicion_

# Test para el método obtener_color
def test_obtener_color():
    """
    Verifica que el método obtener_color() devuelve el color correcto.
    """
    ficha = Checker(color="negro")
    assert ficha.obtener_color() == "negro"
