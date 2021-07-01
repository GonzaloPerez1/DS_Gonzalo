import numpy as np

n = True

# Creamos el tablero del jugador 1
tablero = np.full((10,10), '~')

#Definimos las primeras coordenadas del barco
coordenadas = np.random.randint(0,10, size=2)
fila = coordenadas[0]
columna = coordenadas[1]

#Listas barcos
eslora_4 = [4]
eslora_3 = [3,3]
eslora_2 = [2,2,2]
eslora_1 = [1,1,1,1]

#Listas de eslora
eslora = [eslora_1, eslora_2, eslora_3, eslora_4]