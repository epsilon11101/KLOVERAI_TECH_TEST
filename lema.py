import csv
import spacy

# Ruta del archivo CSV de entrada y salida
input_file = 'tokens_data.csv'
output_file = 'lemmatized_tokens.csv'

# Cargar el modelo de SpaCy para el idioma español
nlp_es = spacy.load('es_core_news_sm')

# Lista para almacenar los tokens y los lemas
data = []

# Leer el archivo CSV de entrada y realizar la lematización de los tokens
with open(input_file, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        token = row[0]  # Obtener el token en la primera columna
        
        # Realizar la lematización del token
        doc = nlp_es(token)
        
        # Obtener el lema del token
        lemma = doc[0].lemma_

        data.append([token, lemma])  # Agregar el token y el lema a la lista

# Escribir los tokens y lemas en el archivo CSV de salida
with open(output_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['token', 'lemma'])  # Escribir el encabezado de las columnas
    writer.writerows(data)  # Escribir los datos

