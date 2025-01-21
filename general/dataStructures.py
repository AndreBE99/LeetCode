# Estructuras de datos
# Aquí se muestra una estructura de pila (stack) implementada usando una lista.
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "Stack is empty"

    def is_empty(self):
        return len(self.stack) == 0

# Usage
stack = Stack()
stack.push(5)
stack.push(10)
print(stack.pop())  # Output: 10
