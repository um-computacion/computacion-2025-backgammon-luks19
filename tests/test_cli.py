import pytest
from cli.cli import CLI
from core.backgammon_game import BackgammonGame

# `capsys` es una herramienta de pytest que "captura" todo lo que se imprime
# en la consola durante la ejecución de este test.

def test_mostrar_tablero_inicial(capsys):
    """
    Verifica que la CLI muestra correctamente el tablero al inicio.
    """
    # Crear CLI (que crea su propio juego internamente)
    cli = CLI()
    cli._juego_.iniciar_juego()  # Inicializar el juego interno

    # Llamar al método privado de dibujo
    cli._dibujar_tablero_()

    salida_capturada = capsys.readouterr().out
    
    # Verificar que aparecen puntos y fichas (ajustar según tu formato real)
    assert "12 a 1:" in salida_capturada
    assert "13 a 24:" in salida_capturada



