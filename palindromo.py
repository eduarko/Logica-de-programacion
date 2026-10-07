def es_palindromo(texto):
    """Codigo para revisar si una palabra, frase u oración es palíndroma. Es decir , si se lee igual alrevés"""
    palindromo = texto[::-1].replace(" ","").lower()
    texto_limpio = texto.replace(" ","").lower()
    return texto_limpio == palindromo

print(es_palindromo("osO"))