# ver el tamaño de disco duro en GB, espacio usado y espacio libre

import psutil

# Solicitar al usuario que ingrese el nombre del disco o la ruta del punto de montaje
disk_path = input("Ingresa el nombre disco: ")

# Obtener información del disco
try:
    disk_usage = psutil.disk_usage(disk_path)

    # Tamaño total del disco en GB
    total_size_gb = disk_usage.total / (1024 ** 3)

    # Espacio usado en GB
    used_space_gb = disk_usage.used / (1024 ** 3)

    # Espacio libre en GB
    free_space_gb = disk_usage.free / (1024 ** 3)

    # Imprimir resultados
    print(f"Tamaño total del disco '{disk_path}': {total_size_gb:.2f} GB")
    print(f"Espacio usado: {used_space_gb:.2f} GB")
    print(f"Espacio libre: {free_space_gb:.2f} GB")
except FileNotFoundError:
    print(f"El disco o ruta '{disk_path}' no se pudo encontrar. Por favor, verifica el nombre o la ruta.")
except Exception as e:
    print(f"Se produjo un error: {e}")

# Pausar el cierre automático de la consola
input("\nPresiona Enter para salir...")
