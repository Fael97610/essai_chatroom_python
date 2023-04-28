import socket
from threading import Thread

def Send(client):
    while True:
         msg = input("->")
         msg = msg.encode("utf-8")
         client.send(msg)

def Reception(client):
     while True:
        requete_client = client.recv(500)
        requete_client = requete_client.decode('utf-8')
        print(requete_client)
        if not requete_client:
            print("Fermeture de la session.")
            break




host = '192.168.1.15' #adresse ip
port = 4820

socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

socket.bind((host,port))
socket.listen(1)

client, ip = socket.accept()
print("le client d'adresse ",ip, " s'est connecté.")

envoi = Thread(target=Send,args=[client])
recep = Thread(target=Reception,args=[client])

envoi.start()
recep.start()

recep.join()
   
client.close()
socket.close()    