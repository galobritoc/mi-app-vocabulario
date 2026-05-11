import os
from datetime import datetime
try:
    from twilio.rest import Client
except ImportError:
    import subprocess
    import sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "twilio"])
    from twilio.rest import Client

# Tu lista de palabras
vocabulario = [
    {"palabra": "Disentir", "definicion": "No ajustarse al parecer de otro.", "ejemplo": "Es sano disentir en las reuniones de directorio."},
    {"palabra": "Laconismo", "definicion": "Brevedad y economía de expresiones.", "ejemplo": "Su laconismo permitió enfocarse en los números clave."},
    # ... asegúrate de tener las 30 palabras aquí ...
]

def enviar_whatsapp():
    # Obtener llaves de GitHub Secrets
    account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
    auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
    
    if not account_sid or not auth_token:
        print("Error: No se encontraron las llaves secretas en GitHub.")
        return

    client = Client(account_sid, auth_token)

    # Lógica de selección
    dia_del_año = datetime.now().timetuple().tm_yday
    item = vocabulario[dia_del_año % len(vocabulario)]

    mensaje = (
        f"💡 *PALABRA DEL DÍA*\n\n"
        f"📖 *{item['palabra']}*: {item['definicion']}\n\n"
        f"📝 *Ejemplo:* {item['ejemplo']}"
    )

    try:
        message = client.messages.create(
            from_='whatsapp:+14155238886', # Asegúrate que este sea el número que te dio Twilio
            body=mensaje,
            to='whatsapp:+56989488615'     # PON TU NÚMERO AQUÍ CON +569
        )
        print(f"Éxito: Mensaje enviado con ID {message.sid}")
    except Exception as e:
        print(f"Error al enviar: {e}")

if __name__ == "__main__":
    enviar_whatsapp()
