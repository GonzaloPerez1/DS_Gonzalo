import pandas as pd
from selenium import webdriver

from selenium.webdriver.firefox.options import Options

def get_driver():
    # Especificamos la ruta del driver para hacer web scrapping
    driver = '/home/gonzalo/Documentos/Data_Science/geckodriver-web_scrapping/geckodriver'
    # Importamos las opciones para firefox
    options = Options()
    # Cancelamos el despliegue de la ventana de firefox
    options.headless = True

    # Definimos el driver
    driver = webdriver.Firefox(executable_path = driver, options = options)

    url = 'https://www.filmaffinity.com'
    driver.get(url)
    return driver

def adds():
    '''
    Función para aceptar la primera ventana emergente que sale
    '''
    driver = get_driver()
    elements_by_tag = driver.find_elements_by_tag_name('button')
    boton_aceptar = elements_by_tag[2]
    boton_aceptar.click()

def scrapping():
    '''
    Sacamos los datos para el dataset
    '''
    driver = get_driver()
    contenedor = driver.find_element_by_id('lsmenu')
    cont2 = contenedor.find_elements_by_class_name('cat-container')
    for menus in cont2:
        if menus.find_element_by_tag_name('div').text == 'España':
            sub_menu = menus

    sub_menu
    contenedor_3 = sub_menu.find_elements_by_tag_name('a')
    for i in contenedor_3:
        if i.text == 'Próximos estrenos':
            enlace = i.get_attribute('href')

    driver.get(enlace)
    list_title = []
    pelis = driver.find_elements_by_id('main-wrapper-rdcat')
    for dias in pelis:
        if dias.find_element_by_tag_name('div').get_attribute('class') == 'rdate-cat rdate-cat-first':
            conjunto = dias

    enlaces_pelis = []
    dataframe = []
    conjunto
    contenedor_4 = conjunto.find_elements_by_class_name('top-movie')
    for link in contenedor_4:
        enlace = link.find_element_by_tag_name('a').get_attribute('href')

        enlaces_pelis.append(enlace)

    for enlace in enlaces_pelis:
        driver.get(enlace)

        list_title = []
        pelicula = driver.find_element_by_id('main-title')
        titulo = pelicula.find_element_by_tag_name('span').text
        list_title.append(titulo)

        info = driver.find_element_by_class_name('movie-info')
        cuerpo = info.find_elements_by_tag_name('dd')
        cuerpo_2 = info.find_elements_by_tag_name('dt')
        dd = []
        dt = []
        for contenido in cuerpo:
            dd.append(contenido.text)
        for nombres in cuerpo_2:
            dt.append(nombres.text)

        dataframe.append(pd.DataFrame([dd], columns=dt, index=list_title))

    return dataframe

def data():
    dataframe = scrapping()
    df1 = [df.reset_index() for df in dataframe]
    df2 = pd.concat(df1, axis=0)
    df_nuevo = df2.rename(columns={'index': 'Titulo'})
    df_nuevo = df_nuevo.set_index('Titulo')
    return df_nuevo
