# Encapsulamiento
class CuentaBancaria:
  def __init__(self, titular, numero_cuenta):
    self.__saldo = 0  # Atributo privado
    self.titular = titular
    self.numero_cuenta = numero_cuenta

  def depositar(self, cantidad):
    if cantidad > 0:
      self.__saldo += cantidad

  def retirar(self, cantidad):
    if 0 < cantidad <= self.__saldo:
      self.__saldo -= cantidad

  def obtener_saldo(self):
    return self.__saldo

if __name__ == '__main__':
  # Crear una cuenta bancaria y realizar operaciones
  cuenta = CuentaBancaria("Juan Pérez", "00123456789")
  cuenta.depositar(500)
  print(f"Saldo después del depósito: {cuenta.obtener_saldo()}")

  # Intentar retirar dinero
  cuenta.retirar(100)
  print(f"Saldo después del retiro: {cuenta.obtener_saldo()}")

  # Intentar retirar más de lo disponible
  cuenta.retirar(500)  # No debería permitir el retiro
  print(f"Saldo después de intento de retiro excedente: {cuenta.obtener_saldo()}")
