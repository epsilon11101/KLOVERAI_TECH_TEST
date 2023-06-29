import csv
from spellchecker import SpellChecker

# Ruta del archivo CSV de entrada y salida
input_file = 'lemmatized_tokens.csv'
output_file = 'corrected_tokens.csv'

# Crear objeto SpellChecker para el idioma inglés
spellchecker_en = SpellChecker(language='en')

# Crear objeto SpellChecker para el idioma español
spellchecker_es = SpellChecker(language='es')

# Lista para almacenar los lemmas y sus correcciones
data = []

# Leer el archivo CSV de entrada y realizar la corrección ortográfica
with open(input_file, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        token = row['token']
        lemma = row['lemma']
        corrected_lemma = ""

        # Realizar la corrección ortográfica del lemma en inglés
        if lemma in spellchecker_en:
            corrected_lemma = lemma
        else:
            corrected_lemma = spellchecker_en.correction(lemma)

        # Realizar la corrección ortográfica del lemma en español si es diferente al lemma original
        if corrected_lemma and corrected_lemma != lemma and corrected_lemma not in spellchecker_es:
            corrected_lemma = spellchecker_es.correction(corrected_lemma)

        # Conservar el lemma original si no tiene corrección ortográfica
        if not corrected_lemma:
            corrected_lemma = lemma

        data.append([lemma, corrected_lemma])  # Agregar el lemma original y su corrección a la lista

# Escribir los lemmas y sus correcciones en el archivo CSV de salida
with open(output_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['lemma', 'correction'])  # Escribir el encabezado de las columnas
    writer.writerows(data)  # Escribir los datos
