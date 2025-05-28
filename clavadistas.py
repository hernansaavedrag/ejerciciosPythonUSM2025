#Parte (a): Puntaje total de un clavadista

nombre = input("Nombre: ")
grado = float(input("Grado de dificultad: "))

# Ingreso de puntajes
j1 = float(input("Juez 1: "))
j2 = float(input("Juez 2: "))
j3 = float(input("Juez 3: "))
j4 = float(input("Juez 4: "))
j5 = float(input("Juez 5: "))
j6 = float(input("Juez 6: "))
j7 = float(input("Juez 7: "))

# Encontrar máximo y mínimo
maximo = j1
if j2 > maximo:
    maximo = j2
if j3 > maximo:
    maximo = j3
if j4 > maximo:
    maximo = j4
if j5 > maximo:
    maximo = j5
if j6 > maximo:
    maximo = j6
if j7 > maximo:
    maximo = j7

minimo = j1
if j2 < minimo:
    minimo = j2
if j3 < minimo:
    minimo = j3
if j4 < minimo:
    minimo = j4
if j5 < minimo:
    minimo = j5
if j6 < minimo:
    minimo = j6
if j7 < minimo:
    minimo = j7

# Suma total y eliminación de mayor y menor
suma = j1 + j2 + j3 + j4 + j5 + j6 + j7
suma = suma - maximo - minimo

# Cálculo del puntaje total
puntaje_total = suma * 3/5 * grado

print("El puntaje total es", puntaje_total)

#Parte (b): Múltiples clavadistas, encontrar al ganador

mayor_puntaje = 0
ganador = ""

while True:
    nombre = input("Nombre: ")
    if nombre == "FIN":
        break

    grado = float(input("Grado de dificultad: "))

    j1 = float(input("Juez 1: "))
    j2 = float(input("Juez 2: "))
    j3 = float(input("Juez 3: "))
    j4 = float(input("Juez 4: "))
    j5 = float(input("Juez 5: "))
    j6 = float(input("Juez 6: "))
    j7 = float(input("Juez 7: "))

    maximo = j1
    if j2 > maximo:
        maximo = j2
    if j3 > maximo:
        maximo = j3
    if j4 > maximo:
        maximo = j4
    if j5 > maximo:
        maximo = j5
    if j6 > maximo:
        maximo = j6
    if j7 > maximo:
        maximo = j7

    minimo = j1
    if j2 < minimo:
        minimo = j2
    if j3 < minimo:
        minimo = j3
    if j4 < minimo:
        minimo = j4
    if j5 < minimo:
        minimo = j5
    if j6 < minimo:
        minimo = j6
    if j7 < minimo:
        minimo = j7

    suma = j1 + j2 + j3 + j4 + j5 + j6 + j7
    suma = suma - maximo - minimo

    puntaje_total = suma * 3/5 * grado

    if puntaje_total > mayor_puntaje:
        mayor_puntaje = puntaje_total
        ganador = nombre

print("El ganador es", ganador)
