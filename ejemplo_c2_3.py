# Pedir el valor de x
x = float(input("Ingrese el valor de x: "))

# Variables para el resultado y el exponente actual
resultado = 0
exponente = 0

# Leer coeficientes hasta que se escriba "FIN"
while True:
    entrada = input("Ingrese el coeficiente a" + str(exponente) + " (o 'FIN' para terminar): ")
    
    if entrada == "FIN":
        break
    
    coeficiente = float(entrada)
    
    # Sumar al resultado el término correspondiente
    #resultado += coeficiente * (x ** exponente)
    resultado = resultado + coeficiente * (x ** exponente)
    
    # Pasar al siguiente exponente
    #exponente += 1
    exponente = exponente +1 
# Mostrar resultado final
print("El valor del polinomio en x =", x, "es:", resultado)
