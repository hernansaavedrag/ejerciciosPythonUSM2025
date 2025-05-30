# Entrada de datos iniciales
capacidad = float(input("Capacidad bateria (AH): "))
voltaje = float(input("Voltaje bateria (volt): "))
base_tiempo = float(input("Base de tiempo (Horas): "))
k = 1.15

# Inicialización
potencia_total = 0.0
cantidad_ampolletas = 0
sigue = True

while sigue:
    cantidad_ampolletas = cantidad_ampolletas + 1
    texto = "Potencia ampolleta " + str(cantidad_ampolletas) + " (Watt): "
    nueva_potencia = float(input(texto))

    potencia_total_nueva = potencia_total + nueva_potencia
    corriente = potencia_total_nueva / voltaje

    # Fórmula corregida según tu definición:
    autonomia = base_tiempo / ((corriente * base_tiempo / capacidad) ** k)

    if autonomia >= 8:
        potencia_total = potencia_total_nueva
        print("Autonomia: " + str(round(autonomia, 3)) + " [Horas]. Ampolletas: " + str(cantidad_ampolletas) + ". Potencia Total: " + str(potencia_total) + " [Watt]")
    else:
        cantidad_ampolletas = cantidad_ampolletas - 1
        print("Total de Ampolletas: " + str(cantidad_ampolletas))
        sigue = False

