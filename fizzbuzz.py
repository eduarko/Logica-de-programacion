def fizzbuzz(n):
    """Devuelve una lista del 1 al n con las reglas de FizzBuzz."""
    resultado = []
    for i in range(1,n+1):
        if i%15 == 0:
            resultado.append("FizzBuzz")
        elif i%5 == 0:
            resultado.append("Buzz")
        elif i%3 == 0:
            resultado.append("Fizz")
        else:
            resultado.append(i)
    return resultado

print(fizzbuzz(25))
        