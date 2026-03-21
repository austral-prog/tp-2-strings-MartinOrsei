def rectangle():
    """Lee base y altura de un rectángulo, calcula e imprime
    el área y el perímetro.
    """

    base=int(input("Introducir base: "))
    print(f"Base: {base}")
    altura=int(input("Introducir altura: "))
    print(f"Altura: {altura}")
    area= base * altura
    print(f"Area: {area}")
    perimetro= 2 * (base + altura)
    print(f"Perimetro: {perimetro}")

