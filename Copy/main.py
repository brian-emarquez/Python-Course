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

# Carpeta de origen
#D:\BD\Backups
carpeta_origen = 'D:\\DB\\Backups\\'

# Asegurarse de que la carpeta de origen existe
if not os.path.exists(carpeta_origen):
    print(f'La carpeta de origen no existe: {carpeta_origen}')
    exit()

path01 = 'BD_ÑAUPAX'
path02 = 'BD_KORI'

# Ruta base de la carpeta de destino
destino_base = f'C:\\stokori\\db\\{year}\\{mont}\\{nombre_generado}\\'

# Crear las carpetas destino_base, BD_ÑAUPAX y BD_KORI
destino01 = os.path.join(destino_base, path01)
destino02 = os.path.join(destino_base, path02)

try:
    # Crear las carpetas de destino si no existen
    os.makedirs(destino01, exist_ok=True)
    os.makedirs(destino02, exist_ok=True)
    print(f'Carpetas creadas con éxito: {destino01}, {destino02}')
    
    # Listar todos los archivos en la carpeta de origen
    archivos_origen = [os.path.join(carpeta_origen, f) for f in os.listdir(carpeta_origen) if os.path.isfile(os.path.join(carpeta_origen, f))]
    
    for origen in archivos_origen:
        # Obtener el nombre del archivo
        nombre_archivo = os.path.basename(origen)
        
        # Construir la ruta completa del archivo de destino en BD_ÑAUPAX
        destino_completo = os.path.join(destino01, nombre_archivo)
        
        # Mover el archivo (copia y luego elimina el original)
        shutil.move(origen, destino_completo)
        print(f'Archivo {nombre_archivo} movido con éxito a {destino_completo}.')
    
    # Eliminar el contenido de la carpeta de origen sin eliminar la carpeta en sí
    for root, dirs, files in os.walk(carpeta_origen):
        for file in files:
            os.remove(os.path.join(root, file))
        for dir in dirs:
            shutil.rmtree(os.path.join(root, dir))

    print('Contenido de la carpeta de origen eliminado con éxito.')
except Exception as e:
    print(f'Ocurrió un error: {e}')
