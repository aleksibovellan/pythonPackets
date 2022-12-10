# pythonPackets v.1.2
# udp-sender.py
#
# Aleksi Bovellan
#
# Sends a UDP packet from user input text to any ip address and port set below.
# Run with 'sudo python3 udp-sender.py'


# Set the target IP address and listening port

IP_TARGET = '0.0.0.0'
PORT = 80


import socket


# Prompt the user for the message to send
message = input('\nEnter the message to send: ')


# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


# Set the source IP and port
sock.bind(('', 0))


# Send the UDP packet to the target IP and port
try:
 sock.sendto(message.encode(), (IP_TARGET, PORT))
 print("\nPacket was sent!\n")
except:
 print("The packet was not sent.\n")


# Close the socket
sock.close()