"""
Modulo de figuras geometricas
"""

from abc import ABC, abstractmethod


class FiguraGeometrica(ABC):
    """
    Clase abstracta que define la interfaz para calcular áreas.
    """
    @abstractmethod
    def calcular_area(self):
        """
        Método abstracto para calcular el área de la figura.
        """

    @abstractmethod
    def imprimir_area(self):
        """
        Metodo abstracto para imprimir el area de la figura.
        """

class Rectangulo(FiguraGeometrica):
    """
    Objeto rectangulo
    """
    def __init__(self, base, altura):
        """
        Constructor y parametros de entrada
        """
        self._base = None
        self._altura = None
        self.base = base
        self.altura = altura

    @property
    def base(self):
        """
        Getter para la base del rectángulo
        """
        return self._base

    @base.setter
    def base(self, valor):
        """
        Setter para la base del rectángulo con validación
        """
        if valor <= 0:
            raise ValueError("La base debe ser mayor que cero")
        self._base = valor

    @property
    def altura(self):
        """
        Getter para la altura del rectángulo
        """
        return self._altura

    @altura.setter
    def altura(self, valor):
        """
        Setter para la altura del rectángulo con validación
        """
        if valor <= 0:
            raise ValueError("La altura debe ser mayor que cero")
        self._altura = valor

    def calcular_area(self):
        """
        Calcula el área del rectángulo.
        """
        return self._base * self._altura

    def imprimir_area(self):
        print(f"El área del rectángulo es: {self.calcular_area()}")

class Triangulo(FiguraGeometrica):
    """
    Clase que representa un triángulo
    """
    def __init__(self, base, altura):
        """
        Constructor y parametros de entrada
        """
        self._base = None
        self._altura = None
        self.base = base
        self.altura = altura

    @property
    def base(self):
        """
        Getter para la base del triángulo
        """
        return self._base

    @base.setter
    def base(self, valor):
        """
        Setter para la base del triángulo con validación
        """
        if valor <= 0:
            raise ValueError("La base debe ser mayor que cero")
        self._base = valor

    @property
    def altura(self):
        """Getter para la altura del rectángulo"""
        return self._altura
    @altura.setter
    def altura(self, valor):
        """
        Setter para la altura del triángulo con validación
        """
        if valor <= 0:
            raise ValueError("La altura debe ser mayor que cero")
        self._altura = valor

    def calcular_area(self):
        """
        Calcula el área del triángulo.
        """
        return (self._base * self._altura) / 2

    def imprimir_area(self):
        print(f"El área del triangulo es: {self.calcular_area()}")

class Circulo(FiguraGeometrica):
    """
    Clase que representa un círculo
    """
    def __init__(self, radio):
        """
        Constructor y parametros de entrada
        """
        self._pi = 3.14159
        self._radio = None
        self.radio = radio

    @property
    def radio(self):
        """Getter para el radio del círculo"""
        return self._radio

    @radio.setter
    def radio(self, valor):
        """
        Setter para el radio del círculo con validación
    """
        if valor <= 0:
            raise ValueError("El radio debe ser mayor que cero")
        self._radio = valor

    def calcular_area(self):
        """
        Calcula el área del círculo.
        """
        return self._pi * (self._radio ** 2)

    def imprimir_area(self):
        print(f"El área del circulo es: {self.calcular_area()}")


# Variables globales
BASE_RECTANGULO =10
ALTURA_RECTANGULO=5
BASE_TRIANGULO=7
ALTURA_TRIANGULO =4
RADIO_CIRCULO =-3

# Ejecución principal
if __name__ == "__main__":
    # Crear instancias de las figuras
    rectangulo = Rectangulo(BASE_RECTANGULO,ALTURA_RECTANGULO)
    triangulo = Triangulo(BASE_TRIANGULO,ALTURA_TRIANGULO)
    circulo = Circulo(RADIO_CIRCULO)

    # Calcular áreas
    rectangulo.imprimir_area()
    triangulo.imprimir_area()
    circulo.imprimir_area()
