# pythonPackets v.1.1
# udp-listener.py
#
# Aleksi Bovellan
#
# Listens for UDP packets on port set below.
# Run with 'sudo python3 udp-listener.py'


# Set the target port

PORT = 80


import socket

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


# Bind the socket to the target IP and port
sock.bind(('', PORT))

print(f'\nWaiting for UDP packets on port {PORT} ...')


while True:
    # Receive the UDP packet
    data, addr = sock.recvfrom(1024)

    # Print the UDP packet in plain text
    print("\n" + data.decode())

# Close the socket
sock.close()