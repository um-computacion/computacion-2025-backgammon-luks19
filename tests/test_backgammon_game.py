import pytest
from core.backgammon_game import BackgammonGame
from core.player import Player
from core.board import Board
from core.dice import Dice
from core.checker import Checker 

def test_creacion_del_juego():
    """
    Verifica que el juego se inicializa correctamente con todos sus componentes.
    """
    juego = BackgammonGame("Jugador 1", "Jugador 2")
    
    assert hasattr(juego._tablero_, '_puntos_')
    assert hasattr(juego._jugador1_, '_fichas_')
    assert hasattr(juego._jugador2_, '_fichas_')
    assert hasattr(juego._dados_, '_tiradas_disponibles_')
    
    assert juego._jugador1_._nombre_ == "Jugador 1"
    assert juego._jugador2_._nombre_ == "Jugador 2"
    
    assert juego._jugador_actual_ is None
    assert juego._ganador_ is None
    assert juego._juego_terminado_ is False

def test_iniciar_juego():
    """
    Verifica que el método iniciar_juego configura el tablero
    y establece un jugador actual para comenzar.
    """
    juego = BackgammonGame("Jugador 1", "Jugador 2")
    juego.iniciar_juego()
    
    assert len(juego._tablero_._puntos_[1]) == 2
    assert juego._jugador_actual_ is not None
    assert juego._jugador_actual_ in [juego._jugador1_, juego._jugador2_]

def test_cambiar_jugador():
    """
    Verifica que el turno cambia correctamente entre los dos jugadores.
    """
    juego = BackgammonGame("Jugador 1", "Jugador 2")
    juego.iniciar_juego()
    
    jugador_inicial = juego._jugador_actual_
    juego.cambiar_jugador()
    jugador_siguiente = juego._jugador_actual_
    
    assert jugador_inicial != jugador_siguiente
    
    juego.cambiar_jugador()
    assert juego._jugador_actual_ == jugador_inicial

def test_verificar_ganador():
    """
    Verifica que el juego detecta correctamente cuando un jugador ha ganado.
    """
    juego = BackgammonGame("Jugador 1", "Jugador 2")
    juego.iniciar_juego()
    
    for _ in range(15):
        juego._tablero_._fichas_fuera_["negro"].append(Checker(color="negro"))
        
    juego._verificar_ganador_()
    
    assert juego._juego_terminado_ is True
    assert juego._ganador_ == juego._jugador1_

def test_no_hay_ganador_al_inicio():
    """
    Verifica que al inicio del juego, no hay ningún ganador.
    """
    juego = BackgammonGame("Jugador 1", "Jugador 2")
    juego.iniciar_juego()
    
    juego._verificar_ganador_()
    
    assert juego._juego_terminado_ is False
    assert juego._ganador_ is None

def test_realizar_movimiento_exitoso():
    """
    Verifica que un movimiento válido se realiza correctamente.
    """
    juego = BackgammonGame("Jugador 1", "Jugador 2")
    juego.iniciar_juego()
    juego._jugador_actual_ = juego._jugador1_
    juego._dados_._tiradas_disponibles_ = [3, 5]
    
    resultado = juego.realizar_movimiento(1, 4)
    
    assert resultado == "OK"
    assert 3 not in juego._dados_._tiradas_disponibles_

def test_realizar_movimiento_ilegal():
    """
    Verifica que un movimiento ilegal es rechazado.
    """
    juego = BackgammonGame("Jugador 1", "Jugador 2")
    juego.iniciar_juego()
    juego._jugador_actual_ = juego._jugador1_
    juego._dados_._tiradas_disponibles_ = [3, 5]
    
    resultado = juego.realizar_movimiento(1, 24)
    
    assert resultado == "MOVIMIENTO_ILEGAL"

def test_realizar_movimiento_tirada_no_disponible():
    """
    Verifica que se rechaza un movimiento cuando la distancia no está en las tiradas.
    """
    juego = BackgammonGame("Jugador 1", "Jugador 2")
    juego.iniciar_juego()
    juego._jugador_actual_ = juego._jugador1_
    juego._dados_._tiradas_disponibles_ = [3, 5]
    
    resultado = juego.realizar_movimiento(1, 5)
    
    assert resultado == "TIRADA_NO_DISPONIBLE"

def test_realizar_movimiento_bear_off():
    """
    Verifica que sacar fichas funciona correctamente.
    """
    juego = BackgammonGame("Jugador 1", "Jugador 2")
    juego.iniciar_juego()
    juego._jugador_actual_ = juego._jugador1_
    juego._dados_._tiradas_disponibles_ = [6]
    
    juego._tablero_._puntos_ = {i: [] for i in range(1, 25)}
    juego._tablero_.agregar_ficha(Checker(color="negro"), 19)
    
    resultado = juego.realizar_movimiento(19, 25)
    
    assert resultado == "OK"
    assert len(juego._tablero_._fichas_fuera_["negro"]) == 1

def test_realizar_movimiento_desde_barra():
    """
    Verifica que mover desde la barra funciona correctamente.
    """
    juego = BackgammonGame("Jugador 1", "Jugador 2")
    juego.iniciar_juego()
    juego._jugador_actual_ = juego._jugador1_
    juego._dados_._tiradas_disponibles_ = [3]
    
    juego._tablero_._barra_["negro"].append(Checker(color="negro"))
    
    resultado = juego.realizar_movimiento(0, 3)
    
    assert resultado == "OK"