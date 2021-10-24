
    a = int(input("Indique el radio de la mesa: \n"))
    pi: float = 3.1416
    radioAlCuadrado = a**2
    descuento =0
    areaCirculo = radioAlCuadrado*pi



    if areaCirculo > 20:
        descuento = 20
    else:
        if areaCirculo< 20:
            descuento = 10

    print(f"el area de la mesa es: {areaCirculo}")
    print(f"Tienes un descuento de : {descuento}")