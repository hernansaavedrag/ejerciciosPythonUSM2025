def calculoGra(masa1,masa2,radio):
    GRAV = 6.67428e-11

    calculo = GRAV * masa1 * masa2 /radio**2
    return calculo

ma1 = float(input("Ingrese masa del primer planeta: "))
ma2 = float(input("Ingrese masa del segundo planeta: "))
rad = float(input("Distancia entre los planetas: "))

resultado = calculoGra(ma1,ma2,rad)


print(resultado)