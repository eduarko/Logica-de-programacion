#Utilizando la funcion get(elemento, valor base)
def contar_palabras(texto):
    palabras = texto.split()
    diccionario={}
    for palabra in palabras:
        diccionario[palabra] = diccionario.get(palabra, 0) +1
    return diccionario

print(contar_palabras("hola mundo hola"))
print(contar_palabras(""))


def contar_palabras_basico(texto):
    """Forma mas explícita de realizar el conteo
    Creamos un diccionario vacio y lo llenamos con los casos evaluados, si la palabra no se encuentra en el,
    se agrega , si se repite el conteo incrementa, de esta forma se obtiene un diccionario cuya clave es la palabra y el valor es 
    la cantidad de veces que se repite"""
    palabras = texto.split()
    diccionario = {}
    for palabra in palabras:
        if palabra in diccionario:
            diccionario[palabra]+=1
        else:
            diccionario[palabra]=1
    return diccionario

print(contar_palabras_basico("erase una vez"))
    

