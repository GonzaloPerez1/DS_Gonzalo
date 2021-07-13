import smtplib
from urllib.request import urlopen
from xml.etree.ElementTree import parse

from constants import *

lista_periodicos = [URL_EL_CONFIDENCIAL, URL_EXPANSION, URL_5_DIAS, URL_EL_ECONOMISTA]

for i in range(len(lista_periodicos)):
    var_url = urlopen(lista_periodicos[i])
    xmldoc = parse(var_url)

    for item in xmldoc.findall('./channel/item'):
        titulos = item.findtext('title')
        link_noticia = item.findtext('link')
        if 'amazon' in titulos.lower():
            try:
                email = """From: %s
                        To: %s
                        MIME-Version: 1.0
                        Content-type: text/html
                        Subject: %s

                        %s
                        """ % (FROM_ADDR, TO_ADDR, titulos, link_noticia)


                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(USERNAME, PASSWORD)
                server.sendmail(FROM_ADDR, TO_ADDR, email.encode('utf-8'))
                server.quit()
            except Exception as e:
                print('No se han enviado los correos, Error: ', e)

