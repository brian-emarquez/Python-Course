import datetime
import locale

def obtener_mes_actual():
    # Establecer la configuración regional a español
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
    # Obtener el mes actual en español y convertirlo a mayúsculas
    mes_actual = datetime.datetime.now().strftime("%B").upper()
    return mes_actual

