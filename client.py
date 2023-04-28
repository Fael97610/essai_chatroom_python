import socket
from threading import Thread

def Send(socket):
    while True:
        msg = input('->')
        msg = msg.encode('utf-8')
        socket.send(msg)
        
def Reception(socket):
    while True:
        requete_server = socket.recv(500)
        requete_server = requete_server.decode("utf-8")
        print(requete_server)


host = '192.168.1.15' #adresse ip
port = 4820

socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

socket.connect((host,port))


envoi = Thread(target=Send,args=[socket])
recep = Thread(target=Reception,args=[socket])

envoi.start()
recep.start()