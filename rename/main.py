

from date import date 
import os


date1 = date()
init = 'rename\\file\\'

# Ruta del archivo de texto
#ruta_archivo = 'rename\\Reporte de cobros-CREP-CUOTA-03_08_2024 (1).txt'
# Reporte de cobros-CREP-AHORRO-03_08_2024

ruta_archivo_cuota = f'{init}Reporte de cobros-CREP-CUOTA-{date1} (1).txt'
ruta_archivo_ahorro = f'{init}Reporte de cobros-CREP-AHORRO-{date1}.txt'

# Nuevo nombre del archivo
nuevo_nombre_cuota = 'CREP7390.txt'
nuevo_nombre_ahorro = 'CREP7391.txt'

try:
    # Verificar que el archivo de origen existe
    if not os.path.exists(ruta_archivo_cuota):
        print(f'El archivo no existe: {ruta_archivo_cuota}')
    
    else:
        # Obtener la ruta del directorio del archivo
        directorio = os.path.dirname(ruta_archivo_cuota)
        directorio1 = os.path.dirname(ruta_archivo_ahorro)
        
        # Nueva ruta del archivo con el nuevo nombre
        nueva_ruta = os.path.join(directorio, nuevo_nombre_cuota)
        nueva_ruta1 = os.path.join(directorio1, nuevo_nombre_ahorro)
        
        # Renombrar el archivo
        os.rename(ruta_archivo_cuota, nueva_ruta)
        os.rename(ruta_archivo_ahorro, nueva_ruta1)
        print(f'Archivo renombrado con éxito a: {nueva_ruta}')
        print(f'Archivo renombrado con éxito a: {nueva_ruta1}')
        
except Exception as e:
    print(f'Ocurrió un error al renombrar el archivo: {e}')
