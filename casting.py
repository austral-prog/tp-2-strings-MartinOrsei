def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total."""


    precio= int(input("precio del item:"))
    descuento= float(input("descuento:"))
    print(f"Precio: {precio}")
    print(f"Descuento: {descuento}")
    precio_descuento = float(precio - descuento)
    print(f"Precio con descuento: {precio_descuento}")
    cantidad=int(input("cuanto items quiere?:"))
    total= precio_descuento * cantidad
    print(f"Total: {total}")

