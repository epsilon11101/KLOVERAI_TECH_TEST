import csv
import os
from sklearn.model_selection import train_test_split

# Ruta del archivo CSV de entrada
input_file = 'expanded_tokens.csv'

# Leer el archivo CSV y obtener los datos
data = []
with open(input_file, 'r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Leer la primera fila (encabezados de columna)
    for row in reader:
        data.append(row)

# Dividir los datos en conjuntos de entrenamiento, validación y prueba
train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)
train_data, val_data = train_test_split(train_data, test_size=0.2, random_state=42)

# Rutas de los archivos CSV de salida
train_file = 'train_data.csv'
val_file = 'val_data.csv'
test_file = 'test_data.csv'

directory = './'

file_list = os.listdir(directory)

# Eliminar los archivos CSV en el directorio
for file_name in file_list:
    if file_name.endswith('.csv'):
        file_path = os.path.join(directory, file_name)
        os.remove(file_path)

# Guardar los conjuntos de datos en archivos CSV separados
def save_data_to_csv(data, file_path):
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)  # Escribir el encabezado de columna
        writer.writerows(data)

save_data_to_csv(train_data, train_file)
save_data_to_csv(val_data, val_file)
save_data_to_csv(test_data, test_file)


print("WELL DONE!")