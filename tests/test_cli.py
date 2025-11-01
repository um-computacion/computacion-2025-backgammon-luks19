import pytest
from cli.cli import CLI
from core.backgammon_game import BackgammonGame

def test_creacion_cli():
    """
    Verifica que la CLI se crea correctamente con un juego interno.
    """
    cli = CLI()
    
    assert cli._juego_ is not None
    assert isinstance(cli._juego_, BackgammonGame)
    assert cli._juego_._jugador1_._nombre_ == "Jugador 1 (Negras)"
    assert cli._juego_._jugador2_._nombre_ == "Jugador 2 (Blancas)"

def test_juego_se_inicializa():
    """
    Verifica que el juego interno se puede inicializar correctamente.
    """
    cli = CLI()
    cli._juego_.iniciar_juego()
    
    assert cli._juego_._jugador_actual_ is not None
    assert cli._juego_._tablero_._puntos_[1] != []
    assert cli._juego_._tablero_._puntos_[24] != []

def test_tablero_tiene_fichas_inicial():
    """
    Verifica que después de iniciar el juego, el tablero tiene las fichas en sus posiciones.
    """
    cli = CLI()
    cli._juego_.iniciar_juego()
    
    tablero = cli._juego_._tablero_
    
    # Verificar algunas posiciones iniciales de negras
    assert len(tablero._puntos_[1]) == 2
    assert tablero._puntos_[1][0].obtener_color() == "negro"
    
    # Verificar algunas posiciones iniciales de blancas
    assert len(tablero._puntos_[24]) == 2
    assert tablero._puntos_[24][0].obtener_color() == "blanco"