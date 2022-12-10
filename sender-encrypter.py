# sender-encrypter.py
#
# Sends an encrypted TCP packet from user input text to port 80
# Might need to run pip3 install cryptography
# Fill in TARGET_IP below
# Run with python 3.9

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes, hmac
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.exceptions import InvalidSignature
from socket import socket, AF_INET, SOCK_STREAM

# Generate a random 32-byte Fernet key
# Better to make your own and put the same key into the listener-decrypter.py

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
message = input("Enter the message to send: ").encode()
encrypted_message = encrypt_message(message, fernet_key)
try:
        send_message(encrypted_message, 'TARGET_IP', 80)
        print("Packet sent!")

except:
        print("Packet did not send.")


