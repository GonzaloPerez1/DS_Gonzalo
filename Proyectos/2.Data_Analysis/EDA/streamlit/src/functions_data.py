'''
En este script encontraremos las funciones necesarias para hacer
busquedas de datos en la BBDD (SQLite) a través de Python.

@author: Gonzalo Pérez Díez.
'''

import sqlite3
import pandas as pd

def comunidades_cama_habitante():
    #Iniciamos la conexión con la base de datos
    conn = sqlite3.connect('database_eda')

    query='''
    SELECT H.COMUNIDAD_AUTONOMA, SUM(H.NUMERO_DE_CAMAS) AS NUMERO_CAMAS, P.POBLACION
    FROM HOSPITALES H
    JOIN POBLACION P ON H.COMUNIDAD_AUTONOMA = P.COMUNIDAD_AUTONOMA
    GROUP BY H.COMUNIDAD_AUTONOMA;
    '''

    df = pd.read_sql_query(query, conn)

    #Cerramos la conexión con la base de datos
    conn.close()

    df['CAMAS_1000_HABITANTES'] = (df['NUMERO_CAMAS']/df['POBLACION'])*1000
    df = df.sort_values(by='CAMAS_1000_HABITANTES', ascending=False)

    return df

def gasto_comunidad():
    conn = sqlite3.connect('database_eda')

    query='''
    SELECT G.COMUNIDAD_AUTONOMA, G.GASTO_SANIDAD, P.POBLACION
    FROM GASTO_SANIDAD G
    JOIN POBLACION P ON G.COMUNIDAD_AUTONOMA = P.COMUNIDAD_AUTONOMA
    GROUP BY G.COMUNIDAD_AUTONOMA;
    '''

    df = pd.read_sql_query(query, conn)

    conn.close()

    df['GASTO_HABITANTE'] = df['GASTO_SANIDAD']/df['POBLACION']
    df = df.sort_values(by='GASTO_HABITANTE', ascending=False)

    return df

def rel_camas_gasto():
    conn = sqlite3.connect('database_eda')

    query='''
    SELECT H.COMUNIDAD_AUTONOMA, SUM(H.NUMERO_DE_CAMAS) AS NUMERO_CAMAS, G.GASTO_SANIDAD, P.POBLACION
    FROM HOSPITALES H
    JOIN GASTO_SANIDAD G ON H.COMUNIDAD_AUTONOMA = G.COMUNIDAD_AUTONOMA
    JOIN POBLACION P ON H.COMUNIDAD_AUTONOMA = P.COMUNIDAD_AUTONOMA
    GROUP BY H.COMUNIDAD_AUTONOMA;
    '''

    df = pd.read_sql_query(query, conn)

    conn.close()

    df['CAMAS_1000_HABITANTES'] = (df['NUMERO_CAMAS']/df['POBLACION'])*1000
    df['GASTO_HABITANTE'] = df['GASTO_SANIDAD']/df['POBLACION']

    return df

def rel_maquina_gasto():
    conn = sqlite3.connect('database_eda')

    query = '''
    SELECT E.*, G.GASTO_SANIDAD, P.POBLACION
    FROM EQUIPO_MEDICO E
    JOIN GASTO_SANIDAD G ON E.COMUNIDAD_AUTONOMA = G.COMUNIDAD_AUTONOMA
    JOIN POBLACION P ON E.COMUNIDAD_AUTONOMA = P.COMUNIDAD_AUTONOMA
    GROUP BY E.COMUNIDAD_AUTONOMA;
    '''

    df = pd.read_sql_query(query, conn)

    conn.close()

    df['TOTAL_MAQUINAS'] = df.loc[:, 'TAC':'DIAL'].sum(axis=1)
    df['MAQUINA_HABITANTE'] = df['TOTAL_MAQUINAS']/df['POBLACION']
    df['GASTO_HABITANTE'] = df['GASTO_SANIDAD']/df['POBLACION']
    df = df[['COMUNIDAD_AUTONOMA',
          'GASTO_SANIDAD',
          'POBLACION',
          'TOTAL_MAQUINAS',
          'MAQUINA_HABITANTE',
          'GASTO_HABITANTE']]

    return df

def rel_pib_gasto():
    conn = sqlite3.connect('database_eda')

    query = '''
    SELECT PI.*, G.GASTO_SANIDAD, P.POBLACION, ROUND(CAST(PI.PIB AS FLOAT)/CAST(P.POBLACION AS FLOAT), 5) AS PIB_PER_CAPITA,
        ROUND(CAST(G.GASTO_SANIDAD AS FLOAT)/CAST(P.POBLACION AS FLOAT), 5) AS GASTO_HABITANTE
    FROM PIB PI
    JOIN POBLACION P ON PI.COMUNIDAD_AUTONOMA = P.COMUNIDAD_AUTONOMA
    JOIN GASTO_SANIDAD G ON P.COMUNIDAD_AUTONOMA = G.COMUNIDAD_AUTONOMA
    GROUP BY PI.COMUNIDAD_AUTONOMA;
    '''

    df = pd.read_sql_query(query, conn)

    conn.close()

    return df
