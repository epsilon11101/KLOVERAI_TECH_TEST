import csv

# Ruta del archivo CSV de entrada y salida
input_file = 'corrected_tokens.csv'
output_file = 'expanded_tokens.csv'

# Diccionario de abreviaciones y sus expansiones en inglés
abbreviations_en = {
    'lol': 'laughing out loud',
    'omg': 'oh my god',
    'btw': 'by the way',
    'idk': 'I don\'t know',
    'wtf': 'what the f**k',
    'tbh': 'to be honest',
    'brb': 'be right back',
    'imo': 'in my opinion',
    'fyi': 'for your information',
    'amlo': 'president',
    'ama': 'mom',
    'mxn': 'mexico'
    
}

# Diccionario de abreviaciones y sus expansiones en español
abbreviations_es = {
    'jajaja': 'risa',
    'omg': 'oh dios mío',
    'btw': 'por cierto',
    'idk': 'no lo sé',
    'wtf': 'qué demonios',
    'tbh': 'para ser honesto',
    'brb': 'vuelvo enseguida',
    'imo': 'en mi opinión',
    'fyi': 'para tu información',
    'amlo': 'presidente',
    'ama': 'mama',
    'mxn': 'mexico'
}

# Lista para almacenar los tokens originales y sus expansiones
data = []

# Leer el archivo CSV de entrada y expandir las abreviaciones y la jerga
with open(input_file, 'r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Leer la primera fila (encabezado de columna)
    for row in reader:
        token = row[0]  # Obtener el token en la primera columna

        # Expandir la abreviación si está presente en el diccionario correspondiente
        if token.lower() in abbreviations_en:
            expanded_token = abbreviations_en[token.lower()]
        elif token.lower() in abbreviations_es:
            expanded_token = abbreviations_es[token.lower()]
        else:
            expanded_token = token

        data.append([token, expanded_token])  # Agregar el token original y su expansión a la lista

# Escribir los tokens originales y sus expansiones en el archivo CSV de salida
with open(output_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['token', 'expanded_token'])  # Escribir el encabezado de las columnas
    writer.writerows(data)  # Escribir los datos

