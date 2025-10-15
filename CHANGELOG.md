# Changelog
Todos los cambios notables del proyecto van a ser documentados en este archivo.

## [15/10/2024]
### Agregado
- Nueva clase Board para gestionar el tablero de juego
- Métodos para el dibujo y renderizado del tablero en la interfaz gráfica

## [14/10/2024]
### Agregado
- Método para el inicio y gestión de la interfaz gráfica
- Bases para la futura estructura del proyecto
### Cambiado
- Refactor completo del archivo Main.py

## [13/10/2024]
### Agregado
- Método para verificar el ganador del juego
- Integración de la condición de victoria en la interfaz de línea de comandos (CLI)
- Inicio del desarrollo con Pygame para la interfaz gráfica

## [30/09/2024]
### Agregado
- Método para verificar condiciones de finalización del juego
- Método para manejar la lógica de fin de partida (victoria/empate)

### Cambiado
- Finalización del bucle principal del juego con integración completa de la lógica de finalización

## [29/09/2024]
### Agregado
- Conexión entre la interfaz CLI y el módulo Core del juego
- Configuración del bucle de movimientos para el turno actual
- Implementación del bucle principal del juego con interacción de usuario

### Cambiado
- Integración de la lógica del juego con el flujo principal

## [28/09/2024]
### Cambiado
- Configuración y mejora del archivo main.py
- Refactorización y finalización del método Run() en el módulo CLI para mejor funcionalidad

## [26/09/2024]
### Agregado
- Método para la representación visual del tablero de juego
- Método para la gestión y manipulación del estado del tablero
- Creación del archivo main.py como punto de entrada de la aplicación

## [16/09/2025]
### Agregado
- Creación de la carpeta `cli/` y su archivo principal para la interfaz de línea de comandos
- Implementación de la base fundamental del módulo CLI
- Método para la representación visual actualizada del tablero en la interfaz CLI

## [15/09/2025]
### Agregado
- Implementación de lógica para sacar fichas del tablero en el juego de backgammon
- Clase BackgammonGame completa con métodos para manejar el estado del juego

### Cambiado
- Refactor de la estructura del proyecto para incluir la nueva clase BackgammonGame
- Mejora en la validación de movimientos para incluir la posibilidad de bear off

## [09/09/2024]
### Agregado
- Lógica de captura de fichas en la clase Board
- Sistema de reingreso de fichas en el juego

### Cambiado
- Mejorada la estructura de la clase Board
- Refactorizado código para mejor mantenibilidad

## [08/09/2024]
### Cambiado
- Implementadas mejoras generales en la clase Board
- Refactorización de código existente

## [07/09/2025]
### Agregado
- Nuevos desarrollos aplicados en `prompts-documentación.md` y otros archivos de documentación
- Implementación de la clase `Board` y realización de pruebas asociadas
- Creación de la carpeta `assets` para almacenar imágenes y sonidos

### Corregido
- Ajustes menores en los archivos mencionados para mejorar consistencia y organización

## [04/09/2025]
### Agregado
- Desarrollos y mejoras en `README.md` y `prompts-documentación.md`
- Creación de la carpeta `prompts-ai` para organizar archivos relacionados con prompts

### Corregido
- Configuración correcta del archivo `.gitignore` para excluir archivos innecesarios

## [02/09/2025]
### Agregado
- Implementación de la Clase Player (TDD):
  - Clase `Player` en `core/player.py` con lógica para la creación de sus 15 fichas
  - Tests unitarios correspondientes en `tests/test_player.py` para validar la inicialización y métodos básicos
- Documentación del proyecto:
  - Actualización del archivo `CHANGELOG.md` para reflejar el progreso de los últimos días
  - Refinada la documentación del diseño y la metodología de testing

## [01/09/2025]
### Agregado
- Implementación de la Clase Dice (TDD):
  - Clase `Dice` en `core/dice.py` con lógica completa para lanzar dados y gestionar tiradas normales y dobles
  - Tests unitarios en `tests/test_dice.py` para asegurar el correcto funcionamiento

### Corregido
- Solucionado error de entorno (`ModuleNotFoundError`):
  - Problema de importación que impedía a `pytest` encontrar los módulos del `core`
  - Configuración de archivo `setup.py` e instalación del proyecto en modo editable (`pip install -e .`)

## [30/08/2025]
### Agregado
- Implementación inicial de la Clase Checker (TDD):
  - Clase `Checker` completamente funcional en `core/checker.py`
  - Tests unitarios para `Checker` en `tests/test_checker.py`
- Estructura de archivos del proyecto:
  - Carpetas y archivos base para el `core` del juego (`board.py`, `backgammon_game.py`, etc.)
  - Inicialización de la carpeta `tests` con su `__init__.py`

## [26/08/2025]
### Agregado
- Configuración de CircleCI para integración continua
- Archivo de configuración `.circleci/config.yml` con pipeline de tests y reporte de cobertura
- Configuración completa del archivo `.gitignore` para excluir:
  - `__pycache__/`
  - `venv/`
  - `.coverage`
  - `coverage.xml`

### Corregido
- Problema con la rama por defecto del repositorio (cambiado de 'feedback' a 'main')
- Sincronización correcta de cambios entre ramas después del pull request

## [25/08/2025]
### Agregado
- Estructura sólida del proyecto con todos los archivos y carpetas base
- Creación de la estructura de carpetas:
  - `.github/` (para futuras configuraciones de GitHub)
  - `assets/` (para recursos del proyecto)
  - `cli/` (para interfaz de línea de comandos)
  - `core/` (para lógica principal del juego)
  - `pygame_ui/` (para interfaz gráfica con Pygame)
- Creación de archivos de documentación esenciales:
  - `CHANGELOG.md`
  - `JUSTIFICATION.md`
  - `README.md`
  - `prompts-desarrollo.md`
  - `prompts-documentacion.md`
  - `prompts-testing.md`
- Archivo `requirements.txt` para dependencias del proyecto
- Configuración inicial del repositorio Git

