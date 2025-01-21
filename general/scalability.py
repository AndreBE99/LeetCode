# Escalabilidad
# Un ejemplo de escalabilidad podría incluir el uso de caché para evitar múltiples cálculos en un sistema.
class FibonacciCache:
    def __init__(self):
        self.cache = {}

    def fibonacci(self, n):
        if n in self.cache:
            return self.cache[n]
        if n <= 1:
            return n
        self.cache[n] = self.fibonacci(n - 1) + self.fibonacci(n - 2)
        return self.cache[n]

fib_cache = FibonacciCache()
print(fib_cache.fibonacci(10))  # Escalable al reducir el tiempo de cálculo
