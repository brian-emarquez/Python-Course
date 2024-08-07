import psutil

def mostrar_tamano_disponible(disco):
    try:
        # Obtener información del disco
        uso_disco = psutil.disk_usage(disco)
        
        # Convertir el tamaño disponible a GB
        tamano_disponible_gb = uso_disco.free / (1024 ** 3)
        
        print(f"El tamaño disponible en el disco {disco} es: {tamano_disponible_gb:.2f} GB")
    except FileNotFoundError:
        print(f"El disco {disco} no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Solicitar al usuario que ingrese el nombre del disco
disco = input("Ingrese el nombre del disco (por ejemplo, 'C:\\' para Windows): ")

mostrar_tamano_disponible(disco)
