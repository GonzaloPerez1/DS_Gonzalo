import numpy as np

n = True

# Creamos el tablero del jugador 1
tablero = np.full((10,10), '~')

#Definimos las primeras coordenadas del barco
coordenadas = np.random.randint(0,10, size=2)
fila = coordenadas[0]
columna = coordenadas[1]

#Definimos las diferentes orientaciones que puede tener el barco
orientacion = np.random.choice(list('NSEW'))
