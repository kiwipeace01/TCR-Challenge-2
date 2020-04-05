#Truck3
import socket
import time

ClientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = '127.0.0.1'
port = 9999

print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
    print('Connection established')
except socket.error as e:
    print("There was an Error:",str(e))
    

while True:
    
    ClientSocket.send(str.encode('free'))

    data=(ClientSocket.recv(1024)).decode('utf-8')
    loc,t=data.split(" ")
        
    print(t)
    print(loc)
    timeout=time.time()+int(t)
        
    while True:
        #print("Entering second loop")
        ClientSocket.send(str.encode('busy'))
        
        if time.time()>timeout:
            print("Delivery done,next")
            break

