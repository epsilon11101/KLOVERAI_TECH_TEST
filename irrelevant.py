import csv

# Ruta del archivo CSV de entrada y salida
input_file = 'expanded_tokens.csv'
output_file = 'filtered_tokens.csv'

# Lista de palabras irrelevantes en inglés y español que se deben eliminar
irrelevant_words_en = [
    'ad', 'advertisement', 'promo', 'promotion', 'sale', 'discount', 'offer',
    'spam', 'irrelevant', 'off-topic', 'comment', 'discussion'
]

irrelevant_words_es = [
    'anuncio', 'promoción', 'venta', 'descuento', 'oferta', 'spam', 'irrelevante',
    'fuera de tema', 'comentario', 'discusión'
]

# Lista para almacenar los tokens filtrados
filtered_tokens = []

# Leer el archivo CSV de entrada y filtrar los tokens irrelevantes
with open(input_file, 'r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Leer la primera fila (encabezado de columna)
    for row in reader:
        token = row[0]  # Obtener el token original en la primera columna
        expanded_token = row[1]  # Obtener el token expandido en la segunda columna

        # Verificar si el token y el token expandido no están en la lista de palabras irrelevantes en inglés o español
        if (
            token.lower() not in irrelevant_words_en
            and token.lower() not in irrelevant_words_es
            and expanded_token.lower() not in irrelevant_words_en
            and expanded_token.lower() not in irrelevant_words_es
        ):
            filtered_tokens.append([token, expanded_token])  # Agregar el par token original y token expandido filtrado a la lista

# Escribir los tokens filtrados en el archivo CSV de salida
with open(output_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['token', 'expanded_token'])  # Escribir el encabezado de las columnas
    writer.writerows(filtered_tokens)  # Escribir los datos

print(f"Se han guardado los tokens filtrados en '{output_file}'.")
