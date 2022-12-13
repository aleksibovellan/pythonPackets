# pythonPackets v.1.3
# tcp-listener-decrypter.py
#
# Aleksi Bovellan
#
# Listens for symmetrically encrypted TCP packets on port set below and decrypts them.
# Might need to run 'pip3 install cryptography' before starting.
# Run with 'sudo python3 tcp-listener-decrypter.py'


from socket import socket, AF_INET, SOCK_STREAM
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes, hmac
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet
import binascii
import os, signal
import time


try:


 # Set the listening port manually here if typing is not needed.
 # Remember in that case to comment out the below 'input' line for port.

 # PORT = 80

 # Prompt the user for the listening  port:

 PORT = int(input('\nEnter the port number to listen for TCP packets: '))

 # Symmetric encryption key, which should be the same in your listener script, and sender script.
 # Better to change some values into random ones and  put that same key into the tcp-sender-encrypter.py file

 fernet_key = b'2fqczRzMV88AJwVz42cdDqdy2tk33lVDbXYEbOENuHU='


 # ---------------------------------


 try:

  # Find the process or processes that are using the specified port
  process_ids = os.popen("lsof -t -i:{}".format(PORT)).read().split('\n')

  # Remove empty strings from the list of process IDs
  process_ids = [x for x in process_ids if x]

  # Convert the process IDs from strings to integers
  process_ids = [int(x) for x in process_ids]

  # Stop the processes
  for process_id in process_ids:
     os.kill(process_id, signal.SIGKILL)
  print("\nPort checked free from previous process ...")
 except:
  print("\nPort could not be released from a previous process.")

 time.sleep(2)

 # Decrypt the message using the Fernet key
 def decrypt_message(encrypted_message, fernet_key):
     f = Fernet(fernet_key)
     decrypted_message = f.decrypt(encrypted_message)
     return decrypted_message

 # Listen for incoming connections on the specified port
 def listen_for_connections(listen_port):
  try:
     with socket(AF_INET, SOCK_STREAM) as s:
         s.bind(('', listen_port))
         print(f'\nWaiting for encrypted TCP packets on port {PORT} ...')
         while True:
             s.listen()
             conn, addr = s.accept()
             with conn:
                 print('\nGot a connection from', addr)
                 while True:
                     try:
                         data = conn.recv(1024)
                         if not data:
                             break
                         decrypted_message = decrypt_message(data, fernet_key)
                         print('Received an encrypted TCP packet:',
                               decrypted_message.decode())
                     except binascii.Error:
                         print("Could not read, probably not an encrypted packet")
                     except:
                         print("Could not read, probably not an encrypted packet")

  except KeyboardInterrupt:
   print("\n")
   exit()

 # Run the program.
 listen_for_connections(PORT)

except KeyboardInterrupt:
    print("\n")
    exit()
#except:
#         print('\nSomething went wrong, maybe the port value.\n')
#         exit()
