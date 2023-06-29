import csv
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Descargar stopwords en inglés y español
nltk.download('stopwords')
nltk.download('punkt')

# Obtener las stopwords en inglés y español
english_stopwords = set(stopwords.words('english'))
spanish_stopwords = set(stopwords.words('spanish'))

# Función para generar los tokens únicos de un texto sin stopwords y números
def generate_tokens(text):
    tokens = set(word_tokenize(text))
    tokens_without_stopwords = [token for token in tokens if token.lower() not in english_stopwords and token.lower() not in spanish_stopwords and not re.search(r'\d', token)]
    return tokens_without_stopwords

# Ruta del archivo CSV de entrada y salida
input_file = 'post_data.csv'
output_file = 'tokens_data.csv'

# Leer el archivo CSV de entrada y obtener los tokens sin stopwords y números para cada post
tokens = set()
with open(input_file, 'r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Leer la primera fila (encabezados de columna)
    for row in reader:
        post = row[0]  # Obtener el texto del post en la primera columna
        post_tokens = generate_tokens(post)
        tokens.update(post_tokens)  # Agregar los tokens al conjunto de tokens

# Escribir los tokens en el archivo CSV de salida
with open(output_file, 'w', newline='') as file:
    writer = csv.writer(file)
    for token in tokens:
        writer.writerow([token])

