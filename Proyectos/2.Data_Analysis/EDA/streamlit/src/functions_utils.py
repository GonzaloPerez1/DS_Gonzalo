'''
En este script encontramos los datos importados de los archivos csv y la imagen que encabeza
el trabajo.

@author: Gonzalo Pérez Díez
'''

import pandas as pd
from PIL import Image

#Imagen de cabecera de la presentación
Imagen_inicial = Image.open('./img/hospital-universitario-ramon-y-cajal.jpeg')

#Datasets, solo lo usaremos para visualizar los datos
catalogo_hospitales = pd.read_csv('./data/catalogo_hospitales.csv')
equipo_medico = pd.read_csv('./data/Equipo_Médico.csv', sep='\t')
gasto_sanidad = pd.read_csv('./data/gasto_sanidad_ccaa_2019.csv', sep=';')
popu_sup = pd.read_csv('./data/pop_sup_2019.csv', sep=';')
pib_ccaa = pd.read_csv('./data/pib_ccaa_2019.csv', sep=';')