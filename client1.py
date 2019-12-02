import socket
import threading

hote = "localhost"
port = 18200
#controle = False

connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_avec_serveur.connect((hote, port))

def First_whait_user():
    msg_a_envoyer = b""
    while msg_a_envoyer != b"exit":
        msg_a_envoyer = raw_input("> ")
        # Peut planter si vous tapez des caracteres speciaux
        msg_a_envoyer = msg_a_envoyer.encode()
        # On envoie le message
        connexion_avec_serveur.send(msg_a_envoyer)
            
def Second_listen_server():
    lol = True
    while lol == True:
        msg_recu = connexion_avec_serveur.recv(1024)
        print(msg_recu.decode()) # La encore, peut planter s'il y a des accents
        
first  = threading.Thread(target=First_whait_user)
second = threading.Thread(target=Second_listen_server)


first.start()
second.start()