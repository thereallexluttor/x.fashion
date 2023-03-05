import requests
from bs4 import BeautifulSoup
import os

# la URL de la sección de "últimas tendencias" de Vogue
url = "https://www.vogue.com/fashion/trends"

# enviar una solicitud GET a la página web y analizar el HTML con BeautifulSoup
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

print(soup)

# encontrar todas las imágenes en la página y descargarlas
for img in soup.find_all('img'):
    # obtener la URL de la imagen
    img_url = img.get('src')
    # asegurarse de que la URL de la imagen es válida
    if img_url and img_url.startswith("http"):
        # descargar la imagen y guardarla en un archivo
        img_data = requests.get(img_url).content
        filename = os.path.basename(img_url)
        with open(filename, 'wb') as f:
            f.write(img_data)