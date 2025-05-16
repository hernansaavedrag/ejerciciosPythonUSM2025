# Preguntar cuántos datos se ingresarán
cantidad = int(input("¿Cuántos datos serán ingresados? "))

# Leer el primer dato y usarlo como valor inicial de mayor y menor
'''dato = float(input("Ingrese el dato número 1: "))
mayor = dato
menor = dato
'''
mayor = 0
menor  = 1000
# Leer el resto de los datos (desde el segundo en adelante)
for i in range(cantidad):
    dato = float(input(f"Ingrese el dato número {i + 1}: "))
    
    if dato > mayor: 
        mayor = dato # mayor = 9
    if dato < menor:
        menor = dato # menor = 1

# Calcular el rango
rango = mayor - menor

# Mostrar el resultado
print("El rango de los datos es:", rango)
