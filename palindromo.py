def es_palindromo(texto):
    """Codigo para revisar si una palabra, frase u oración es palíndroma. Es decir , si se lee igual alrevés"""
    palindromo = texto[::-1].replace(" ","").lower()
    texto_limpio = texto.replace(" ","").lower()
    return texto_limpio == palindromo

print(es_palindromo("osO"))

"""Una forma de inventir el texto de forma mas lógica es utilizando una cadena vacía , ya que al concatenar las letras estas se irán
agregando a la cadena en el orden que han sido leídas, por ejemplo si analizamos la palabra rayar , el texto será leido de la siguiente forma
r a y a r
Y la inserción se verá así:
 ""
 "r"
 "ar"
 "yar"
 "ayar"
 "rayar"
 """
def invertir(texto):
    resultado = ""
    texto_normalizado = texto.lower()
    for letra in texto_normalizado:
        resultado = letra + resultado
    return resultado

print(invertir("paraguas"))
