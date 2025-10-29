# Justificación Técnica del Proyecto: Backgammon

Este documento detalla las decisiones de diseño, arquitectura y metodología tomadas durante el desarrollo del proyecto de Backgammon, con el objetivo de justificar el enfoque adoptado y su alineación con los requisitos de la materia y las buenas prácticas de la ingeniería de software.

---

## 1. Resumen del Diseño General

La arquitectura del proyecto se basa en el principio de **Separación de Capas (Layered Architecture)**, dividiendo claramente la aplicación en dos grandes áreas:

*   **Capa de Lógica de Negocio (`core`):** Contiene las reglas, entidades y la lógica fundamental del juego de Backgammon. Es un motor de juego completamente funcional e independiente de cómo se presenta la información al usuario.
*   **Capa de Presentación (`cli`, `pygame_ui`):** Contiene los módulos responsables de la interacción con el usuario. Esta capa consume la lógica del `core` para mostrar el estado del juego y enviar las acciones del usuario, pero nunca modifica directamente el estado del juego.

Este diseño fue elegido deliberadamente para promover la **reusabilidad** del motor de juego, la **mantenibilidad** a largo plazo y, fundamentalmente, para facilitar la **testabilidad** exhaustiva del sistema, un requisito clave del proyecto.

---

## 2. Justificación de Clases y Atributos

### 2.1. Clases Principales y sus Responsabilidades

*   **`BackgammonGame`:** Actúa como el orquestador central del juego. Su única responsabilidad es coordinar el flujo de la partida, gestionar los turnos y servir de intermediario entre la interfaz de usuario y las demás clases del `core`.
*   **`Board`:** Modela el tablero de Backgammon. Encapsula toda la lógica espacial del juego: la posición de las fichas en los 24 puntos, la barra, el área de "bear off", y las reglas para movimientos válidos, capturas y reingresos.
*   **`Player`:** Representa a un jugador. Gestiona su nombre, su color y la colección de fichas que le pertenecen.
*   **`Dice`:** Gestiona la mecánica de los dados. Su responsabilidad se limita a lanzar los dados, proveer los movimientos disponibles (manejando los dobles) y registrar qué tiradas han sido utilizadas.
*   **`Checker`:** Es la entidad más simple, representando una única ficha. Su única responsabilidad es conocer su color y su posición.
*   **`CLI` y `PygameUI`:** Son las clases de la capa de presentación. Su única función es traducir el estado del juego (provisto por `BackgammonGame`) en una representación visual (texto o gráficos) y capturar la entrada del usuario para enviarla al `core`.

### 2.2. Justificación de Atributos Clave

*   **Atributo `_puntos_` en la clase `Board`:** Se eligió un **diccionario de listas** (`dict[int, list[Checker]]`) para representar los 24 puntos del tablero. Esta estructura es ideal por varias razones:
    1.  **Acceso Directo:** Permite acceder a las fichas de cualquier punto en tiempo constante O(1) usando el número del punto como clave (ej. `self._puntos_[10]`), lo cual es mucho más eficiente que buscar en una lista.
    2.  **Modelado Natural:** Modela perfectamente la idea de un "punto" que puede "contener" una cantidad variable de fichas (una lista).
    3.  **Simplicidad:** Facilita operaciones como añadir (`.append()`) o quitar (`.pop()`) fichas de un punto.

---

## 3. Decisiones de Diseño Relevantes

La decisión arquitectónica más importante del proyecto fue la estricta **separación entre la lógica del `core` y las interfaces de usuario (`ui`)**.

### 3.1. Alternativa Considerada y Descartada

*   **Alternativa Considerada:** Integrar la lógica de la interfaz directamente en las clases del `core`. Por ejemplo, que la clase `Board` tuviera métodos como `.dibujar_en_consola()` o `.dibujar_en_pygame()`.
*   **Razón del Descarte:** Esta alternativa habría violado gravemente el **Principio de Responsabilidad Única (SRP)**. La clase `Board` tendría múltiples razones para cambiar: si cambian las reglas del juego, si cambia el formato de la consola, o si cambia la librería gráfica. Esto genera un código frágil, difícil de mantener y casi imposible de testear de forma aislada.

### 3.2. Diseño Elegido: Separación `core` / `ui`

*   **Justificación:** El diseño actual asegura que el `core` no tiene ninguna dependencia de Pygame ni de ninguna otra librería de presentación. Esto permite que el motor del juego pueda ser reutilizado en el futuro para una interfaz web o móvil sin cambiar una sola línea de código del `core`. Más importante aún, permite la creación de una suite de tests unitarios robusta que verifica la lógica del juego sin necesidad de simular clics o leer texto de la pantalla.

---

## 4. Estrategia de Testing y Calidad

Se adoptó un enfoque de calidad de código basado en pruebas automatizadas para garantizar la correctitud y robustez del software.

*   **Framework Utilizado:** Se utilizó `pytest` por su sintaxis clara y su potente ecosistema de plugins, como `pytest-cov`.
*   **Enfoque de Testing:** Se aplicó un enfoque de **pruebas unitarias** centrado en la capa de lógica de negocio (`core`), ya que es la parte más crítica del proyecto. Se crearon tests para cada método público de las clases del `core`, cubriendo escenarios de éxito, casos borde y validaciones de reglas.
*   **Cobertura de Código:** Se utilizó `pytest-cov` para medir la cobertura de los tests. Se alcanzó un **95% de cobertura** sobre el `core`, superando el requisito mínimo del 90% y garantizando que la gran mayoría de las líneas de código de la lógica del juego han sido verificadas por las pruebas.
*   **Testing de CLI:** Para cumplir con el requisito de testear la interfaz de texto, se utilizó la fixture `capsys` de `pytest`. Esta herramienta permite capturar la salida de la consola y verificar que la CLI muestra la información del tablero esperada, demostrando la viabilidad de testear interfaces de texto de forma automatizada.

---

## 5. Referencias a Principios SOLID

El diseño del proyecto se adhiere a varios principios SOLID, fundamentales para un buen diseño orientado a objetos.

*   **Principio de Responsabilidad Única (SRP):** Es el pilar del diseño. Cada clase tiene un único y bien definido propósito. La clase `Dice` solo se encarga de los dados, la clase `Board` solo de las reglas del tablero, y las clases de la UI solo de la presentación. Esto hace que el código sea más fácil de entender, modificar y testear.
*   **Principio Abierto/Cerrado (OCP):** La separación `core`/`ui` permite que el sistema esté "abierto a la extensión" (se pueden añadir nuevas interfaces como una web o móvil) pero "cerrado a la modificación" (no es necesario cambiar el `core` para hacerlo).

---

## 6. Anexos

### Diagrama de Clases UML

![diagramauml](image.png)
