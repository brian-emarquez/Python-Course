

from date import date 
import os


date1 = date()

# Ruta del archivo de texto
#ruta_archivo = 'rename\\Reporte de cobros-CREP-CUOTA-03_08_2024 (1).txt'
ruta_archivo = f'rename\\Reporte de cobros-CREP-CUOTA-{date1}(1).txt'

print('------------------------', ruta_archivo)

# Nuevo nombre del archivo
nuevo_nombre = 'CREP7390.txt'

try:
    # Verificar que el archivo de origen existe
    if not os.path.exists(ruta_archivo):
        print(f'El archivo no existe: {ruta_archivo}')
    else:
        # Obtener la ruta del directorio del archivo
        directorio = os.path.dirname(ruta_archivo)
        
        # Nueva ruta del archivo con el nuevo nombre
        nueva_ruta = os.path.join(directorio, nuevo_nombre)
        
        # Renombrar el archivo
        os.rename(ruta_archivo, nueva_ruta)
        print(f'Archivo renombrado con éxito a: {nueva_ruta}')
except Exception as e:
    print(f'Ocurrió un error al renombrar el archivo: {e}')
