# El Archivo copia y borra del origen

import shutil
import os
from datetime import datetime, timedelta
from month import obtener_mes_actual
from year import obtener_ano_actual

# Obtener el mes actual en mayúsculas
mont = obtener_mes_actual()
year = obtener_ano_actual()

fecha_anterior = datetime.now() - timedelta(days=1)
nombre_generado = fecha_anterior.strftime("MIS%m%dALL")

# Lista de archivos de origen
archivos_origen = [
    'C:\\DB\\Backups\\',
]

# Ruta base de la carpeta de destino
destino_base = f'C:\\stokori\\db\\{year}\\{mont}\\{nombre_generado}\\'

try:
    for origen in archivos_origen:
        # Verificar que el archivo de origen existe
        if not os.path.exists(origen):
            print(f'El archivo de origen no existe: {origen}')
        else:
            # Obtener el nombre del archivo
            nombre_archivo = os.path.basename(origen)
            # Construir la ruta completa del archivo de destino
            destino = os.path.join(destino_base, nombre_archivo)
            
            # Crear la carpeta de destino si no existe
            os.makedirs(os.path.dirname(destino), exist_ok=True)

            # Mover el archivo
            shutil.move(origen, destino)
            print(f'Archivo {nombre_archivo} movido con éxito.')
except Exception as e:
    print(f'Ocurrió un error al mover el archivo: {e}')
