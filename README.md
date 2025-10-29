# Backgammon - Computación 2025

> Una implementación completa del juego de Backgammon en Python, con una lógica de juego robusta, una interfaz de línea de comandos y una interfaz gráfica de usuario con Pygame.

Este repositorio contiene la implementación del juego de Backgammon, desarrollado como proyecto para la materia Computación 2025. El proyecto demuestra la aplicación de principios de diseño de software como la separación de capas y el desarrollo guiado por pruebas (TDD) para construir una aplicación funcional y de alta calidad.

**Autor:** Lucas Valdemoros



## Guía de Instalación y Uso

Esta guía te llevará paso a paso para que puedas ejecutar el juego en tu propia computadora.

### 1. Prerrequisitos

Antes de empezar, asegúrate de tener instalado lo siguiente en tu sistema:

*   **Python:** Se recomienda la versión 3.10 o una más reciente.
*   **Git:** Necesario para descargar el código del proyecto desde GitHub.

### 2. Instalación (Paso a Paso)

Estos comandos deben ejecutarse en tu terminal o consola.

**Paso 1: Descargar el Proyecto**
Usa `git` para clonar (descargar) una copia del proyecto en tu computadora y navega a la nueva carpeta. comando que debes usar:

git clone https://github.com/um-computacion/computacion-2025-backgammon-luks19.git
cd computacion-2025-backgammon-luks19

## Paso 3: Crear un Entorno Virtual

Un entorno virtual es una “caja” aislada para tu proyecto.  
Es una buena práctica para evitar que las librerías de este proyecto interfieran con otros que tengas.

# Este comando crea una carpeta llamada 'env' que contendrá el entorno:
python -m venv env

# En Linux o macOS:
source env/bin/activate

# En Windows (usando PowerShell):
# .\env\Scripts\Activate.ps1

## Paso 4: Instalar las Librerías del Juego

El último paso es instalar todas las librerías que el juego necesita para funcionar, como pygame. El siguiente comando lo hace todo automáticamente.

# Este comando lee el archivo setup.py e instala todo lo necesario.
pip install -e .

¡Y eso es todo! Tu entorno está listo.



## Cómo Jugar

### a) Versión Gráfica con Pygame (Recomendada)

Para la experiencia de juego visual e interactiva, ejecuta:

python main.py

Se abrirá una ventana con el tablero de Backgammon.

### b) Versión de Texto en Consola (CLI)

Si prefieres una experiencia clásica en la terminal, ejecuta:

python cli/cli.py

El juego te dará instrucciones en la consola para que introduzcas tus movimientos.




# Cómo Jugar (Interfaz Gráfica)

Una vez que ejecutas python main.py, verás la ventana del juego. Aquí te explicamos qué significa cada cosa y cómo jugar.

## ¿Qué Ves en Pantalla?

**Turno Actual:** En la parte superior de la pantalla, verás un texto que indica de quién es el turno (ej. "Turno de: Jugador 1 (blanco)").

**Dados:** Al lado del turno, verás los valores de los dados que debes usar en tus movimientos.

**Tablero y Fichas:** Verás el tablero de Backgammon con las 15 fichas blancas y 15 negras en sus posiciones iniciales.

## Reglas del Juego y Acciones del Jugador

El objetivo es ser el primer jugador en mover todas sus 15 fichas fuera del tablero.

### Movimiento de Fichas:

Las fichas blancas se mueven en sentido antihorario (de puntos mayores a menores, del 24 al 1).

Las fichas negras se mueven en sentido horario (de puntos menores a mayores, del 1 al 24).

### Seleccionar y Mover:

**Seleccionar:** Haz clic con el ratón sobre una de tus fichas. Si la selección es válida, la ficha se resaltará con un borde amarillo, indicando que está lista para moverse.

**Mover:** Una vez que tienes una ficha seleccionada, haz clic en el punto de destino al que la quieres mover. Si el movimiento es válido según las reglas y los dados, la ficha se moverá.

**Cancelar Selección:** Si seleccionaste una ficha por error, simplemente haz clic en cualquier lugar fuera del tablero para deseleccionarla.

## Reglas Importantes:

**Captura:** Si mueves una ficha a un punto ocupado por una sola ficha del oponente (un "blot"), la ficha del oponente es capturada y movida a la barra central.

**Bloqueo:** No puedes mover una ficha a un punto que esté ocupado por dos o más fichas del oponente.

**Reingreso desde la Barra:** Si tienes fichas en la barra, tu única prioridad es reingresarlas al tablero antes de poder mover cualquier otra ficha.

**Sacar Fichas (Bear Off):** Solo puedes empezar a sacar tus fichas del tablero una vez que todas tus 15 fichas estén en tu cuadrante.