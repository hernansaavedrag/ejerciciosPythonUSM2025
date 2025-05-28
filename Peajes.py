tipo_vehiculo = input("Tipo Vehiculo: ")
dia = input("Dia: ")
hora = input("Horario: ")

hora_hh = int(hora[0:2])
hora_mm = int(hora[3:5])
minutos = hora_hh * 60 + hora_mm
print(minutos)

# si es auto, ingresamos la cantidad de pasajeros
if tipo_vehiculo == "auto":
    cantidad_pasajeros = int(input("Cantidad Pasajeros: "))

total = 0

if dia == "sabado" or dia == "domingo":
    # Hora alta congestion: 08:30 a 11:00 y 17:45 a 22:30
    if (minutos >= 510 and minutos <= 660) or (minutos >= 1065 and minutos <= 1350):
        if tipo_vehiculo == "camion":
            total = 4500
        else:
            total = 4500 - (cantidad_pasajeros * 300)
    else:
        if tipo_vehiculo == "camion":
            total = 3800
        else:
            total = 2800

# lunes a viernes
else:
    # Hora alta congestion: 07:30 a 09:30 y 17:30 a 20:00
    if (minutos >= 450 and minutos <= 570) or (minutos >= 1050 and minutos <= 1200):
        if tipo_vehiculo == "camion":
            total = 3500
        else:
            if cantidad_pasajeros >= 3:
                total = 0
            else:
                total = 2400
    else:
        if tipo_vehiculo == "camion":
            total = 2500
        else:
            total = 2000 - (cantidad_pasajeros * 100)

print("Total a pagar:", total)
