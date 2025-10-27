"""
Configuración de coordenadas para el tablero de Backgammon.
Ajustado para una imagen de 448x448 píxeles centrada en una ventana de 800x600.
"""

# Dimensiones de la ventana y el tablero
ANCHO_VENTANA = 800
ALTO_VENTANA = 600
ANCHO_TABLERO = 448
ALTO_TABLERO = 448

# Offset del tablero (para centrarlo)
OFFSET_X = (ANCHO_VENTANA - ANCHO_TABLERO) // 2  # 176
OFFSET_Y = (ALTO_VENTANA - ALTO_TABLERO) // 2    # 76

# Tamaño de las fichas
TAMANO_FICHA = 35

# Coordenadas X de los puntos (relativas a la imagen del tablero)
# Lado derecho (puntos 1-6 y 19-24)
PUNTO_24_X = 405
PUNTO_23_X = 365
PUNTO_22_X = 325
PUNTO_21_X = 285
PUNTO_20_X = 245
PUNTO_19_X = 205

# Lado izquierdo (puntos 7-12 y 13-18)
PUNTO_18_X = 163
PUNTO_17_X = 123
PUNTO_16_X = 83
PUNTO_15_X = 43
PUNTO_14_X = 43
PUNTO_13_X = 43

PUNTO_12_X = 43
PUNTO_11_X = 83
PUNTO_10_X = 123
PUNTO_9_X = 163
PUNTO_8_X = 205
PUNTO_7_X = 245

PUNTO_6_X = 285
PUNTO_5_X = 325
PUNTO_4_X = 365
PUNTO_3_X = 405
PUNTO_2_X = 405
PUNTO_1_X = 405

# Coordenadas Y
Y_SUPERIOR = 80   # Para puntos 13-24 (arriba)
Y_INFERIOR = 368  # Para puntos 1-12 (abajo)

# Espaciado vertical entre fichas apiladas
ESPACIADO_FICHAS = 30

# Mapeo de número de punto a coordenadas (x, y) ABSOLUTAS (incluyendo offset)
COORDENADAS_PUNTOS = {
    # Fila inferior (puntos 1-12)
    1: (OFFSET_X + PUNTO_1_X, OFFSET_Y + Y_INFERIOR),
    2: (OFFSET_X + PUNTO_2_X, OFFSET_Y + Y_INFERIOR),
    3: (OFFSET_X + PUNTO_3_X, OFFSET_Y + Y_INFERIOR),
    4: (OFFSET_X + PUNTO_4_X, OFFSET_Y + Y_INFERIOR),
    5: (OFFSET_X + PUNTO_5_X, OFFSET_Y + Y_INFERIOR),
    6: (OFFSET_X + PUNTO_6_X, OFFSET_Y + Y_INFERIOR),
    7: (OFFSET_X + PUNTO_7_X, OFFSET_Y + Y_INFERIOR),
    8: (OFFSET_X + PUNTO_8_X, OFFSET_Y + Y_INFERIOR),
    9: (OFFSET_X + PUNTO_9_X, OFFSET_Y + Y_INFERIOR),
    10: (OFFSET_X + PUNTO_10_X, OFFSET_Y + Y_INFERIOR),
    11: (OFFSET_X + PUNTO_11_X, OFFSET_Y + Y_INFERIOR),
    12: (OFFSET_X + PUNTO_12_X, OFFSET_Y + Y_INFERIOR),
    
    # Fila superior (puntos 13-24)
    13: (OFFSET_X + PUNTO_13_X, OFFSET_Y + Y_SUPERIOR),
    14: (OFFSET_X + PUNTO_14_X, OFFSET_Y + Y_SUPERIOR),
    15: (OFFSET_X + PUNTO_15_X, OFFSET_Y + Y_SUPERIOR),
    16: (OFFSET_X + PUNTO_16_X, OFFSET_Y + Y_SUPERIOR),
    17: (OFFSET_X + PUNTO_17_X, OFFSET_Y + Y_SUPERIOR),
    18: (OFFSET_X + PUNTO_18_X, OFFSET_Y + Y_SUPERIOR),
    19: (OFFSET_X + PUNTO_19_X, OFFSET_Y + Y_SUPERIOR),
    20: (OFFSET_X + PUNTO_20_X, OFFSET_Y + Y_SUPERIOR),
    21: (OFFSET_X + PUNTO_21_X, OFFSET_Y + Y_SUPERIOR),
    22: (OFFSET_X + PUNTO_22_X, OFFSET_Y + Y_SUPERIOR),
    23: (OFFSET_X + PUNTO_23_X, OFFSET_Y + Y_SUPERIOR),
    24: (OFFSET_X + PUNTO_24_X, OFFSET_Y + Y_SUPERIOR),
}

# Coordenadas para la barra (fichas capturadas)
BARRA_X = OFFSET_X + 224  # Centro del tablero
BARRA_Y_NEGRAS = OFFSET_Y + 150
BARRA_Y_BLANCAS = OFFSET_Y + 298

# Coordenadas para las zonas de bear-off (sacar fichas)
BEAROFF_NEGRAS_X = OFFSET_X + 430
BEAROFF_NEGRAS_Y = OFFSET_Y + 224
BEAROFF_BLANCAS_X = OFFSET_X + 18
BEAROFF_BLANCAS_Y = OFFSET_Y + 224