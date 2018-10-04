import socket
import time
import random

host = "127.0.0.1"
port = 80

def send(msg):
    s.send(msg.encode("UTF-8"))

def getInstructions():
    while True:
        msg = s.recv(4096)
        inst = msg.decode("UTF-8")

        if(inst == "test"):
            try:
                send("Test received")
            except:
                pass

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
connected = False
while connected == False:
    try:
        s.connect((host, port))
        connected = True
        print("Connected to server - IP: " + host)
    except socket.error as e:
        sleepTime = random.randint(20,30)
        time.sleep(sleepTime)
getInstructions()


