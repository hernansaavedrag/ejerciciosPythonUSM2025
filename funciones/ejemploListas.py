colores = ["amarillo","rojo","azul","verde",5]

print(colores)

colores[0] = 'fucsia'
print(colores)

colores.insert(3,"naranjo")

print(colores)

colores.append("blanco")
print(colores)

color = input("Ingrese color: ")
colores.append(color)
print(colores)
'''
colores += [color]
colores = colores + [gris]
print(colores)
'''