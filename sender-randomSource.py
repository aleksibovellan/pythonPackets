# sender-randomSource.py

# Sends a TCP packet from user input text to port 80
# Also sets a random source IP address
# Fill in TARGET_IP
# Use with python3

import socket
import random

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set the source IP address to a random address
source_ip = ".".join(str(random.randint(0, 255)) for _ in range(4))

# Set the destination IP address and port
dest_ip = "TARGET_IP"
dest_port = 80

message = input("\nEnter the message to send: ").encode()

try:
    # Connect to the destination
    sock.connect((dest_ip, dest_port))
    # Send a single packet
    sock.send(message)
    print("\nThe packet was sent!\n")
except:
    print("\nCould not create a connection.\n")


# Close the socket
sock.close()