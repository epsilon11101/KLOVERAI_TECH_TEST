import csv
import re
import requests
from bs4 import BeautifulSoup

def remove_emoji(string):
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)

# URL de la página a scrapear
url = 'https://www.reddit.com/'

# Realizar la solicitud HTTP GET a la página
response = requests.get(url)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Crear un objeto BeautifulSoup a partir del contenido HTML
    soup = BeautifulSoup(response.content, 'html.parser')

    # Encontrar todos los elementos <a> que contengan los títulos de los posts
    post_links = soup.find_all('h3')

    # Listas para almacenar los títulos de los posts y los comentarios
    posts = []
    comentarios = []

    # Iterar sobre los enlaces y obtener el texto del título y los comentarios de cada post
    for link in post_links:
        post_title = link.text

        # Normalizar el título del post y eliminar espacios en blanco
        post_title = ' '.join(post_title.lower().split())

        # Eliminar caracteres especiales y emojis del título
        post_title = re.sub(r'[^\w\s]+', '', post_title)  # Eliminar caracteres especiales
        post_title = remove_emoji(post_title)  # Eliminar emojis

        # Encontrar los elementos <span> que contienen los comentarios
        comment_span = link.find_next('span', string=lambda text: text and 'comentarios' in text.lower())

        if comment_span:
            # Obtener el texto de los comentarios
            comments_text = comment_span.text.strip()

            # Extraer el número de comentarios utilizando expresiones regulares
            comments_count = re.search(r'\d+', comments_text).group()

            # Agregar el título del post y los comentarios a las listas correspondientes
            posts.append(post_title)
            comentarios.append(comments_count)
        else:
            # Si no se encontraron comentarios, se agrega el título del post con 0 comentarios
            posts.append(post_title)
            comentarios.append('0')

    # Ordenar las listas de posts y comentarios en función de los comentarios (de mayor a menor)
    posts, comentarios = zip(*sorted(zip(posts, comentarios), key=lambda x: int(x[1]), reverse=True))

    # Abrir un archivo CSV en modo escritura
    with open('post_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        # Escribir encabezados de columna
        writer.writerow(['Input', 'Output'])

        # Iterar sobre las listas de posts y comentarios y escribir los datos en el archivo CSV
        for post, comment in zip(posts, comentarios):
            writer.writerow([post, comment])

else:
    print('Error al obtener la página:', response.status_code)
