Todos los cambios notables del proyecto van a ser documentados en este changelog.

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
- Nuevos desarrollos aplicados en `prompts-documentación.md` y otros archivos de documentación.
- Implementación de la clase `Board` y realización de pruebas asociadas.
- Creación de la carpeta `assets` para almacenar imágenes y sonidos.

### Corregido
- Ajustes menores en los archivos mencionados para mejorar consistencia y organización.

## [04/09/2025]
### Agregado
- Desarrollos y mejoras en `README.md` y `prompts-documentación.md`.
- Creación de la carpeta `prompts-ai` para organizar archivos relacionados con prompts.

### Corregido
- Configuración correcta del archivo `.gitignore` para excluir archivos innecesarios.

## [02/09/2025]
### Agregado
*   **Implementación de la Clase Player (TDD):**
    *   Añadida la clase `Player` en `core/player.py`, con lógica para la creación de sus 15 fichas.
    *   Creados los tests unitarios correspondientes en `tests/test_player.py` para validar la inicialización y métodos básicos.
*   **Documentación del Proyecto:**
    *   Actualizado el archivo `CHANGELOG.md` para reflejar el progreso de los últimos días.
    *   Refinada la documentación del diseño y la metodología de testing.

## [01/09/2025]
### Agregado
*   **Implementación de la Clase Dice (TDD):**
    *   Añadida la clase `Dice` en `core/dice.py` con la lógica completa para lanzar dados y gestionar tiradas normales y dobles.
    *   Creados los tests unitarios en `tests/test_dice.py` para asegurar el correcto funcionamiento.

### Corregido
*   **Solucionado Error de Entorno (`ModuleNotFoundError`):**
    *   Se resolvió el problema de importación que impedía a `pytest` encontrar los módulos del `core`.
    *   Se configuró un archivo `setup.py` y se instaló el proyecto en modo editable (`pip install -e .`) para garantizar que la estructura de paquetes sea reconocida correctamente por el entorno virtual.

## [30/08/2025]
### Agregado
*   **Implementación Inicial de la Clase Checker (TDD):**
    *   Añadida la clase `Checker` completamente funcional en `core/checker.py`.
    *   Creados los tests unitarios para `Checker` en `tests/test_checker.py`.
*   **Estructura de Archivos del Proyecto:**
    *   Creada la estructura de carpetas y archivos base para el `core` del juego (`board.py`, `backgammon_game.py`, etc.).
    *   Inicializada la carpeta `tests` con su `__init__.py`.

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

