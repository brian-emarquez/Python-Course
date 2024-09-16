import pywhatkit as kit
import schedule
import time

def send_whatsapp_message():
    # Número de teléfono en formato internacional
    kit.sendwhatmsg("+51943787427", "Hola, este es un mensaje programado", 14, 0)

# Programar el envío para las 14:00 (2:00 PM)
schedule.every().day.at("13:58").do(send_whatsapp_message)

while True:
    # Revisa cada segundo si hay alguna tarea programada
    schedule.run_pending()
    time.sleep(1)
