# Rename

import os

# Ruta del archivo actual
ruta_actual = 'rename\\demo.txt'

# Nueva ruta del archivo con el nuevo nombre
nueva_ruta = 'rename\\demo123.txt'

try:
    # Verificar que el archivo de origen existe
    if not os.path.exists(ruta_actual):
        print(f'El archivo no existe: {ruta_actual}')
    else:
        # Renombrar el archivo
        os.rename(ruta_actual, nueva_ruta)
        print(f'Archivo renombrado con éxito a: {nueva_ruta}')
except Exception as e:
    print(f'Ocurrió un error al renombrar el archivo: {e}')
