def crear_reporte(fecha, temperaturas): # Imprimir encabezado con la fecha print("REPORTE DEL DÍA {}-{}-{}:".format(fecha[0], fecha[1], fecha[2]))
# Recorrer el diccionario de ciudades
    for ciudad in temperaturas:
        temp_min = temperaturas[ciudad][0]
        temp_max = temperaturas[ciudad][1]
        
        # Convertir el nombre a mayúsculas si la máxima es mayor a 25
        if temp_max > 25:
            nombre_ciudad = ciudad.upper()
        else:
            nombre_ciudad = ciudad
        
        # Imprimir la línea del reporte
        print(f"{nombre_ciudad}: max {temp_max}, min {temp_min}")

temperaturas = {
    'Vina del Mar': [9, 26],
    'Valparaiso': [10, 24],
    'Quilpue': [7, 30],
    'Olmue': [5, 29],
    'Limache': [9, 23],
    'Villa Alemana': [9, 22]
}
 
crear_reporte([2011, 5, 14], temperaturas)
'''
REPORTE DEL DÍA 2011-5-14:
VINA DEL MAR: max 26, min 9
Valparaiso: max 24, min 10
QUILPUE: max 30, min 7
OLMUE: max 29, min 5
Limache: max 23, min 9
Villa Alemana: max 22, min 9
'''
