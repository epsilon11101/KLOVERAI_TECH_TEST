import subprocess

# Definir la lista de archivos en el orden que se deben ejecutar
file_list = [
    'scrapper.py',
    'tokens.py',
    'lema.py',
    'correction.py',
    'jerga.py',
    'irrelevant.py',
    'split.py'
]

# Ejecutar los archivos en orden
for file in file_list:
    subprocess.run(['python3', file])
