def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """

    print("Ingresar gasto:" )
    gasto = float(input())
    print(gasto)
    print("Dinero recibido")
    Dinero = int(input())
    print(Dinero)

    pesos = int(Dinero - gasto)
    centavos =round((float(Dinero - gasto) - pesos) * 100)

    print("\nVuelto\n" )
    print("Pesos:")
    print(pesos)
    print("Centavos:")
    print(centavos)

