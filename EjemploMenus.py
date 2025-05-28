mayor = 0
menor = 1000
exponente = 0
resultado = 0

while True:
    print("-----MENU-----")
    print("1. Calcular el valor de un rango")
    print("2. Calcular polinomio")
    print("3. Salir")
    opc = int(input("Ingrese su opcion: "))

    if opc == 1:
        print("Calculo del valor de un rango")
        cantidad = int(input("Cuantos valores ingresara?: "))

        for i in range(cantidad):
            num = float(input(f"Valor {i+1}: "))

            if num > mayor:
                mayor = num
            
            if num < menor:
                menor = num
            
        rango = mayor - menor
        rango = round(rango,2)
        print("El rango es: ",rango)
    else:
        if opc == 2:
            print("Calculo de polinomio")
            x = float(input("Ingrese valor de x: "))

            while True:
                ingreso = input(f"Ingrese coeficiente a{exponente} o 'FIN' para terminar: ").lower()
                

                if ingreso == "fin":
                    break
                
                coeficiente = float(ingreso)

                resultado = resultado + coeficiente *(x ** exponente)
                exponente = exponente + 1
                
            print("El valor de p(x) : " , round(resultado,3))
        else:
            if opc == 3:
                print("Gracias por usarme!!, nos vemos! ")
                break
            else:
                print("Opcion no valida")

