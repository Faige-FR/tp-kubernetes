# Thibaut ALLART - TP Kubernetes

Image Docker : faige/flask:1.0.0

Pour démarrer le conteneur :
docker run -e "APP_PORT=<port>" -e "MESSAGE=<message>" -dp "$APP_PORT":"$APP_PORT" faige/flask:1.0.0

Exemple :
docker run -e "APP_PORT=9999" -e "MESSAGE=test-msg" -dp "$APP_PORT":"$APP_PORT" faige/flask:1.0.0