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

origen = 'C:\\BD\\Backups\\hola.txt'

# Solicitar al usuario la ruta de la carpeta de destino
destino = 'C:\\stokori\\db\\'+ year + mont + '\\' + nombre_generado + '\\' + 'hola.txt'


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
