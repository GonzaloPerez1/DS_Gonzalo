# Importamos las librerías
import pygame
import time
import numpy as np

# Iniciar pantalla
pygame.init()

# Tamaño de la pantalla
width, height = 1600, 1600
screen = pygame.display.set_mode((width, height))

# Color de fondo(Casi negro)
bg = 25, 25, 25

screen.fill(bg)

#Especificar las celdas
nxC, nyC = 150, 150

#Tamaño de las celdas
dimCW = width / nxC
dimCH= height / nyC

# Estado de las celdas (Vivas = 1, Muertas = 0)
gameState = np.zeros((nxC, nyC))

# Estado inicial(Autómata móvil)
gameState[21,21] = 1
gameState[22,22] = 1
gameState[22,23] = 1
gameState[21,23] = 1
gameState[20,23] = 1

pauseExect = False

# Bucle de ejecución
while True:

    newGameState = np.copy(gameState)

    screen.fill(bg)

    time.sleep(0.1)

    ev = pygame.event.get()

    for event in ev:
        if event.type == pygame.KEYDOWN:
            pauseExect = not pauseExect

        mouseClick = pygame.mouse.get_pressed()
        if sum(mouseClick) > 0:
            posX, posY = pygame.mouse.get_pos()
            celX, celY = int(np.floor(posX/dimCW)), int(np.floor(posY/dimCH))
            newGameState[celX, celY] = not mouseClick[2]

    for y in range(0, nxC):
        for x in range(0, nyC):

            if not pauseExect:

                n_neigh = gameState[(x-1) % nxC,(y-1) % nyC] + \
                        gameState[(x) % nxC, (y-1) % nyC] + \
                        gameState[(x+1) % nxC, (y-1) % nyC] + \
                        gameState[(x-1) % nxC, (y) % nyC] + \
                        gameState[(x+1) % nxC, (y) % nyC] + \
                        gameState[(x-1) % nxC, (y+1) % nyC] + \
                        gameState[(x) % nxC, (y+1) % nyC] + \
                        gameState[(x+1) % nxC, (y+1) % nyC]

                # Regla 1: Una celula muerta con exactamente 3 vecinas vivas: 'Vive'
                if gameState[x, y] == 0 and n_neigh == 3:
                    newGameState[x, y] = 1

                # Regla 2: Una celula viva con 2 o más de 3 vecinas vivas: 'Muertas'
                elif gameState[x, y] == 1 and (n_neigh < 2 or n_neigh > 3):
                    newGameState[x, y] = 0

            poly = [(x * dimCW, y * dimCH),
                    ((x+1) * dimCW, y * dimCH),
                    ((x+1) * dimCW, (y+1) * dimCH),
                    (x * dimCW, (y+1) * dimCH)]

            # Dibunamos celdas
            if newGameState[x,y] == 0:
                pygame.draw.polygon(screen, (128, 128,128), poly, 1)
            else:
                pygame.draw.polygon(screen, (255,255,255), poly, 0)

    gameState = np.copy(newGameState)

    pygame.display.flip()