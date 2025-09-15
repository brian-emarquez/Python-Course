pip install pywin32


import win32com.client
import os

def descargar_adjunto_outlook_desde_cuenta(nombre_cuenta_outlook, nombre_correo, nombre_adjunto, carpeta_destino):
    try:
        outlook_app = win32com.client.Dispatch("Outlook.Application")
        outlook_namespace = outlook_app.GetNamespace("MAPI")

        # Crear la carpeta de destino si no existe
        if not os.path.exists(carpeta_destino):
            os.makedirs(carpeta_destino)
            print(f"Carpeta de destino '{carpeta_destino}' creada.")

        # Iterar a través de todos los Stores (cuentas de correo)
        for store in outlook_namespace.Stores:
            if store.DisplayName.lower() == nombre_cuenta_outlook.lower():
                print(f"Cuenta '{store.DisplayName}' encontrada.")
                # Acceder a la bandeja de entrada de esta cuenta específica
                inbox = store.GetDefaultFolder(6) # 6 se refiere a la bandeja de entrada (Inbox)

                for message in inbox.Items:
                    if message.Subject == nombre_correo:
                        print(f"Correo '{nombre_correo}' encontrado en la cuenta '{store.DisplayName}'.")
                        if message.Attachments.Count > 0:
                            for attachment in message.Attachments:
                                if attachment.FileName == nombre_adjunto:
                                    ruta_completa_descarga = os.path.join(carpeta_destino, attachment.FileName)
                                    attachment.SaveAsFile(ruta_completa_descarga)
                                    print(f"Archivo '{nombre_adjunto}' descargado en: {ruta_completa_descarga}")
                                    return True  # Adjunto encontrado y descargado
                            print(f"El adjunto '{nombre_adjunto}' no se encontró en el correo '{nombre_correo}' en la cuenta '{store.DisplayName}'.")
                        else:
                            print(f"El correo '{nombre_correo}' en la cuenta '{store.DisplayName}' no tiene adjuntos.")
                        return False # Correo encontrado, pero adjunto no descargado
                
                print(f"Correo '{nombre_correo}' no encontrado en la bandeja de entrada de la cuenta '{store.DisplayName}'.")
                return False # No se encontró el correo en esta cuenta

        print(f"La cuenta '{nombre_cuenta_outlook}' no fue encontrada en Outlook.")
        return False

    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return False

if __name__ == "__main__":
    # ¡IMPORTANTE! Reemplaza esto con el nombre exacto de tu cuenta de Outlook
    # que aparece en la barra lateral de Outlook (e.g., tu dirección de correo electrónico)
    nombre_cuenta_a_buscar = "brian3marquez@outlook.com" # <--- ¡CAMBIA ESTO!
    
    nombre_correo_buscado = "Prueba Correo"
    nombre_adjunto_buscado = "demo.txt"
    
    carpeta_descargas = os.path.join(os.path.expanduser("~"), "Downloads")

    print(f"Buscando en la cuenta: '{nombre_cuenta_a_buscar}'")
    print(f"Buscando correo: '{nombre_correo_buscado}' con adjunto: '{nombre_adjunto_buscado}'")
    print(f"Carpeta de destino: '{carpeta_descargas}'")

    descarga_exitosa = descargar_adjunto_outlook_desde_cuenta(
        nombre_cuenta_a_buscar, 
        nombre_correo_buscado, 
        nombre_adjunto_buscado, 
        carpeta_descargas
    )

    if descarga_exitosa:
        print("Proceso de descarga completado con éxito.")
    else:
        print("Hubo un problema durante el proceso de descarga o el correo/adjunto no se encontró.")