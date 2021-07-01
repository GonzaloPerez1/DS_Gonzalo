import numpy as np
import random
# Devuelve una orientación aleatoria
'''def orientancion():
    puntcar = ['N', 'S', 'E', 'O']
    azar = np.random.randint(0, 4)
    return (puntcar[azar])
'''
# Devuelve True si puede colocarse sino devuelve false
def colocar_barco(direccion, tablero, fila, columna, tam_barco):
    if direccion == 'N':
        if not((fila - (tam_barco - 1)) < 0) and (tablero[(fila - tam_barco):fila, columna] != "O").any():
            return True
        else:
            return False
    elif direccion == 'S':
        if not(((tam_barco - 1) + fila) >= 10) and (tablero[fila: (fila + tam_barco), columna] != "O").any():
            return True
        else:
            return False
    elif direccion == 'O':
        if not((columna - (tam_barco - 1)) < 0) and (tablero[fila, (columna - tam_barco): columna] != "O").any():
            return True
        else:
            return False
    else:
        if not(((tam_barco - 1) + columna) >= 10) and (tablero[fila, columna:(columna + tam_barco)] != "O").any():
            return True
        else:
            return False
def dibujar_barco(direccion, tam_barco, tablero, fila, columna):
    if direccion == 'N':
        tablero[fila: (fila - tam_barco): -1, columna] = "O"
    elif direccion == 'S':
        tablero[fila: (fila + tam_barco), columna] = "O"
    elif direccion == 'O':
        tablero[fila, columna: (columna - tam_barco): -1] = "O"
    else:
        tablero[fila, columna: (columna + tam_barco)] = "O"
def undir_iniciar_tablero():
    tam_barco = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
    tablero = np.full((10, 10), " ")
    direc = ['N', 'S', 'E', 'O']
    j = 0
    while j < 10:
        salida = True
        while salida:
            random.shuffle(direc)
            i = 0
            fila = np.random.randint(0, 10)
            columna = np.random.randint(0, 10)
            if tablero[fila, columna] != "O":
                while i < 4:
                    if colocar_barco(direc[i], tablero, fila, columna, tam_barco[j]):
                        salida = False
                        break
                    else:
                        i += 1
        dibujar_barco(direc[i], tam_barco[j], tablero, fila, columna)
        j += 1
    print(tablero)
undir_iniciar_tablero()