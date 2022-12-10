# pythonPackets v.1.0
# sender-randomSource.py
#
# Aleksi Bovellan
#
# Sends a TCP packet from user input text to any IP and port.
# Also sets a random source IP address.
# Run with 'sudo python3 sender-randomSource.py'

# Set the destination IP address and port

TARGET_IP = '0.0.0.0'
PORT = 80

import socket
import random

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set the source IP address to a random address
source_ip = ".".join(str(random.randint(0, 255)) for _ in range(4))

message = input("\nEnter the message to send: ").encode()

try:
    # Connect to the destination
    sock.connect((TARGET_IP, PORT))
    # Send a single packet
    sock.send(message)
    print("\nThe packet was sent!\n")
except:
    print("\nCould not create a connection.\n")


# Close the socket
sock.close()
