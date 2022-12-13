# pythonPackets v.1.3
# udp-listener-decrypter.py
#
# Aleksi Bovellan
#
# Listens for symmetrically encrypted UDP packets on port set below and decrypts them.
# Might need to run 'pip3 install cryptography' before starting.
# Run with 'sudo python3 udp-listener-decrypter.py'


import base64
import socket
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
 # Better to change some values into random ones and  put that same key into the udp-sender-encrypter.py file

 key = b'GxLP1dAs6U6DxGvQ0pppIdgJcnPOtaL5bpuwehbWn9k='


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

 def listen_for_connections():
  try:
   sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   sock.bind(('', PORT))
   print(f'\nWaiting for encrypted UDP packets on port {PORT} ...\n')
   while True:
     # Receive the UDP packet
     data, addr = sock.recvfrom(1024)
     try:
      val = base64.b64decode(data)
      # Decrypt the UDP packet using the secret key
      f = Fernet(key)
      decrypted_message = f.decrypt(data)
      # Print the decrypted message
      print('Got a connection from', addr)
      print('Received encrypted UDP packet:', decrypted_message.decode(), "\n")
     except binascii.Error:
      print("Could not read, fragmented or not encrypted packet\n")
     except:
      print("Could not read, fragmented or not encrypted packet\n")

  except KeyboardInterrupt:
    print("\n")
    sock.close()
    exit()

 # Run the program.
 listen_for_connections()


except KeyboardInterrupt:
    print("\n")
    exit()
except:
    exit()
