import os
from datetime import datetime
from twilio.rest import Client

# Tu lista de palabras (puedes poner las 30 que te di)
vocabulario = [
    {"palabra": "Disentir", "definicion": "No ajustarse al parecer de otro.", "ejemplo": "Es sano disentir en el directorio."},
    # ... agrega el resto de las 30 aquí ...
]

def enviar_whatsapp():
    # Credenciales secretas (las configuraremos en GitHub)
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)

    # Lógica para elegir palabra del día
    dia_del_año = datetime.now().timetuple().tm_yday
    item = vocabulario[dia_del_año % len(vocabulario)]

    mensaje = (
        f"💡 *PALABRA DEL DÍA*\n\n"
        f"📖 *{item['palabra']}*: {item['definicion']}\n\n"
        f"📝 *Ejemplo:* {item['ejemplo']}"
    )

    # Enviar mensaje
    message = client.messages.create(
        from_='whatsapp:+14155238886', # Número de Twilio
        body=mensaje,
        to='whatsapp:+569XXXXXXXX'     # TU NÚMERO
    )
    print(f"Mensaje enviado: {message.sid}")

if __name__ == "__main__":
    enviar_whatsapp()