tipo_vehiculo = input("Tipo Vehiculo: ")
dia = input("Dia: ")
hora = input("Horario: ")

hora_hh = int(hora[0:2])
hora_mm = int(hora[3:5])
minutos = hora_hh * 60 + hora_mm
print(minutos)