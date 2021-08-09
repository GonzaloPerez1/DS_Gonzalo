'''
En este script podemos encontrar las funciones que contienen toda la estructura de la página,
desde la página de inicio hasta las gráficas con las conclusiones.

@author: Gonzalo Pérez Díez
'''

import seaborn as sns
import streamlit as st
import plotly.express as px
import functions_data as fd
import function_graphs as fg
import functions_utils as fu
import matplotlib.pyplot as plt

########################################################### HOME ################################################################

def main_page():
    st.title('Hospitales en España')
    st.image(fu.Imagen_inicial, caption='Hospital Ramón y Cajal')

def eda_description():
    st.markdown('''
    ## **Proyecto EDA**
    ''')
    st.markdown('''
    A continuación se expondrá de forma clara y sencilla el Análisis Exploratorio de Datos realizado como \
        ejercicio en el Bootcamp de Data Science en The Bridge. \n
    En este trabajo se estudiará si el reparto de medios sanitarios (número de camas, equipo médico, gasto sanitario) \
        es óptimo o si la distribución es irregular.
    ''')
    st.markdown('''
    ## Teorías a comprobar
    1. ¿Qué comunidades tienen más camas por habitante?
    2. ¿Qué comunidades gastan más en sanidad por habitante?
    3. ¿Hay relación entre el PIB y el gasto en sanidad?
    4. ¿Hay relación entre el número de camas en hospitales y la inversión por Comunidad Autónoma?
    5. ¿Hay relación entre el gasto en sanidad y el número de maquinaria médica?
    ''')
    st.markdown('''
    ### Links de donde se ha extraido la información
    - [url_datos_hospitales](https://www.mscbs.gob.es/ciudadanos/centrosCA.do)
    - [url_gasto_sanidad](https://www.mscbs.gob.es/estadEstudios/estadisticas/inforRecopilaciones/docs/presupuestosIniciales.pdf)
    - [url_población](https://es.wikipedia.org/wiki/Anexo:Comunidades_y_ciudades_aut%C3%B3nomas_de_Espa%C3%B1a)
    - [url_PIB](https://datosmacro.expansion.com/pib/espana-comunidades-autonomas)
    ''') #Colocamos los enlaces utilizados

    with st.beta_expander('Author'):
        st.markdown('''
        ## **Gonzalo Pérez Díez**\n
        ''')

########################################################### DATA ###############################################################

def datasets_description():
    st.title('Datasets')
    st.markdown('''
    A lo largo del proyecto utilizaremos cinco datasets que incorporaremos a una base de datos (SQLite) para \
        poder recoger la información con mayor facilidad.\n
    Toda la información recogida es del año 2019, además no se han tenido en cuenta ciertas características econónomicas \
        propias de ciertas Comunidades Autónomas, como País Vasco.\n
    Los datos son:\n
    - **Catálogo de hospitales**:  contiene los identificadores, nombres, \
    direcciones, número de camas y demás datos relevantes sobre los hospitales de todo el país.
    - **Equipo Médico**: contiene el número de máquinas sanitarias que posee cada comunidad autónoma.
    - **Gasto en sanidad**: contiene la cantidad de dinero asignado a cada comunidad autónoma en lo relacionado a la sanidad.
    - **Población por Comunidad Autónoma**: contiene el número de personas y la superficie de cada comunidad autónoma.
    - **PIB por Comunidad Autónoma**: valor del producto interior bruto de cada comunidad autónoma
    ''')
    with st.beta_expander('Saber más sobre el Equipo Médico.'):
        st.markdown('''
        - **TAC**: Tomografía Axial Computerizada
        - **RM**: Resonancia Magnética
        - **GAM**: Gammagrafía
        - **HEM**: Sala de Hemodinámica
        - **ASD**: Angiografía por Sustracción Digital
        - **LIT**: Litotricia Extracorporea por Ondas de Choque
        - **BCO**: Bomba de Cobalto
        - **ALI**: Acelerador Lineal de Partículas
        - **SPECT**: Tomografía por emisión de fotones
        - **PET**: Tomografía por emisión de positrones
        - **MAMOS**: Mamógrafo
        - **DO**: Densitómetros Óseos
        - **DIAL**: Equipos de Hemodiálisis

        Cataluña: Los datos de gammagrafía incluyen SPECT
        ''')

def show_datasets():
    st.markdown('## Headers de los datasets')

    st.write('Catálogo de Hospitales')
    st.dataframe(fu.catalogo_hospitales.head())

    st.write('Equipo médico')
    st.dataframe(fu.equipo_medico.head())

    st.write('Población, superficie y densidad de población en 2019')
    st.dataframe(fu.popu_sup.head())

    st.write('Gasto en sanidad en 2019')
    st.dataframe(fu.gasto_sanidad.head())

    st.write('PIB por Comunidad Autónoma en 2019')
    st.dataframe(fu.pib_ccaa.head())

######################################################## GRAPHS #################################################################

def cama_habitante_ccaa():
    df = fd.comunidades_cama_habitante()

    fig = px.bar(
        df,
        x = 'COMUNIDAD_AUTONOMA',
        y = 'CAMAS_1000_HABITANTES',
        height = 500,
        width = 1300,
        hover_data = ['COMUNIDAD_AUTONOMA', 'CAMAS_1000_HABITANTES']
    )

    st.plotly_chart(fig)

def gasto_ccaa():
    df = fd.gasto_comunidad()

    fig = px.bar(
        df,
        x = 'COMUNIDAD_AUTONOMA',
        y = 'GASTO_HABITANTE',
        height = 500,
        width = 1300,
        hover_data = ['COMUNIDAD_AUTONOMA', 'GASTO_HABITANTE']
    )

    st.plotly_chart(fig)

def relacion_camas_gasto():
    df = fd.rel_camas_gasto()

    fig, ax = plt.subplots()

    sns.heatmap(df.corr(),
        ax = ax,
        vmin = -1,
        vmax = 1,
        annot=True, #Introduzco los números dentro de cada recuadro
        square = True, #Obtengo cuadrados en vex de rectángulos
        linewidths = .5, #Margen entre cuadrados
        cmap=sns.diverging_palette(150, 277, s=100, l=30, n=13))

    st.write(fig)

def relacion_maquinas_gasto():
    df = fd.rel_maquina_gasto()

    fig, ax = plt.subplots()

    sns.heatmap(df.corr(),
        ax = ax,
        vmin = -1,
        vmax = 1,
        annot=True, #Introduzco los números dentro de cada recuadro
        square = True, #Obtengo cuadrados en vex de rectángulos
        linewidths = .5, #Margen entre cuadrados
        cmap=sns.diverging_palette(150, 277, s=100, l=30, n=13))

    st.write(fig)

def relacion_pib_gasto():
    df = fd.rel_pib_gasto()

    fig, ax = plt.subplots()

    sns.heatmap(df.corr(),
        ax = ax,
        vmin = -1,
        vmax = 1,
        annot=True, #Introduzco los números dentro de cada recuadro
        square = True, #Obtengo cuadrados en vex de rectángulos
        linewidths = .5, #Margen entre cuadrados
        cmap=sns.diverging_palette(150, 277, s=100, l=30, n=13))

    st.write(fig)

def visualizar_graficos():
    st.title('Número de camas por cada 1000 habitantes por Comunidad Autónoma')
    fg.cama_habitante_ccaa()
    st.title('Gasto en sanidad por habitante por Comunidad Autónoma')
    fg.gasto_ccaa()
    st.title('Relación entre el número de camas en hospitales y el gasto en sanidad por Comunidad Autónoma')
    fg.relacion_camas_gasto()
    st.title('Relación entre el número de equipo médico y el gasto en sanidad por Comunidad Autónoma')
    fg.relacion_maquinas_gasto()
    st.title('Relación entre el PIB y el gasto en sanidad por Comunidad Autónoma')
    fg.relacion_pib_gasto()
    st.title('Conclusiones')
    with st.beta_expander('Conclusiones.'):
        st.markdown('''
        - El reparto de los medios expuestos anteriormente ha sido pensando en la importancia \
            de cada Comunidad Autónoma, no se ha tenido en cuenta el número de habitantes en cada una.
        - Cuanta más población tenga una Comunidad Autónoma, menor dinero recibe cada ciudadano, \
            rebajando la calidad de atención al paciente.
        - La distribución de los medios actual no es óptima, la prueba es que durante un periodo de pandemia \
            (COVID-19) se han colapsado la mayoría de hospitales, indistintamente de la comunidad donde estuviesen.
        ''')