from os import sep
import pandas as pd
import function_utils as fu

# Importamos las muertes por causas
deaths_cases = pd.read_csv('./data/number-of-deaths-by-risk-factor.csv', sep=',')

# Importamos los datos de la población por paises
ISO2 = pd.read_csv('./data/mundial_population.csv')
pop = ISO2.T

# Hemos pasado los países a un excel para traducirlos a inglés
country = pd.read_excel('./data/translate_country.xlsx', usecols='C')
years = pop.loc['1990':'2017']

lista_con= country.values.tolist()

popu = pd.DataFrame(years)
lista_fin = []
for i in lista_con:
    lista_fin.extend(i)

popu.columns = lista_fin
print(popu.head())
print(deaths_cases.head())

#population = pd.DataFrame(data=years)
#print(country)
#population = population.T
#population['Entity'] = country

#population['Entity'].to_excel('ejemplo.xlsx', sheet_name='hoja_1')

#print(deaths_cases['Entity'].nunique())
#print(population.index.nunique())

#Imprimimos la información del dataset (cantidad de columnas, valores nulos, tipo de datos)
#print(deaths_cases.head())
#print(population.head())
