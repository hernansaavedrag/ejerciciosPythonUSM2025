# Ingreso de inversión inicial y tasa de descuento
inversion_inicial = float(input("Ingrese la inversión inicial: "))
tasa_descuento = float(input("Ingrese la tasa de descuento mensual (porcentaje): ")) / 100

# Inicializar variables
van = -inversion_inicial
mes = 1

# Bucle que se ejecuta hasta que el VAN sea positivo
while van <= 0:
    flujo = float(input("Ingrese el flujo estimado del mes " + str(mes) + ": "))
    van += flujo / ((1 + tasa_descuento) ** mes)
    print("VAN acumulado (parte entera):", int(van))
    if van > 0:
        print("El proyecto es rentable. Termina el programa.")
        break
    mes += 1
