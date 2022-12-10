# listener-decrypter.py
#
# might need to run pip3 install cryptography
# run with python3

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes, hmac
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.exceptions import InvalidSignature
from socket import socket, AF_INET, SOCK_STREAM

# Set the Fernet key (must be the same as the one used to encrypt the message)
# Better to make your own and put the same key into the sender-encrypter.py

fernet_key = b'2fqczRzMV88AJwVz42cdDqdy2tk11lVDbXYEbOENuHU='

waitingText = "Waiting for encrypted TCP packet on port 80 ..."
print(waitingText)

# Decrypt the message using the Fernet key
def decrypt_message(encrypted_message, fernet_key):
    f = Fernet(fernet_key)
    decrypted_message = f.decrypt(encrypted_message)
    return decrypted_message

# Listen for incoming connections on the specified port
def listen_for_connections(listen_port):
    with socket(AF_INET, SOCK_STREAM) as s:
        s.bind(('', listen_port))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connection from', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                decrypted_message = decrypt_message(data, fernet_key)
                print('Received message:', decrypted_message)

# Example usage
listen_for_connections(80)

