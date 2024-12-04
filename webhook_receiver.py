from flask import Flask, request, jsonify

app = Flask(__name__)

# Este es el endpoint que recibirá el webhook
@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        # Obtiene los datos del webhook en formato JSON
        data = request.json
        print("Datos recibidos:", data)

        # Aquí podrías realizar el procesamiento de los datos
        # Ejemplo: almacenar en una base de datos, enviar un correo, etc.
        
        # Responder con éxito (200 OK)
        return jsonify({"message": "Webhook recibido correctamente!"}), 200

    except Exception as e:
        # En caso de error, responder con un código 500
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Ejecutar el servidor Flask
    app.run(debug=True, port=5000)
