# pythonPackets v.1.2
# tcp-listener.py
#
# Aleksi Bovellan
#
# Listens for TCP packets on port set below.
# Run with 'sudo python3 tcp-listener.py'


# Set the listening port

PORT = 80


import socket

# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# get local machine name
host = socket.gethostname()


# bind to the port
serversocket.bind((host, PORT))


# queue up to 5 requests
serversocket.listen(5)

print(f'\nWaiting for TCP packets on port {PORT} ...')


try:
 while True:
    # establish a connection
    clientsocket, addr = serversocket.accept()

    print("\nGot connection from %s" % str(addr))

    # receive data from the client
    data = clientsocket.recv(1024).decode()

    print("Received TCP packet: %s" % data)

    # send a thank you message to the client
    clientsocket.send(b'Thank you for connecting')

    # close the connection
    clientsocket.close()
    
except KeyboardInterrupt:
 serversocket.close()
 print("\n")
 exit()
