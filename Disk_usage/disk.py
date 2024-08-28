import psutil

# Obtener información del disco
disk_usage = psutil.disk_usage('/')

# Tamaño total del disco en GB
total_size_gb = disk_usage.total / (1024 ** 3)

# Espacio usado en GB
used_space_gb = disk_usage.used / (1024 ** 3)

# Espacio libre en GB
free_space_gb = disk_usage.free / (1024 ** 3)

# Imprimir resultados
print(f"Tamaño total del disco: {total_size_gb:.2f} GB")
print(f"Espacio usado: {used_space_gb:.2f} GB")
print(f"Espacio libre: {free_space_gb:.2f} GB")
import psutil


