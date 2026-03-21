def slice_simple():
    """Dado el texto 'Awesome', imprime distintos substrings
    usando slicing y lower().
    """
    texto = "Awesome"
    texto_minuscula = texto.lower()
    print(texto_minuscula[:3])
    print(texto_minuscula[2:5])
    print(texto_minuscula)

