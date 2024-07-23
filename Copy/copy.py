# El Archivo copia y borra del origen

import shutil
import os
from datetime import datetime, timedelta

fecha_anterior = datetime.now() - timedelta(days=1)
nombre_generado = fecha_anterior.strftime("MIS%m%dALL")


origen = 'C:\\demo1\\hola.txt'

# Solicitar al usuario la ruta de la carpeta de destino
# destino = 'C:\\demo2\\stokori\\bd\\'
destino = 'C:\\demo2\\'+nombre_generado+'\\hola.txt'

try:
    # Verificar que el archivo de origen existe
    if not os.path.exists(origen):
        print(f'El archivo de origen no existe: {origen}')
    else:
        # Crear la carpeta de destino si no existe
        os.makedirs(os.path.dirname(destino), exist_ok=True)

        # Mover el archivo
        shutil.move(origen, destino)
        print('Archivo movido con exito.')
except Exception as e:
    print(f'Ocurrio un error al mover el archivo: {e}')
