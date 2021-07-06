import time
import numpy as np

from constants import *

def pintar_barco(eslora, tablero):
    while True:
        orientacion = np.random.choice(list('NSEW'))

        coordenadas = np.random.randint(0,10, size=2)
        fila = coordenadas[0]
        columna = coordenadas[1]

        Norte = tablero[fila:(fila - eslora):-1, columna]
        Sur = tablero[fila:(fila + eslora), columna]
        Este = tablero[fila, columna :(columna + eslora)]
        Oeste = tablero[fila, columna :(columna - eslora):-1]

        if (orientacion == 'N') and (len(Norte) == eslora) and ('O' not in Norte):
            tablero[fila:(fila - eslora):-1, columna] = 'O'
            break
        elif (orientacion == 'S') and (len(Sur) == eslora) and ('O' not in Sur):
            tablero[fila:(fila + eslora), columna] = 'O'
            break
        elif (orientacion == 'E') and (len(Este) == eslora) and ('O' not in Este):
            tablero[fila, columna :(columna + eslora)] = 'O'
            break
        elif (orientacion == 'W') and (len(Oeste) == eslora) and ('O' not in Oeste):
            tablero[fila, columna :(columna - eslora):-1] = 'O'
            break
'''
Mirar si nos combiene hacer una función para la lógica de disparos y llamarla
en disparo_bot y disparo_jugador
'''

def disparo_bot():
    continua_ejec_bot = True
    while continua_ejec_bot:

        disparo_fila_bot = np.random.randint(1, 10)
        disparo_colum_bot = np.random.randint(1, 10)

        if (tablero_juego[disparo_fila_bot, disparo_colum_bot] == '~'):
            tablero_juego[disparo_fila_bot, disparo_colum_bot] = '#'
            print('Tablero jugador 1: \n', tablero_juego)
            continua_ejec_bot = False
        elif (tablero_juego[disparo_fila_bot, disparo_colum_bot] == 'O'):
            tablero_juego[disparo_fila_bot, disparo_colum_bot] = 'X'
            print('Tablero jugador 1: \n', tablero_juego)
            time.sleep(0.5)
            continue
        elif (tablero_juego[disparo_fila_bot, disparo_colum_bot] == '#'):
            print('Tablero jugador 1: \n', tablero_juego)
            print('Has fallado')
        elif (tablero_juego_maquina[disparo_fila_bot, disparo_colum_bot] == 'X'):
            continue
        else:
            continua_ejec_bot = False

    disparo_jugador()

def disparo_jugador():
    continua_ejecucion = True
    while continua_ejecucion:

        disparo_fila = int(input("¿Dónde te gustaría atacar? Elige la fila:\n"))
        disparo_colum = int(input("Ahora alige la columna\n"))

        if (0 > disparo_fila > 10) or (0 > disparo_colum > 10):
            print("Tus coordenadas son incorrectas :/ Introduce valores del 1 al 10!")
            #return disparo_jugador()
        elif (tablero_juego_maquina[disparo_fila, disparo_colum] == '#'): #Comprobar como hacerlo par aque no salga al fallar el tiro
            print("Ya has disparado aquí, zoquetx!")
            continue
            #return disparo_jugador()
        elif (tablero_juego_maquina[disparo_fila, disparo_colum] == '~'):
            tablero_juego_maquina[disparo_fila, disparo_colum] = '#'
            tablero_guia[disparo_fila, disparo_colum] = '#'
            print("Tu disparo ha caído al agua! :(")
            print(tablero_guia)
            continua_ejecucion = False
        elif (tablero_juego_maquina[disparo_fila, disparo_colum] == 'O'):
            tablero_juego_maquina[disparo_fila, disparo_colum] = 'X'
            tablero_guia[disparo_fila, disparo_colum] = 'X'
            print("Le has dado a un barco de tu rival!")
            print(tablero_guia)
            continue
        elif (tablero_juego_maquina[disparo_fila, disparo_colum] == 'X'):
            print('Ya has disparado aquí')
            continue
        else:
            print("Has acabado tu turno.")
            continua_ejecucion = False

    disparo_bot()


def comprobacion():
    print('Empieza el juego.')
    disparo_jugador()

    condicion = True
    while condicion:
        if 'O' in tablero_juego:
            return disparo_bot()
        elif 'O' in tablero_juego_maquina:
            return disparo_jugador()
        else:
            condicion = False
            return False

def nueva_partida():
    juego_nuevo = input("¿Te gustaría volver a jugar? Introduce PLAYAGAIN para jugar de nuevo o cualquier tecla para salir")
    if juego_nuevo == 'PLAYAGAIN':
        return iniciar_juego()
    elif juego_nuevo == 'DATA':
        print("Vámonos al beercamp con Tito") #EASTEREGG
    else:
        print("Gracias por jugar al Hundir la Flota de Gonzalo y Rafa!")
        return False

def iniciar_juego():
    numero_barcos = 0
    while numero_barcos < 10:
        if numero_barcos == 0:
            pintar_barco(4, tablero_juego)
            pintar_barco(4, tablero_juego_maquina)
        elif numero_barcos in [1,2]:
            pintar_barco(3, tablero_juego)
            pintar_barco(3, tablero_juego_maquina)
        elif numero_barcos in [3,4,5]:
            pintar_barco(2, tablero_juego)
            pintar_barco(2, tablero_juego_maquina)
        elif numero_barcos in [6,7,8,9]:
            pintar_barco(1, tablero_juego)
            pintar_barco(1, tablero_juego_maquina)
        numero_barcos += 1

    print('Tablero del jugador 1 \n',tablero_juego)
    comprobacion()
    if comprobacion == False:
        nueva_partida()
        if nueva_partida == False:
            exit
