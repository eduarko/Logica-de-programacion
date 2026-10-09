#Se debe devolver el cuadrado de los elementos pares del arreglo hasta llegar al numero n, un punto importante , el range recorre hasta
#un valor antes del indicado, por ello es necesario sumarle uno
def cuadrados_pares(n):
    cuadrados = []
    for i in range(1,n+1):
        if i%2 == 0:
            cuadrados.append(i**2)
    return cuadrados

print(cuadrados_pares(5))
assert cuadrados_pares(1) == []

#Modo list comprehension
def cuadrados_pares_comprehension(n):
    return [i ** 2 for i in range (1,n+1) if i%2  == 0]

print(cuadrados_pares_comprehension(8))

for k in range(0, 20):
    assert cuadrados_pares(k) == cuadrados_pares_comprehension(k)