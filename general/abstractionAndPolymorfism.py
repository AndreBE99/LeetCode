# Abstraccion y polimorfismo
from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

class Circulo(Forma):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return 3.1416 * self.radio ** 2

class Rectangulo(Forma):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def calcular_area(self):
        return self.ancho * self.alto

if __name__ == '__main__':
  # Crear instancias de formas
  circulo = Circulo(5)
  rectangulo = Rectangulo(4, 3)

  # Calcular área usando polimorfismo
  formas = [circulo, rectangulo]
  for forma in formas:
      print(f"Área de {forma.__class__.__name__}: {forma.calcular_area()}")
