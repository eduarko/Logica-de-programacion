def calcular_factorial(n):
    """Devuelve el factorial de un número"""
    resultado = 1
    for i in range(1, n+1):
        resultado = resultado * i
    return resultado

print(calcular_factorial(5))

def factorial_recursivo(n):
    """Devuelve n! de forma recursiva."""
    if n <= 1:
        return 1
    return n + factorial_recursivo(n-1)

print(factorial_recursivo(3))