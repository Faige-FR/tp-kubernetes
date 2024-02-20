from flask import Flask, jsonify
import os

# Variables d'environnement
port = os.getenv('APP_PORT')
msg = os.getenv('MESSAGE')

# Initialisation application Flask
app = Flask(__name__)

# Route /motd-api
@app.route('/motd-api')
def motd():
    data = {
        "message": msg
	}
    return jsonify(data)

# Exécution de l'application à l'exécution du fichier
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port)