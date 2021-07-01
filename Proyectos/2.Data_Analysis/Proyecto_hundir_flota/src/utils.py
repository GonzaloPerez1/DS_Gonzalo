import numpy as np

from constants import *

print(fila, columna)
print(orientacion)

def pintar_barco(fila, columna, eslora, rep_barcos):
    while rep_barcos != 0:
        Norte = tablero[fila:(fila - eslora):-1, columna]
        Sur = tablero[fila:(fila + eslora), columna]
        Este = tablero[fila, columna :(columna + eslora)]
        Oeste = tablero[fila, columna :(columna - eslora):-1]

        if (orientacion == 'N') and (len(Norte) == eslora) and ('O' not in Norte):
            tablero[fila:(fila - eslora):-1, columna] = 'O'
        elif (orientacion == 'S') and (len(Sur) == eslora) and ('O' not in Sur):
            tablero[fila:(fila + eslora), columna] = 'O'
        elif (orientacion == 'E') and (len(Este) == eslora) and ('O' not in Este):
            tablero[fila, columna :(columna + eslora)] = 'O'
        elif (orientacion == 'W') and (len(Oeste) == eslora) and ('O' not in Oeste):
            tablero[fila, columna :(columna - eslora):-1] = 'O'
        rep_barcos -= 1

def iniciar_juego():
    numero_barcos = 0
    while numero_barcos < 10:
        coordenadas = np.random.randint(0,10, size=2)
        fila = coordenadas[0]
        columna = coordenadas[1]
        if numero_barcos == 0:
            pintar_barco(fila, columna, 4, 1)
        elif numero_barcos in [1,2]:
            pintar_barco(fila, columna, 3, 2)
        elif numero_barcos in [3,4,5]:
            pintar_barco(fila, columna, 2, 3)
        elif numero_barcos in [6,7,8,9]:
            pintar_barco(fila, columna, 1, 4)
        numero_barcos += 1
    print(tablero)