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
    
    assert isinstance(juego._tablero_, Board)
    assert isinstance(juego._jugador1_, Player)
    assert isinstance(juego._jugador2_, Player)
    assert isinstance(juego._dados_, Dice)
    
    assert juego._jugador1_._nombre_ == "Jugador 1"
    assert juego._jugador2_._nombre_ == "Jugador 2"
    
    assert juego._jugador_actual_ is None # El juego aún no ha empezado
    assert juego._ganador_ is None
    assert juego._juego_terminado_ is False

def test_iniciar_juego():
    """
    Verifica que el método iniciar_juego configura el tablero
    y establece un jugador actual para comenzar.
    """
    juego = BackgammonGame("Jugador 1", "Jugador 2")
    juego.iniciar_juego()
    
    # Verifica que el tablero se ha configurado (buscando una pieza conocida)
    assert len(juego._tablero_._puntos_[1]) == 2 # 2 fichas negras en el punto 1
    
    # Verifica que se ha asignado un jugador actual
    assert juego._jugador_actual_ is not None
    assert juego._jugador_actual_ in [juego._jugador1_, juego._jugador2_]

def test_cambiar_jugador():
    """
    Verifica que el turno cambia correctamente entre los dos jugadores.
    """
    juego = BackgammonGame("Jugador 1", "Jugador 2")
    juego.iniciar_juego() # Asigna un jugador inicial
    
    jugador_inicial = juego._jugador_actual_
    juego.cambiar_jugador()
    jugador_siguiente = juego._jugador_actual_
    
    assert jugador_inicial != jugador_siguiente
    
    # Verificamos que vuelve al jugador inicial después de otro cambio
    juego.cambiar_jugador()
    assert juego._jugador_actual_ == jugador_inicial

def test_verificar_ganador():
    """
    Verifica que el juego detecta correctamente cuando un jugador ha ganado.
    """
    juego = BackgammonGame("Jugador 1", "Jugador 2")
    juego.iniciar_juego()
    
    # Simulamos que el jugador 1 (negras) ha sacado todas sus 15 fichas
    # Para esto, simplemente llenamos su lista de fichas fuera en el tablero
    for _ in range(15):
        juego._tablero_._fichas_fuera_["negro"].append(Checker(color="negro"))
        
    # Llamamos al método que verifica la condición de victoria
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