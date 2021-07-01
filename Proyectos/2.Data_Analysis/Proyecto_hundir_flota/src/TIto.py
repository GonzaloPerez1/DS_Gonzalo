import numpy as np

#Variables constantes
tablero = np.full((10,10), '~')
eslora = 1
rep_barcos = 4
'''
#Bucle Iniciar_juego
coordenadas = np.random.randint(0,10, size=2)
fila = coordenadas[0]
columna = coordenadas[1]
print(fila, columna)

orientacion = np.random.choice(list('NSEW'))
print(orientacion)
'''

for i in range(rep_barcos):
    coordenadas = np.random.randint(0,10, size=2)
    fila = coordenadas[0]
    columna = coordenadas[1]
    print(fila, columna)

    orientacion = np.random.choice(list('NSEW'))
    print(orientacion)
    Norte = tablero[fila:(fila - eslora):-1, columna]
    Sur = tablero[fila:(fila + eslora), columna]
    Este = tablero[fila, columna :(columna + eslora)]
    Oeste = tablero[fila, columna :(columna - eslora):-1]
    print(i)
    if (orientacion == 'N') and (len(Norte) == eslora) and ('O' not in Norte):
        tablero[fila:(fila - eslora):-1, columna] = 'O'
    elif (orientacion == 'S') and (len(Sur) == eslora) and ('O' not in Sur):
        tablero[fila:(fila + eslora), columna] = 'O'
    elif (orientacion == 'E') and (len(Este) == eslora) and ('O' not in Este):
        tablero[fila, columna :(columna + eslora)] = 'O'
    elif (orientacion == 'W') and (len(Oeste) == eslora) and ('O' not in Oeste):
        tablero[fila, columna :(columna - eslora):-1] = 'O'


print(tablero)




