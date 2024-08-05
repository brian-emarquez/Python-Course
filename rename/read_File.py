# Ruta del archivo
ruta_archivo = 'rename\\123.txt'

try:
    # Abrir el archivo en modo de lectura
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        contenido = archivo.read()
        print(contenido)
except FileNotFoundError:
    print(f'El archivo no se encontró: {ruta_archivo}')
except Exception as e:
    print(f'Ocurrió un error al leer el archivo: {e}')
