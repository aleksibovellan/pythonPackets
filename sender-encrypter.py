# pythonPackets v.1.0
# sender-encrypter.py
#
# Aleksi Bovellan
#
# Sends an encrypted TCP packet from user input text to any IP and port.
# Might need to run 'pip3 install cryptography' before starting.
# Run with 'sudo python3.9 sender-encrypter.py'

# Set the destination IP address and port

from socket import socket, AF_INET, SOCK_STREAM
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes, hmac
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet
TARGET_IP = '0.0.0.0'
PORT = 80

# Set the Fernet key (it must be the same as the one used to read and decrypt encrypted messages)
# Better to make a new one and put that same key into the listener-decrypter.py file.

fernet_key = b'2fqczRzMV88AJwVz42cdDqdy2tk11lVDbXYEbOENuHU='


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
