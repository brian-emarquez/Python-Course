from twilio.rest import Client
import schedule
import time

# Credenciales de Twilio (obtén estas credenciales de tu cuenta de Twilio)
account_sid = 'TU_ACCOUNT_SID'
auth_token = 'TU_AUTH_TOKEN'
twilio_number = 'whatsapp:+14155238886'  # Este es el número de Twilio para WhatsApp

# Crear el cliente de Twilio
client = Client(account_sid, auth_token)

# Función para enviar el mensaje
def enviar_mensaje():
    mensaje = client.messages.create(
        from_=twilio_number,
        body='¡Hola grupo! Este es un mensaje programado.',
        to='whatsapp:+521XXXXXXXXXX'  # El número de WhatsApp del grupo o persona (necesita estar verificado en Twilio)
    )
    print(f"Mensaje enviado con SID: {mensaje.sid}")

# Programar el mensaje para una hora específica
def programar_mensaje(hora):
    schedule.every().day.at(hora).do(enviar_mensaje)

# Programar el mensaje para las 10:00 AM (puedes ajustar la hora)
programar_mensaje("10:00")

# Mantener el script corriendo para verificar el tiempo constantemente
while True:
    schedule.run_pending()
    time.sleep(60)  # Revisar cada minuto
