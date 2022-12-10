# pythonPackets v.1.2
# udp-sender-encrypter.py
#
# Aleksi Bovellan
#
# Sends a symmetrically encrypted UDP packet from user input text to any IP address and port set below.
# Might need to run 'pip3 install cryptography' before starting.
# Run on Linux with "sudo python3 udp-sender-encrypter.py"
# Run on MacOS with 'sudo python3.9 udp-sender-encrypter.py'


# Set the destination IP address and port

TARGET_IP = '0.0.0.0'
PORT = 80

# Set the Fernet key (it must be the same as the one used to read and decrypt encrypted messages)
# Better make a new one and put that same key into the udp-listener-decrypter.py file also.

key = b'GxLP1dAs6U6DxGvQ0pppIdgJcnPOtaL5bpuwehbWn9k='


import socket
from cryptography.fernet import Fernet


# Get the message to be encrypted from the user
message = input("\nEnter the message to send: ")

# Encrypt the message using the secret key
f = Fernet(key)
encrypted_message = f.encrypt(message.encode())

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Set the source IP and port
sock.bind(('', 0))

# Send the UDP packet to the target IP and port
try:
 sock.sendto(encrypted_message, (TARGET_IP, PORT))
 print("\nPacket was sent!\n")
except:
 print("The packet was not sent.\n")

# Close the socket
sock.close()