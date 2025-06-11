# Datos del grupo (listas en lugar de tuplas)
grupo = {
    'rick': [172, 10], 'daryl': [136, 11], 'michonne': [80, 6],
    'glenn': [73, 0], 'maggie': [55, 4], 'carl': [62, 1],
    'tyreese': [35, 0], 'carol': [17, 3]
}

# Función total
def total(grupo):
    total_walkers = 0
    total_humanos = 0
    for datos in grupo.values():
        total_walkers += datos[0]
        total_humanos += datos[1]
    return (float(total_walkers), float(total_humanos))

# Función puntaje
def puntaje(grupo):
    total_walkers, total_humanos = total(grupo)
    puntajes = {}
    for nombre, datos in grupo.items():
        w = datos[0]
        h = datos[1]
        pw = w / total_walkers if total_walkers > 0 else 0
        ph = h / total_humanos if total_humanos > 0 else 0
        puntajes[nombre] = round(pw + 2 * ph, 2)
    return puntajes

# Función ranking
'''def ranking(grupo):
    puntos = puntaje(grupo)
    ordenados = sorted(puntos.items(), key=lambda x: x[1], reverse=True)
    return [nombre for nombre, _ in ordenados]'''

def obtener_puntaje(elemento):
    return elemento[1]

def ranking(grupo):
    puntos = puntaje(grupo)
    ordenados = sorted(puntos.items(), key=obtener_puntaje, reverse=True)
    return [nombre for nombre, _ in ordenados]


# Menú interactivo
def menu():
    while True:
        print("\nMENÚ DE SUPERVIVIENTES")
        print("1. Ver total de walkers y humanos eliminados")
        print("2. Ver puntaje de cada miembro")
        print("3. Ver ranking del grupo")
        print("4. Salir")
        opcion = input("Elige una opción (1-4): ")

        if opcion == "1":
            tw, th = total(grupo)
            print(f"\nTotal de walkers: {tw}")
            print(f"Total de humanos: {th}")
        elif opcion == "2":
            print("\nPuntaje de cada miembro:")
            for nombre, valor in puntaje(grupo).items():
                print(f"{nombre}: {valor}")
        elif opcion == "3":
            print("\nRanking del grupo (mayor a menor):")
            for i, nombre in enumerate(ranking(grupo), 1):
                print(f"{i}. {nombre}")
        elif opcion == "4":
            print("Saliendo... ¡mantente con vida!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

# Ejecutar menú
menu()
