import psutil

def mostrar_tamano_disponible(disco):
    # Obtener información del disco
    uso_disco = psutil.disk_usage(disco)
    
    # Convertir el tamaño disponible a GB
    tamano_disponible_gb = uso_disco.free / (1024 ** 3)
    
    print(f"El tamaño disponible en el disco {disco} es: {tamano_disponible_gb:.2f} GB")

# Especifica la ruta del disco que quieres verificar (por ejemplo, 'C:\\' para Windows)
disco = 'C:\\'

mostrar_tamano_disponible(disco)
