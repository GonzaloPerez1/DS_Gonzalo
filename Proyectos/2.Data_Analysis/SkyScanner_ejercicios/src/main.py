import smtplib
import requests
import pandas as pd

from config import *

url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browsequotes/v1.0/ES/EUR/es-ES/ES-M/UY-MO/2021-07-11"

querystring = {"inboundpartialdate":"2021-08-11"}

headers = {
    'x-rapidapi-key': "6299a9f547mshcc043ac028bfd1cp1cf5a0jsnc250a5dbcae0",
    'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

data = response.json()

quotes = data['Quotes']
carriers = data['Carriers']
places = data['Places']

names = []

for quote in quotes:
    min_price = quote['MinPrice']
    out_date = quote['QuoteDateTime']

for carrier in carriers:
    company = carrier['Name']

for place in places:
    name = place['Name']
    names.append(name)

df = pd.DataFrame([{'out_date': out_date,
                   'flight_company': company,
                   'from': names[1],
                   'to': names[2],
                   'price': min_price}])

try:
    email = """From: %s
            To: %s
            MIME-Version: 1.0
            Content-type: text/html
            Subject: %s

            %s
            """ % (FROM_ADDR, TO_ADDR, "Vuelos", df.to_html())


    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(USERNAME, PASSWORD)
    server.sendmail(FROM_ADDR, TO_ADDR, email.encode('utf-8'))
    server.quit()
except Exception as e:
    print('No se han enviado los correos, Error: ', e)
