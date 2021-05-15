

#!/usr/bin/env python3
import socket
import os

FAKE_CLOUD_IP = '0.0.0.0'

print( 'Starting a socket on port 443!')
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
sock.bind((FAKE_CLOUD_IP, 443))
sock.listen(5)
while True:  
    connection,address = sock.accept()  
    buf = connection.recv(1024)
    print( 'received ' + buf.decode('utf8'))
    connection.send(buf)