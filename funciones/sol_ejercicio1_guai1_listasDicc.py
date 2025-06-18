def validar_lista_numeros():
    while True:
        lista = input("Ingrese numeros enteros separados por espacio: ").split()
        try:
            numeros = []
            for dato in lista:
                numeros.append(int(dato))
            return numeros
        except ValueError:
            print("Error , debe ingresar solo números")

def clasificar_pares_impares(numeros):
    pares = []
    impares = []
    for num in numeros:
        if num%2 ==0 :
            pares.append(num)
        else:
            impares.append(num) 
    return pares,impares   

#lista = input("Ingrese numeros enteros separados por espacio: ").split()
#print(lista)
numeros = validar_lista_numeros()
print(numeros)
pares,impares = clasificar_pares_impares(numeros)
print("Números pares son: ",pares)
print("Números impares son: ",impares)
