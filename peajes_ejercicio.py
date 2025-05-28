resp = "s"
while resp == "s":
    while True:

        tipoVehiculo = input("Tipo Vehículo (Auto/Camion): ").lower()
        if tipoVehiculo == "camion" or tipoVehiculo == "auto":
            break
        else:
            print("Por favor, ingrese camion o auto")

    dia = input("Dia: ")
    while True:
        hora = input("Horario (HH:MM): ")
        try:
            hora_HH = int(hora[0:2])
            hora_MM = int(hora[3:5])
            minutos = hora_HH * 60 + hora_MM
            break
        except ValueError:
            print("Error al ingresar horario, por favor ingrese el formato correcto")

    #print(minutos)

    if tipoVehiculo == "auto":
        cant_pasajeros = int(input("Cantidad de pasajeros: "))

    #fin de semana
    if dia == "sabado" or dia == "domingo":
        #alta congestión 8:30 a 11:00 y 17:45 a 22:30
        # en minutos --> 510 a 660 y 1065 a 1350
        if (minutos >= 510 and minutos <= 660) or (minutos >= 1065 and minutos <= 1350):
            if tipoVehiculo == "camion":
                total = 4500
            else:
                total = 4500 - (cant_pasajeros * 300)
        else:
            if tipoVehiculo == "camion":
                total = 3800
            else:
                total = 2800
    else: # lunes a viernes
        #alta congestión 7:30 a 09:30 y 17:30 a 20:00
        if (minutos >= 450 and minutos <= 570) or (minutos >= 1050 and minutos <= 1200):
            if tipoVehiculo == "camion":
                total = 3500
            else:
                if cant_pasajeros >= 3:
                    total = 0
                else:
                    total = 2400
        else:
            if tipoVehiculo == "camion":
                total = 2500
            else:
                total = 2000 - (cant_pasajeros * 100)

    print("Total a pagar : $",total)
    resp = input("Desea calcular nuevamente? (s/n)")
    if resp == "n":
        print("Gracias por usarme!!")





