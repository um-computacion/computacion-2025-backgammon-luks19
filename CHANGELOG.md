Todos los cambios notables del proyecto van a ser documentados en este changelog.

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