# Sintaxis usada: [start:stop:step]
# start: Es el índice donde comienza el corte. Si se omite, empieza desde el principio de la secuencia.
# stop: Es el índice donde termina el corte, pero no incluye el carácter de ese índice. Si se omite, el corte llega hasta el final de la secuencia.
# step: Es el valor que indica el paso o dirección en la que se recorre la secuencia. Un valor positivo recorre de izquierda a derecha, mientras que un valor negativo lo hace de derecha a izquierda.
def isPalindrome(x: int) -> bool:
    a = str(x)  
    if a == a[::-1]:  
        return True
    return False

if __name__ == '__main__':
    test_strings = [
        '121',
        '-121',
        '10',
    ]

    for s in test_strings:
        print(f'Input string: {s}')
        print(f'Output: {isPalindrome(s)}')