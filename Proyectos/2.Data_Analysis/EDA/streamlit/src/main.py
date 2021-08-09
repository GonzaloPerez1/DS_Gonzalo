'''
Cuerpo del streamlit

@author: Gonzalo Pérez Díez
'''

import streamlit as st
import function_graphs as fg

st.sidebar.title('MAIN MENU')
menu = st.sidebar.selectbox('Selection Menu',('Home','Data','Graphs'))

if menu == 'Home':
    fg.main_page()
    fg.eda_description()

if menu == 'Data':
    fg.datasets_description()
    fg.show_datasets()

if menu == 'Graphs':
    fg.visualizar_graficos()