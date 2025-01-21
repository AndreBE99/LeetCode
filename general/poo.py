# Programacion orientada a objetos POO
# La POO se centra en modelar objetos y su interacción. En este ejemplo, implementamos una jerarquía de clases para vehículos.
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}")

class Car(Vehicle):
    def __init__(self, make, model, seats):
        super().__init__(make, model)
        self.seats = seats

    def display_info(self):
        super().display_info()
        print(f"Seats: {self.seats}")

car = Car("Toyota", "Corolla", 5)
car.display_info()
