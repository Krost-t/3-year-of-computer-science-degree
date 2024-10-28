import socket
import json
from pymongo import MongoClient
from flask import *



client = MongoClient('Localhost', 27017)
register = client.a_verifier

# le code ne fonctionne pas 


def conect():
    # Créer un socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Adresse IP et port sur lesquels écouter
    host = '192.168...'
    port = 80
     # Lier le socket à l'adresse IP et au port
    sock.bind((host, port))
     # Écouter les connexions entrantes
    sock.listen(1)
    while True:
         # Accepter une connexion entrante
         conn, addr = sock.accept()
         # Recevoir les données via le socket
         data = conn.recv(1024).decode()
         # Convertir la chaîne JSON en variable Python
         my_variable = json.loads(data)
         my_variable = str(my_variable)
         table = register.users.find_one({"numid": my_variable})
         print(table['nom'])
         return render_template("account.html",userName =  table['nom'])


    connect_user2(my_variable)
     # Fermer la connexion
    conn.close()
     # Fermer le socket
    sock.close()

conect()