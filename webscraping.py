from bs4 import BeautifulSoup as bs
import requests
import json

#%% Preparación de Datos

# Designamos la url del sitio
url = 'https://super.walmart.com.mx/all-departments'

# Agregamos la información de los headers para evitar el acceso denegado al sitio
header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

# Generamos la petición al sitio
respuesta = requests.get(url, headers=header)

# Extraemos el contedio html del sitio
soup = bs(respuesta.content, 'html.parser')

dep_box = soup.find_all('div', class_='h-100 relative')

dep_box

title = dep_box.find('h1').get_text()
title
