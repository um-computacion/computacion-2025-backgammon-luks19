import pytest
from core.board import Board
from core.checker import Checker
from core.player import Player 

def test_creacion_tablero_vacio():
    """
    Verifica que un tablero se crea vacío pero con la estructura correcta.
    """
    tablero = Board()
    
    assert len(tablero._puntos_) == 24
    assert all(len(fichas) == 0 for fichas in tablero._puntos_.values())
    assert tablero._barra_ == {"blanco": [], "negro": []}
    assert tablero._fichas_fuera_ == {"blanco": [], "negro": []}

def test_configurar_tablero_inicial():
    """
    Verifica que el método para configurar el tablero inicial
    coloca el número correcto de fichas en las posiciones correctas.
    """
    tablero = Board()
    tablero.configurar_tablero_inicial()

    # Fichas Negras
    assert len(tablero._puntos_[1]) == 2
    assert tablero._puntos_[1][0].obtener_color() == "negro"
    assert len(tablero._puntos_[12]) == 5
    assert len(tablero._puntos_[17]) == 3
    assert len(tablero._puntos_[19]) == 5

    # Fichas Blancas
    assert len(tablero._puntos_[24]) == 2
    assert tablero._puntos_[24][0].obtener_color() == "blanco"
    assert len(tablero._puntos_[13]) == 5
    assert len(tablero._puntos_[8]) == 3
    assert len(tablero._puntos_[6]) == 5

    # Punto vacío
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

def test_mover_ficha_simple():
    """
    Verifica que una ficha se puede mover de un punto a otro vacío.
    """
    tablero = Board()
    ficha_a_mover = Checker(color="blanco")
    tablero.agregar_ficha(ficha_a_mover, 1)
    
    tablero.mover_ficha(1, 4)
    
    assert len(tablero._puntos_[1]) == 0
    assert len(tablero._puntos_[4]) == 1
    assert tablero._puntos_[4][0].obtener_color() == "blanco"

def test_es_movimiento_valido_simple_negras():
    """
    Verifica la validación de un movimiento simple y legal para las negras.
    """
    tablero = Board()
    jugador_negro = Player(nombre="Test", color="negro")
    
    tablero.agregar_ficha(Checker(color="negro"), 1)
    
    es_valido = tablero.es_movimiento_valido(jugador_negro, 1, 4)
    assert es_valido is True

def test_es_movimiento_valido_bloqueado():
    """
    Verifica que un movimiento a un punto bloqueado por el oponente no es válido.
    """
    tablero = Board()
    jugador_negro = Player(nombre="Test", color="negro")
    
    tablero.agregar_ficha(Checker(color="negro"), 1)
    
    # Bloqueamos el punto 4 con dos fichas blancas (usando un bucle)
    for _ in range(2):
        tablero.agregar_ficha(Checker(color="blanco"), 4)
    
    es_valido = tablero.es_movimiento_valido(jugador_negro, 1, 4)
    assert es_valido is False

def test_es_movimiento_valido_direccion_incorrecta_blancas():
    """
    Verifica que un jugador de blancas no puede mover sus fichas hacia adelante.
    """
    tablero = Board()
    jugador_blanco = Player(nombre="Test", color="blanco")
    
    tablero.agregar_ficha(Checker(color="blanco"), 5)
    
    es_valido = tablero.es_movimiento_valido(jugador_blanco, 5, 7)
    assert es_valido is False

def test_mover_ficha_con_captura():
    """
    Verifica que al mover a un blot, la ficha enemiga es capturada.
    """
    tablero = Board()
    
    tablero.agregar_ficha(Checker(color="negro"), 1)
    ficha_a_capturar = Checker(color="blanco")
    tablero.agregar_ficha(ficha_a_capturar, 4)

    tablero.mover_ficha(1, 4)

    assert len(tablero._puntos_[1]) == 0
    assert len(tablero._puntos_[4]) == 1
    assert tablero._puntos_[4][0].obtener_color() == "negro"
    assert len(tablero._barra_["blanco"]) == 1
    assert tablero._barra_["blanco"][0] == ficha_a_capturar
    assert len(tablero._barra_["negro"]) == 0

def test_movimiento_invalido_si_hay_fichas_en_la_barra():
    """
    Verifica que un jugador con fichas en la barra no puede mover otras fichas.
    """
    tablero = Board()
    jugador_negro = Player(nombre="Negro", color="negro")

    tablero.agregar_a_barra(Checker(color="negro"))
    tablero.agregar_ficha(Checker(color="negro"), 10)

    es_valido = tablero.es_movimiento_valido(jugador_negro, 10, 12)
    assert es_valido is False

def test_reingreso_desde_la_barra_es_valido():
    """
    Verifica que un movimiento para reingresar desde la barra es válido.
    """
    tablero = Board()
    jugador_negro = Player(nombre="Negro", color="negro")

    tablero.agregar_a_barra(Checker(color="negro"))

    es_valido = tablero.es_movimiento_valido(jugador_negro, 0, 3)
    assert es_valido is True

def test_puede_sacar_fichas_false():
    """
    Verifica que un jugador no puede sacar fichas si tiene fichas fuera de su home board.
    """
    tablero = Board()
    jugador_blanco = Player(nombre="Blanco", color="blanco")
    
    # Colocamos 14 fichas en el home board (usando un bucle)
    for _ in range(14):
        tablero.agregar_ficha(Checker(color="blanco"), 1)
    # Dejamos una ficha fuera, en el punto 7
    tablero.agregar_ficha(Checker(color="blanco"), 7)
    
    assert tablero.puede_sacar_fichas(jugador_blanco) is False

def test_puede_sacar_fichas_true():
    """
    Verifica que un jugador puede sacar fichas si todas están en su home board.
    """
    tablero = Board()
    jugador_blanco = Player(nombre="Blanco", color="blanco")

    # Colocamos todas las 15 fichas en el home board (usando bucles)
    for _ in range(5): tablero.agregar_ficha(Checker(color="blanco"), 1)
    for _ in range(5): tablero.agregar_ficha(Checker(color="blanco"), 3)
    for _ in range(5): tablero.agregar_ficha(Checker(color="blanco"), 6)

    assert tablero.puede_sacar_fichas(jugador_blanco) is True

def test_sacar_ficha_movimiento_valido():
    """
    Verifica que mover una ficha "fuera" es válido durante el bear off.
    """
    tablero = Board()
    jugador_negro = Player(nombre="Negro", color="negro")

    # Ponemos todas las fichas negras en su home board
    for _ in range(15):
        tablero.agregar_ficha(Checker(color="negro"), 20)

    es_valido = tablero.es_movimiento_valido(jugador_negro, 20, 25)
    assert es_valido is True

def test_sacar_ficha_ejecucion():
    """
    Verifica que el método para sacar una ficha la mueve al área de fuera.
    """
    tablero = Board()
    
    ficha_a_sacar = Checker(color="negro")
    tablero.agregar_ficha(ficha_a_sacar, 22)
    
    tablero.sacar_ficha(22)
    
    assert len(tablero._puntos_[22]) == 0
    assert len(tablero._fichas_fuera_["negro"]) == 1
    assert tablero._fichas_fuera_["negro"][0] == ficha_a_sacar