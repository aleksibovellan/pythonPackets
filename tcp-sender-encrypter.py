# pythonPackets v.1.3
# tcp-sender-encrypter.py
#
# Aleksi Bovellan
#
# Sends a symmetrically encrypted TCP packet from user input text to any IP address and port set below.
# Might need to install 'pip3 install cryptography' before starting.
# Run on Linux with 'sudo python3 tcp-sender-encrypter.py'
# Run on MacOS with 'sudo python3.9 tcp-sender-encrypter.py'


from socket import socket, AF_INET, SOCK_STREAM
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes, hmac
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet


try:


 # Set the destination IP address and port manually here if typing is not needed.
 # Remember in that case to comment out the below 'input' lines for IP and port.

 # TARGET_IP = '127.0.0.1'
 # PORT = 80

 # Prompt the user for the destination IP address and port:

 TARGET_IP = input('\nEnter the IP address where to send the encrypted TCP packet: ') 
 PORT = int(input('Enter the port number: '))


 # Prompt the user for the message to send:

 message = input("\nEnter the message to be sent in the encrypted TCP packet's payload field: ").encode()

 # Symmetric encryption key, which should be the same in your sender script, and listener script.
 # # Better to change some values into random ones and put that same key into the tcp-listener-decrypter.py file

 fernet_key = b'2fqczRzMV88AJwVz42cdDqdy2tk33lVDbXYEbOENuHU='


 # ---------------------------------


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

 # Run the program.
 encrypted_message = encrypt_message(message, fernet_key)
 try:
     print('\nTrying to connect to destination ...')
     send_message(encrypted_message, TARGET_IP, PORT)
     print("\nEncrypted TCP packet was sent!\n")

 except:
     print("\nCould not create a connection.\n")


except KeyboardInterrupt:
    print("\n")
    exit()
except:
    print('\nSomething went wrong, maybe the target values.\n')
    exit()
