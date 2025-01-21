# Herencia
class Vehiculo:
  def __init__(self, velocidad_maxima, capacidad):
    self.velocidad_maxima = velocidad_maxima
    self.capacidad = capacidad

  def arrancar(self):
    print("El vehículo ha arrancado.")

class Automovil(Vehiculo):
  def __init__(self, velocidad_maxima, capacidad, num_puertas):
    super().__init__(velocidad_maxima, capacidad)
    self.num_puertas = num_puertas

class Camion(Vehiculo):
  def __init__(self, velocidad_maxima, capacidad, carga_maxima):
    super().__init__(velocidad_maxima, capacidad)
    self.carga_maxima = carga_maxima


if __name__ == '__main__':
  # Crear instancias de vehículos
  automovil = Automovil(180, 5, 4)
  camion = Camion(120, 2, 1000)

  # Usar métodos de Vehiculo y las subclases
  automovil.arrancar()
  print(f"Automóvil - Velocidad máxima: {automovil.velocidad_maxima} km/h, Capacidad: {automovil.capacidad} personas")

  camion.arrancar()
  print(f"Camión - Velocidad máxima: {camion.velocidad_maxima} km/h, Carga máxima: {camion.carga_maxima} kg")
