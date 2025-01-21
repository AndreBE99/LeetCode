# En el problema debemos revisar los pares adyacentes, por ejemplo para 11001110, se revisa:
# 11 -> 00 -> 11 -> 10
# De este modo, solo en el ultimo par se necesita hacer el cambio.
# Durante el recorrido de cada par, se debe pasar al siguiente con i + 2

def minChanges(s: str) -> int:
    count = 0
    for i in range(0, len(s), 2):
        if s[i] != s[i+1]: count = count + 1
    return count

if __name__ == "__main__":
    test_strings = [
        "1001",  # Ejemplo 1
        "10",     # Ejemplo 2
        "0000",    # Ejemplo 3
        "000111",    # Ejemplo 4
        "1111",      # Ejemplo 5
        "01010101",   # Ejemplo 6
        "0011100110",  # Ejemplo 7
        "11000111",  # Ejemplo 8
    ]

    for s in test_strings:
        print(f"Input string: {s}")
        print(f"Substring count: {minChanges(s)}\n")