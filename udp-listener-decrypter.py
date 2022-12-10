# pythonPackets v.1.1
# udp-listener-decrypter.py
#
# Aleksi Bovellan
#
# Listens for symmetrically encrypted UDP packets on port set below and decrypts them.
# Might need to run 'pip3 install cryptography' before starting.
# Run with 'sudo python3 udp-listener-decrypter.py'


# Set the listening port

PORT = 80

# Set the Fernet key (it must be the same as the one used to send encrypted messages)
# Better make a new one and put that same key into the udp-sender-encrypter.py file

key = b'GxLP1dAs6U6DxGvQ0uuuIdgJcnPOtaL5bpuwehbWn9k='


import base64
import socket
from cryptography.fernet import Fernet
import binascii


print(f'\nWaiting for encrypted UDP packets on port {PORT} ...\n')

def listen_for_connections():
 try:
  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  sock.bind(('', PORT))
  while True:
    # Receive the UDP packet
    data, addr = sock.recvfrom(1024)
    try:
     val = base64.b64decode(data)
     # Decrypt the UDP packet using the secret key
     f = Fernet(key)
     decrypted_message = f.decrypt(data)
     # Print the decrypted message
     print('Received encrypted UDP packet:', decrypted_message.decode(), '\n')
    except binascii.Error:
     print("Could not read, fragmented or not encrypted packet\n")
    except:
     print("Could not read, fragmented or not encrypted packet\n")
 except KeyboardInterrupt:
   sock.close()
   exit()

# Example usage
listen_for_connections()