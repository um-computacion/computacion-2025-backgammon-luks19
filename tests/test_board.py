import pytest
from core.board import Board
from core.checker import Checker
from core.player import Player 

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

def test_mover_ficha_simple():
    """
    Verifica que una ficha se puede mover de un punto a otro vacío.
    """
    tablero = Board()
    
    # Colocamos una ficha blanca en el punto 1 para moverla
    ficha_a_mover = Checker(color="blanco", posicion_inicial=1)
    tablero.agregar_ficha(ficha_a_mover, 1)
    
    # Movemos la ficha del punto 1 al 4 (una tirada de 3)
    tablero.mover_ficha(1, 4)
    
    assert len(tablero._puntos_[1]) == 0
    assert len(tablero._puntos_[4]) == 1
    assert tablero._puntos_[4][0].obtener_color() == "blanco"
    # Verificamos que la posición interna de la ficha se actualizó
    assert ficha_a_mover.obtener_posicion() == 4

def test_es_movimiento_valido_simple():
    """
    Verifica la validación de un movimiento simple y legal.
    """
    tablero = Board()
    jugador_blanco = Player(nombre="Test", color="blanco")
    
    # Colocamos una ficha del jugador en el punto 1
    tablero.agregar_ficha(Checker(color="blanco"), 1)
    
    # Un movimiento de 3 (del punto 1 al 4) debería ser válido para las negras (sentido creciente)
    # y no para las blancas. Vamos a testear para las negras.
    jugador_negro = Player(nombre="Test2", color="negro")
    tablero.agregar_ficha(Checker(color="negro"), 1)
    
    es_valido = tablero.es_movimiento_valido(jugador_negro, 1, 4)
    assert es_valido is True

def test_es_movimiento_valido_bloqueado():
    """
    Verifica que un movimiento a un punto bloqueado por el oponente no es válido.
    """
    tablero = Board()
    jugador_negro = Player(nombre="Test", color="negro")
    
    # Colocamos una ficha negra en el punto 1
    tablero.agregar_ficha(Checker(color="negro"), 1)
    
    # Bloqueamos el punto 4 con dos fichas blancas
    tablero.agregar_ficha(Checker(color="blanco"), 4, cantidad=2)
    
    # El movimiento del 1 al 4 ahora debería ser inválido
    es_valido = tablero.es_movimiento_valido(jugador_negro, 1, 4)
    assert es_valido is False

def test_es_movimiento_valido_direccion_incorrecta_blancas():
    """
    Verifica que un jugador de blancas no puede mover sus fichas hacia adelante (sentido creciente).
    """
    tablero = Board()
    jugador_blanco = Player(nombre="Test", color="blanco")
    
    # Colocamos una ficha blanca en el punto 5
    tablero.agregar_ficha(Checker(color="blanco"), 5)
    
    # Un movimiento hacia "adelante" (del 5 al 7) debería ser inválido para las blancas
    es_valido = tablero.es_movimiento_valido(jugador_blanco, 5, 7)
    assert es_valido is False

def test_mover_ficha_con_captura():
    """
    Verifica que al mover a un punto con una sola ficha enemiga (blot),
    la ficha enemiga es capturada y movida a la barra.
    """
    tablero = Board()
    jugador_negro = Player(nombre="Negro", color="negro")

    # 1. Ficha del jugador negro lista para mover en el punto 1
    tablero.agregar_ficha(Checker(color="negro"), 1)

    # 2. Ficha enemiga (blanca) sola en el punto 4, lista para ser capturada
    ficha_a_capturar = Checker(color="blanco", posicion_inicial=4)
    tablero.agregar_ficha(ficha_a_capturar, 4)

    # 3. El jugador negro mueve del 1 al 4 (una tirada de 3)
    tablero.mover_ficha(1, 4)

    # --- Verificaciones ---
    # El punto de origen (1) debe estar vacío
    assert len(tablero._puntos_[1]) == 0

    # El punto de destino (4) ahora debe tener una sola ficha, y debe ser negra
    assert len(tablero._puntos_[4]) == 1
    assert tablero._puntos_[4][0].obtener_color() == "negro"

    # La barra del jugador blanco debe contener la ficha capturada
    assert len(tablero._barra_["blanco"]) == 1
    assert tablero._barra_["blanco"][0] == ficha_a_capturar
    
    # La barra del jugador negro debe seguir vacía
    assert len(tablero._barra_["negro"]) == 0

def test_movimiento_invalido_si_hay_fichas_en_la_barra():
    """
    Verifica que si un jugador tiene fichas en la barra, no puede mover
    otras fichas en el tablero. Su único movimiento legal es reingresar.
    """
    tablero = Board()
    jugador_negro = Player(nombre="Negro", color="negro")

    # 1. Ponemos una ficha del jugador negro en la barra
    ficha_en_barra = Checker(color="negro")
    tablero.agregar_a_barra(ficha_en_barra)

    # 2. Ponemos otra ficha del mismo jugador en el tablero
    tablero.agregar_ficha(Checker(color="negro"), 10)

    # 3. Verificamos que mover la ficha del tablero (del 10 al 12) es INVÁLIDO
    # porque está obligado a mover primero la de la barra.
    es_valido = tablero.es_movimiento_valido(jugador_negro, 10, 12)
    assert es_valido is False

def test_reingreso_desde_la_barra_es_valido():
    """
    Verifica que un movimiento para reingresar una ficha desde la barra
    al tablero del oponente es considerado válido.
    (Nota: El movimiento exacto depende de la tirada del dado, aquí solo
    validamos la regla general de que el reingreso es posible).
    """
    tablero = Board()
    jugador_negro = Player(nombre="Negro", color="negro")

    # 1. Ponemos una ficha del jugador negro en la barra
    ficha_en_barra = Checker(color="negro")
    tablero.agregar_a_barra(ficha_en_barra)

    # 2. Verificamos que un intento de reingreso es válido.
    # Para las negras, reingresar desde la barra es como mover desde un "punto 0".
    # Un movimiento al punto 3 (tirada de 3) debería ser válido.
    es_valido = tablero.es_movimiento_valido(jugador_negro, 0, 3) # Usamos 0 para la barra
    assert es_valido is True