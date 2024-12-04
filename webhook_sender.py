import requests
import json

# Datos que queremos enviar como parte del webhook
data = {
    "evento": "nuevo_pago",
    "usuario": "juan",
    "monto": 100.0,
    "metodo_pago": "tarjeta_credito"
}

# URL del servidor receptor (webhook)
webhook_url = 'http://localhost:5000/webhook'

# Enviar solicitud POST al servidor receptor
response = requests.post(webhook_url, json=data)

# Verificar respuesta
if response.status_code == 200:
    print("Webhook enviado correctamente.")
else:
    print(f"Error al enviar el webhook: {response.status_code}")
