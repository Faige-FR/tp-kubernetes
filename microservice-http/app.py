from flask import Flask, jsonify
# from dotenv import load_dotenv
import os

# Variables d'environnement
# load_dotenv('./.env')
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
    app.run(debug=True, port=port)