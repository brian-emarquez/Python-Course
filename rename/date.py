from datetime import datetime, timedelta

def date():
    # Obtener la fecha de hoy
    fecha_hoy = datetime.today()

    # Restar un día
    fecha_ayer = fecha_hoy - timedelta(days=1)

    # Formatear las fechas para mostrarlas
    #fecha_hoy_str = fecha_hoy.strftime('%Y-%m-%d')
    fecha_ayer_str = fecha_ayer.strftime('%d_%m_%Y')
    return fecha_ayer_str
    
# Remove this commented out code
# print(fecha_ayer_str)


# 03_08_2024