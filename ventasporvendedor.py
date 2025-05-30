# Ventas acumuladas por vendedor
venta_larry = 0
venta_curly = 0
venta_moe = 0

# Mayor venta individual y su autor
mayor_venta = 0
mayor_vendedor = ""

# Menú principal
while True:
    print("1.- Ingresar ventas")
    print("2.- Venta mayor")
    print("3.- Peor vendedor")
    print("0.- Salir")
    op = input("Operacion? ")

    if op == "1":
        nombre = input("Nombre vendedor: ").lower()
        cantidad = int(input("Cantidad vendida: "))

        if nombre == "larry":
            venta_larry = venta_larry + cantidad
        elif nombre == "curly":
            venta_curly = venta_curly + cantidad
        elif nombre == "moe":
            venta_moe = venta_moe + cantidad

        if cantidad > mayor_venta:
            mayor_venta = cantidad
            mayor_vendedor = nombre

    elif op == "2":
        if mayor_venta > 0:
            print("La mayor venta realizada fue de " + str(mayor_venta) + " y la realizo " + mayor_vendedor)
        else:
            print("Aún no hay ventas registradas.")

    elif op == "3":
        # Determinar el peor vendedor
        peor_vendedor = ""
        menor_venta = venta_larry

        if venta_curly < menor_venta:
            menor_venta = venta_curly
            peor_vendedor = "curly"
        else:
            peor_vendedor = "larry"

        if venta_moe < menor_venta:
            menor_venta = venta_moe
            peor_vendedor = "moe"

        print("El vendedor que menos a vendido es " + peor_vendedor)

    elif op == "0":
        print("moe vendio: " + str(venta_moe) + " productos")
        print("larry vendio: " + str(venta_larry) + " productos")
        print("curly vendio: " + str(venta_curly) + " productos")
        break

    else:
        print("La operacion no existe")
