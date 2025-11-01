import pytest
from unittest.mock import patch
from core.dice import Dice

def test_creacion_dice():
    """Verifica que la clase se inicializa correctamente."""
    dados = Dice()
    assert dados.obtener_valores() == (None, None)
    assert dados.obtener_tiradas_disponibles() == []

@patch('random.randint')
def test_lanzar_calcula_tiradas_correctamente(mock_randint):
    """
    Verifica que el método lanzar() actualiza el estado interno
    de las tiradas disponibles, tanto para tiradas normales como para dobles.
    """
    # --- Caso 1: Tirada Normal ---
    mock_randint.side_effect = [3, 5]
    dados = Dice()
    dados.lanzar()
    # Verificamos el estado interno que 'lanzar' debe haber modificado
    assert dados.obtener_tiradas_disponibles() == [3, 5]

    # --- Caso 2: Tirada de Dobles ---
    mock_randint.side_effect = None # Reseteamos el mock
    mock_randint.return_value = 4
    dados.lanzar()
    assert dados.obtener_tiradas_disponibles() == [4, 4, 4, 4]

@patch('random.randint')
def test_obtener_valores_refleja_el_lanzamiento(mock_randint):
    """
    Verifica que obtener_valores() devuelve correctamente los valores
    que se generaron en el último lanzamiento.
    """
    mock_randint.side_effect = [6, 2]
    dados = Dice()
    dados.lanzar()
    # Ahora probamos el método 'obtener'
    assert dados.obtener_valores() == (6, 2)

def test_usar_tirada_exitosa():
    """Verifica que se puede usar una tirada disponible."""
    dados = Dice()
    # Preparamos el estado interno para el test
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
    assert dados.obtener_tiradas_disponibles() == [6, 1] # La lista no debe cambiar

def test_reiniciar_dados_limpia_el_estado():
    """
    Verifica que el método reiniciar() restaura los dados a su estado inicial.
    """
    dados = Dice()
    # Le damos un estado inicial no vacío
    dados._valor_dado1_ = 5
    dados._valor_dado2_ = 5
    dados._tiradas_disponibles_ = [5, 5, 5, 5]
    
    dados.reiniciar() # Ejecutamos la acción a probar
    
    # Verificamos que el estado se ha limpiado
    assert dados.obtener_valores() == (None, None)
    assert dados.obtener_tiradas_disponibles() == []