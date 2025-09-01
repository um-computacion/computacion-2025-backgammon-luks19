import pytest
from unittest.mock import patch
from core.dice import Dice

def test_creacion_dice():
    """Verifica que la clase se inicializa correctamente."""
    dados = Dice()
    assert dados.obtener_valores() == (None, None)
    assert dados.obtener_tiradas_disponibles() == []

@patch('random.randint')
def test_lanzar_dados_normal(mock_randint):
    """Testea una tirada normal (no doble)."""
    mock_randint.side_effect = [3, 5]
    dados = Dice()
    dados.lanzar()
    assert dados.obtener_valores() == (3, 5)
    assert dados.obtener_tiradas_disponibles() == [3, 5]

@patch('random.randint')
def test_lanzar_dados_dobles(mock_randint):
    """Testea una tirada de dobles."""
    mock_randint.return_value = 4
    dados = Dice()
    dados.lanzar()
    assert dados.obtener_valores() == (4, 4)
    assert dados.obtener_tiradas_disponibles() == [4, 4, 4, 4]

def test_usar_tirada_exitosa():
    """Verifica que se puede usar una tirada disponible."""
    dados = Dice()
    dados._tiradas_disponibles_ = [6, 1]
    usada = dados.usar_tirada(1)
    assert usada is True
    assert dados.obtener_tiradas_disponibles() == [6]

def test_usar_tirada_inexistente():
    """Verifica que no se puede usar una tirada no disponible."""
    dados = Dice()
    dados._tiradas_disponibles_ = [6, 1]
    usada = dados.usar_tirada(5)
    assert usada is False
    assert dados.obtener_tiradas_disponibles() == [6, 1]

def test_reiniciar_dados():
    """Verifica que los dados se reinician a su estado inicial."""
    dados = Dice()
    dados.lanzar() # Le damos un estado
    dados.reiniciar()
    assert dados.obtener_valores() == (None, None)
    assert dados.obtener_tiradas_disponibles() == []
