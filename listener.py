# listener.py

# Listens for TCP packets on port 80
# Use with python3

import socket

# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

port = 80

# bind to the port
serversocket.bind((host, port))

# queue up to 5 requests
serversocket.listen(5)

print("Waiting for TCP connections on port 80 ...")

while True:
    # establish a connection
    clientsocket,addr = serversocket.accept()

    print("Got a connection from %s" % str(addr))

    # receive data from the client
    data = clientsocket.recv(1024)

    print("Received data: %s" % data)

    # send a thank you message to the client
    clientsocket.send(b'Thank you for connecting')

    # close the connection
    clientsocket.close()

