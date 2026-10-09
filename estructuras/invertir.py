
def invertir_diccionario(elementos):
    """Invierte un diccionario, es decir una lista que tiene elementos con clave y valor
    Lanza ValueError si hay valores repetidos.
    """
    diccionario_invertido = {}
    for clave, valor in elementos.items():
        if valor in diccionario_invertido:
            raise ValueError(f"Valor repetido: {valor}")
        diccionario_invertido[valor]=clave
    return diccionario_invertido

print(invertir_diccionario({"a":2,"b":3}))
print(invertir_diccionario({"a":2}))
print(invertir_diccionario({"a":""}))
print(invertir_diccionario({"a":None}))
print(invertir_diccionario({"a":3,"b":3}))

