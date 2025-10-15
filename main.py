from cli.cli import CLI
from pygame_ui.pygame_ui import PygameUI

def main():
    """
    Punto de entrada principal del programa.
    Permite al usuario elegir qué interfaz desea utilizar.
    """
    while True:
        print("\n--- Backgammon Computación 2025 ---")
        print("1. Jugar en la Terminal (CLI)")
        print("2. Jugar con Interfaz Gráfica (Pygame)")
        print("3. Salir")
        
        opcion = input("Elige una opción: ")
        
        if opcion == '1':
            print("Iniciando CLI...")
            cli_juego = CLI()
            cli_juego.run()
            break
        elif opcion == '2':
            print("Iniciando Pygame...")
            try:
                pygame_juego = PygameUI()
                pygame_juego.run()
            except Exception as e:
                print(f"\nError al iniciar Pygame: {e}")
                print("Asegúrate de tener Pygame instalado (`pip install pygame`) y un entorno gráfico disponible.")
            break
        elif opcion == '3':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elige 1, 2 o 3.")

if __name__ == "__main__":
    main()
