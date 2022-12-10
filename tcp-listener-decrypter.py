# pythonPackets v.1.1
# tcp-listener-decrypter.py
#
# Aleksi Bovellan
#
# Listens for symmetrically encrypted TCP packets on port set below and decrypts them.
# Might need to run 'pip3 install cryptography' before starting.
# Run with 'sudo python3 tcp-listener-decrypter.py'


# Set the listening port

PORT = 80

# Set the Fernet key (it must be the same as the one used to create and send encrypted messages)
# Better make a new one and put that same key into the tcp-sender-encrypter.py file

fernet_key = b'2fqczRzMV88AJwVz42cdDqdy2tk11lVDbXYEbOENuHU='


from socket import socket, AF_INET, SOCK_STREAM
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes, hmac
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet
import binascii

print(f'\nWaiting for encrypted TCP packets on port {PORT} ...')


# Decrypt the message using the Fernet key
def decrypt_message(encrypted_message, fernet_key):
    f = Fernet(fernet_key)
    decrypted_message = f.decrypt(encrypted_message)
    return decrypted_message

# Listen for incoming connections on the specified port
def listen_for_connections(listen_port):
    with socket(AF_INET, SOCK_STREAM) as s:
        s.bind(('', listen_port))
        while True:
            s.listen()
            conn, addr = s.accept()
            with conn:
                print('\nConnection from', addr)
                while True:
                    try:
                        data = conn.recv(1024)
                        if not data:
                            break
                        decrypted_message = decrypt_message(data, fernet_key)
                        print('Received encrypted packet:',
                              decrypted_message.decode(), '\n')
                    except binascii.Error:
                        print("Could not read, probably not encrypted packet\n")
                    except:
                        print("Could not read, probably not encrypted packet\n")


# Example usage
listen_for_connections(PORT)
