import psutil

# Ruta del punto de montaje del disco llamado "stokori"
disk_path = '/mnt/stokori'  # O la letra de la unidad como 'E:\\' en Windows

# Obtener información del disco
disk_usage = psutil.disk_usage(disk_path)

# Tamaño total del disco en GB
total_size_gb = disk_usage.total / (1024 ** 3)

# Espacio usado en GB
used_space_gb = disk_usage.used / (1024 ** 3)

# Espacio libre en GB
free_space_gb = disk_usage.free / (1024 ** 3)

# Imprimir resultados
print(f"Tamaño total del disco 'stokori': {total_size_gb:.2f} GB")
print(f"Espacio usado: {used_space_gb:.2f} GB")
print(f"Espacio libre: {free_space_gb:.2f} GB")
