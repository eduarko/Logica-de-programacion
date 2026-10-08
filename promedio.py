

def calcular_promedio(notas):
    """Devuelve el promedio de una lista de notas.
    Lanza ValueError si la lista está vacía.
    """
    if len(notas) == 0:
        raise ValueError("La lista está vacía")
        return 0

    else:
        cantidad=len(notas)
        suma = sum(notas)
        promedio = suma/cantidad
        return promedio
    

print(calcular_promedio([]))


    
