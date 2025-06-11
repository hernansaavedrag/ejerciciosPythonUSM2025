# Lista de conciertos
conciertos = [
    {
        'ciudad': 'Cairo',
        'publico': 30000,
        'canciones': [
            'If your name is main',
            'Break my heart and return',
            'Strings float around you',
        ]
    },
    {
        'ciudad': 'Moscu',
        'publico': 25000,
        'canciones': [
            'Break my heart and return',
            'Open your mind, close your file',
            'Value error'
        ]
    },
    {
        'ciudad': 'Berlin',
        'publico': 40000,
        'canciones': [
            'If your name is main',
            'Value error',
            'Syntax of love'
        ]
    }
]

# Función a) Cuántas personas escucharon una canción específica
def cuantos_escucharon(c):
    total = 0
    for concierto in conciertos:
        if c in concierto['canciones']:
            total += concierto['publico']
    return total

# Función b) ¿Dos canciones fueron tocadas en el mismo concierto?
def mismo_concierto(c1, c2):
    for concierto in conciertos:
        canciones = concierto['canciones']
        if c1 in canciones and c2 in canciones:
            return True
    return False

# Ejemplos de uso:
print("Personas que escucharon 'Value error':", cuantos_escucharon('Value error'))
print("¿'Break my heart and return' y 'Value error' fueron tocadas juntas?:", mismo_concierto('Break my heart and return', 'Value error'))
print("¿'If your name is main' y 'Syntax of love' fueron tocadas juntas?:", mismo_concierto('If your name is main', 'Syntax of love'))
