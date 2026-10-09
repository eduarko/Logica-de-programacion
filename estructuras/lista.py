#Se debe crear una lista sin valores repetidos y mantener el orden en que aparecieron
def sin_duplicados(elementos):
    """Devuelve la lista sin repetidos, conservando el orden."""
    resultado = []
    for elemento in elementos:
        if elemento not in resultado:
            resultado.append(elemento)
    return resultado

print(sin_duplicados([3,2,2,1,"hola","hola"]))
print(sin_duplicados([]))
assert sin_duplicados([1,2,2,3])==[1,2,3]
