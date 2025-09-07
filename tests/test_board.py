import pytest
from core.board import Board
from core.checker import Checker

def test_creacion_tablero_vacio():
    """
    Verifica que un tablero se crea vacío pero con la estructura correcta.
    Debe tener 24 puntos, una barra y un área de fichas fuera.
    """
    tablero = Board()
    
    # Verifica que hay 24 puntos y están todos vacíos
    assert len(tablero._puntos_) == 24
    assert all(len(fichas) == 0 for fichas in tablero._puntos_.values())
    
    # Verifica que la barra y el área de fuera están vacías
    assert tablero._barra_ == {"blanco": [], "negro": []}
    assert tablero._fichas_fuera_ == {"blanco": [], "negro": []}

def test_configurar_tablero_inicial():
    """
    Verifica que el método para configurar el tablero inicial
    coloca el número correcto de fichas en las posiciones correctas.
    """
    tablero = Board()
    tablero.configurar_tablero_inicial()

    # Verificamos algunas posiciones clave según las reglas del Backgammon
    # (Puntos indexados de 1 a 24)
    
    # Fichas Negras
    assert len(tablero._puntos_[1]) == 2
    assert tablero._puntos_[1][0].obtener_color() == "negro"
    assert len(tablero._puntos_[12]) == 5
    assert tablero._puntos_[12][0].obtener_color() == "negro"
    assert len(tablero._puntos_[17]) == 3
    assert tablero._puntos_[17][0].obtener_color() == "negro"
    assert len(tablero._puntos_[19]) == 5
    assert tablero._puntos_[19][0].obtener_color() == "negro"

    # Fichas Blancas (lado opuesto)
    assert len(tablero._puntos_[24]) == 2
    assert tablero._puntos_[24][0].obtener_color() == "blanco"
    assert len(tablero._puntos_[13]) == 5
    assert tablero._puntos_[13][0].obtener_color() == "blanco"
    assert len(tablero._puntos_[8]) == 3
    assert tablero._puntos_[8][0].obtener_color() == "blanco"
    assert len(tablero._puntos_[6]) == 5
    assert tablero._puntos_[6][0].obtener_color() == "blanco"

    # Verificamos un punto que debe estar vacío
    assert len(tablero._puntos_[2]) == 0

def test_agregar_ficha_a_punto():
    """
    Verifica que se puede agregar una ficha a un punto específico.
    """
    tablero = Board()
    ficha = Checker(color="blanco")
    tablero.agregar_ficha(ficha, 10)
    
    assert len(tablero._puntos_[10]) == 1
    assert tablero._puntos_[10][0] == ficha

def test_agregar_ficha_a_barra():
    """
    Verifica que se puede agregar una ficha a la barra de su color.
    """
    tablero = Board()
    ficha = Checker(color="negro")
    tablero.agregar_a_barra(ficha)

    assert len(tablero._barra_["negro"]) == 1
    assert tablero._barra_["negro"][0] == ficha
    assert len(tablero._barra_["blanco"]) == 0
