# Challenge Técnico #1
## Web Scraping con Python y BeautifulSoup

#### Sitio: https://super.walmart.com.mx/all-departments

## Librerías utilizadas
- `Requests`: Para el acceso al sitio web.
- `BeautifulSoup`:  para la manipulación de contenido ***html***.
- `json`: Para la generación de contenido estructurado `JSON`.
- `Pandas`: Para la visualización de los datos (opcional para uso con **Jupyter Notebook**).

## Detalles de ejecución
Al ejecutar las siguiente líneas de código

```python
url = 'https://super.walmart.com.mx/all-departments'
response = requests.get(url)
soup = bs(response.text, 'html.parser')
```
se obtiene la siguiente respuesta:

```html
<html><head>
<title>Access Denied</title>
</head><body>
<h1>Access Denied</h1>

You don't have permission to access "http://super.walmart.com.mx/all-departments" on this server.<p>
Reference #18.8fb53b17.1682492087.16873dff
</p></body>
</html>
```

La cual se puede deber por una restricción de seguiridad del acceso al contenido por parte del sitio.

Al buscar información en foros de ayuda encontré que se puede solucionar agregando un diccionario con información adicional como el `User-Agent` en el parámetro `headers` de la petición del `requests.get()`:

```python
url = 'https://super.walmart.com.mx/all-departments'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299'}
response = requests.get(url, headers=header)
soup = bs(response.text, 'html.parser')
```

## Procedimiento
Una vez solucionado el acceso al sitio se hace una inspección con el `DevTools` para identificar los elementos `tag` y `class` que contienen la información principal solicitada. Los cuales son los `div class="flex flex-column"`.

```python
divs = soup.find_all('div', {'class': 'flex flex-column'})
```

Posteriormente de cada contenedor `div` se extrajo la información del nombre de cada departamento ubicado en el tag `h2 class="ma0"`, y los nombres de las subcategorias del tag `li class="pv1 pv0-m"` de cada contenedor `ul class="pt2 pl0 list"` con el siguiente ciclo `for`:

```python
result = dict()
for div in divs:
    h2 = div.find('h2', {'class': 'ma0'}).text.strip()
    ul = div.find('ul', {'class': 'pt2 pl0 list'})
    lis = ul.find_all('li', {'class': 'pv1 pv0-m'})
    lis_text = [li.text.strip() for li in lis]
    result[h2] = lis_text
```

Se imprime la variable `result` en la linea de comandos y se genera el archivo `JSON` con la función `dump()` de la librería `json`:

```python
print(result)
with open('output.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=4)

```

Al final se obtiene la información estructurada en el archivo `output.json`:

```json
{
    "Abarrotes": [
        "Café, té y sustitutos",
        "Pan y Tortillas Empacados",
        "Cereales y Barras",
        "Galletas",
        "Enlatados y Conservas",
        ...

    ],
    "Lácteos": [
        "Leche",
        "Yogurt",
        "Gelatinas y Postres",
        ...
    ],
    "Frutas y Verduras": [
        "Frutas",
        "Verduras",
        "Orgánicos y Superfoods"
    ],
    ...
    etc
}
```

## Detalles del Challenge
