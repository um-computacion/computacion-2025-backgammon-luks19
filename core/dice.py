import random

class Dice:
    """
    Representa un par de dados de Backgammon.
    Gestiona el lanzamiento y los movimientos disponibles.
    """
    def __init__(self):
        """
        Inicializa los dados. Los valores se guardan para referencia,
        y las tiradas disponibles se calculan en cada lanzamiento.
        """
        self._valor_dado1_ = None
        self._valor_dado2_ = None
        self._tiradas_disponibles_ = []

    def lanzar(self):
        """
        Simula el lanzamiento de dos dados y calcula las tiradas disponibles.
        """
        self._valor_dado1_ = random.randint(1, 6)
        self._valor_dado2_ = random.randint(1, 6)

        if self._valor_dado1_ == self._valor_dado2_:
            # Caso de dobles: 4 movimientos
            self._tiradas_disponibles_ = [self._valor_dado1_] * 4
        else:
            # Caso normal: 2 movimientos
            self._tiradas_disponibles_ = [self._valor_dado1_, self._valor_dado2_]

    def obtener_valores(self) -> tuple[int | None, int | None]:
        """Devuelve una tupla con los valores de la tirada."""
        return (self._valor_dado1_, self._valor_dado2_)

    def obtener_tiradas_disponibles(self) -> list[int]:
        """Devuelve la lista de movimientos que quedan por usar."""
        return self._tiradas_disponibles_

    def usar_tirada(self, valor: int) -> bool:
        """
        Intenta usar un valor de tirada. Si está disponible, lo elimina y devuelve True.
        """
        if valor in self._tiradas_disponibles_:
            self._tiradas_disponibles_.remove(valor)
            return True
        else:
            return False

    def reiniciar(self):
        """Reinicia los dados a su estado inicial antes de una nueva tirada."""
        self._valor_dado1_ = None
        self._valor_dado2_ = None
        self._tiradas_disponibles_ = []
