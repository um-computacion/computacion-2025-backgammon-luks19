## Prompt 1: Solicitud de un Formato Estándar para Documentar Prompts

- **Modelo / herramienta usada:** Manus

- **El texto exacto del prompt:**
  > mira en mi proyecto debo documentar lso pormpts utilizados en los archivos: prompts-desarrollo.md`, `prompts-testing.md`, o `prompts-documentacion.md. puedes darme el formato para escribir los mensajes de los archivos de pormpts

- **Respuesta/resultado completo devuelto por la IA:**
  > ¡Excelente idea! Tener una plantilla o formato estandarizado te ahorrará mucho tiempo y asegurará que todos tus registros sean consistentes y cumplan con los requisitos del profesor.
  >
  > Aquí te presento un formato limpio y bien estructurado que puedes copiar y pegar en tus archivos `.md` cada vez que necesites documentar una nueva interacción con una IA.
  >
  > ---
  >
  > ### **Formato / Plantilla para `prompts-*.md`**
  >
  > Copia este bloque de código completo y pégalo en el archivo `.md` correspondiente (`prompts-desarrollo.md`, `prompts-testing.md`, o `prompts-documentacion.md`). Luego, simplemente reemplaza el texto de ejemplo con tu información real.
  >
  > ```markdown
  > ## Prompt X: [Escribe aquí un título corto y descriptivo de la interacción]
  >
  > - **Modelo / herramienta usada:** [Nombre de la IA, ej: Manus, ChatGPT, DeepSeek, etc.]
  >
  > - **El texto exacto del prompt:**
  >   > [Pega aquí la pregunta o instrucción completa y literal que le diste a la IA. Usa el formato de cita `>` para que se destaque.]
  >
  > - **Respuesta/resultado completo devuelto por la IA:**
  >   > [Pega aquí la respuesta completa y literal que recibiste de la IA. También usa el formato de cita `>`.]
  >
  > - **Indicación de uso:** [Elige UNA de las siguientes opciones y borra las otras]
  >     - **Usado sin cambios:** La respuesta de la IA se implementó tal cual.
  >     - **Usado con modificaciones:** La idea o el código de la IA se usó como base, pero tuve que hacerle los siguientes cambios: [Describe brevemente qué modificaste, por ejemplo: "cambié el nombre de las variables para que encajaran con mi proyecto" o "simplifiqué la lógica del bucle para que fuera más legible"].
  >     - **Descartado:** La respuesta no fue útil o era incorrecta, y no se utilizó en el proyecto.
  >
  > - **Referencia a los archivos finales:** [Indica aquí el o los archivos de tu proyecto que fueron creados o modificados como resultado de esta interacción. Si no aplica, puedes poner "N/A". Ejemplos:]
  >     - `core/dice.py`
  >     - `.gitignore`
  >     - `README.md`
  > ```

- **Indicación de uso:** **Usado sin cambios.** El formato proporcionado fue adoptado como la plantilla estándar para documentar todas las interacciones con herramientas de IA en los archivos `prompts-*.md` del proyecto.

- **Referencia a los archivos finales:** `prompts-desarrollo.md`, `prompts-testing.md`, `prompts-documentacion.md`.
