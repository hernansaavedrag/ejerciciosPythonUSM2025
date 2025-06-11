'''lista = input("Ingrese listado de numeros").split()
print(lista)

numeros = []
for dato in lista:
    numeros.append(int(dato))

print(numeros)
'''

def validar_lista_numeros():
    while True:
        entrada = input("Ingresa números enteros separados por espacios: ")
        elementos = entrada.split()
        try:
            numeros = []
            for e in elementos:
                numeros.append(int(e))  # Intenta convertir a entero
            return numeros  # Si no hubo error, retorna la lista
        except ValueError:
            print("Error: Debes ingresar solo números enteros. Intenta de nuevo.\n")

# Uso
#lista_valida = validar_lista_numeros()
#print("Lista validada:", lista_valida)

def clasificar_pares_impares(numeros):
    pares = []
    impares = []
    for num in numeros:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
    return pares, impares


# Programa principal

lista = validar_lista_numeros()
pares, impares = clasificar_pares_impares(lista)

print("Resultado:")
print("Números pares:   ", pares if pares else "Ninguno")
print("Números impares:", impares if impares else "Ninguno")
