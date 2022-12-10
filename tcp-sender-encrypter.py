# pythonPackets v.1.1
# tcp-sender-encrypter.py
#
# Aleksi Bovellan
#
# Sends a symmetrically encrypted TCP packet from user input text to any IP address and port set below.
# Might need to run 'pip3 install cryptography' before starting.
# Run with 'sudo python3.9 tcp-sender-encrypter.py' !!!


# Set the destination IP address and port

TARGET_IP = '0.0.0.0'
PORT = 80

# Set the Fernet key (it must be the same as the one used to read and decrypt encrypted messages)
# So better make a new one and put that same key into the tcp-listener-decrypter.py file also.

fernet_key = b'2fqczRzMV88AJwVz42cdDqdy2tk11lVDbXYEbOENuHU='


from socket import socket, AF_INET, SOCK_STREAM
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes, hmac
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet



# Encrypt the message using the Fernet key
def encrypt_message(message, fernet_key):
    f = Fernet(fernet_key)
    encrypted_message = f.encrypt(message)
    return encrypted_message

# Send the encrypted message to the target IP address and port
def send_message(encrypted_message, target_ip, target_port):
    with socket(AF_INET, SOCK_STREAM) as s:
        s.connect((target_ip, target_port))
        s.sendall(encrypted_message)


# Example usage
message = input("\nEnter the message to send: ").encode()
encrypted_message = encrypt_message(message, fernet_key)
try:
    send_message(encrypted_message, TARGET_IP, PORT)
    print("\nPacket sent!\n")

except:
    print("\nCould not create a connection.\n")

