def string_methods():
    """Demuestra el uso de métodos de string: strip, lstrip, rstrip, upper, lower,
    title, find, replace, count, operador in, slicing con paso, reverso,
    f-strings y strings multilínea.
    """
    nombre = "   Grace Hopper   "
    frase = "Python es un gran lenguaje de programacion"
    multilinea = """Linea 1
Linea 2
Linea 3"""

    nombre_sin = nombre.strip()
    print(f"Strip: {nombre_sin}")
    nombre_sin_izq= nombre.lstrip()
    print(f"Lstrip: {nombre_sin_izq}")
    nombre_sin_der= nombre.rstrip()
    print(f"Rstrip: {nombre_sin_der}")
    print(f"Upper: {frase.upper()}")
    print(f"Lower: {frase.lower()}")
    print(f"Title: {frase.title()}")
    print(f"Find: {frase.find("gran")}")
    frase_desarrollo= frase.replace("programacion" , "desarrollo")
    print(f"Replace: {frase_desarrollo}")
    print(f"Count: {frase.count("a")}")
    print(f"Contiene Python: {"Python" in frase}" )
    print(f"Contiene Java: {"java" in frase}")
    print(f"Slice: {frase[:6]}")
    print(f"Paso: {frase[:6:2]}")
    python = "Python"
    print(f"Reverso: {python[::-1]}")
    print(f"Formato: {nombre_sin} sabe {frase[:6]}")
    print(multilinea)

