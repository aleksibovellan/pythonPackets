# pythonPackets v.1.3
# udp-sender-encrypter.py
#
# Aleksi Bovellan
#
# Sends a symmetrically encrypted UDP packet from user input text to any IP address and port set below.
# Might need to run 'pip3 install cryptography' before starting.
# Run on Linux with "sudo python3 udp-sender-encrypter.py"
# Run on MacOS with 'sudo python3.9 udp-sender-encrypter.py'


import socket
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

 message = input("\nEnter the message to send: ")

 # Symmetric encryption key, which should be the same in your sender script, and listener script.
 # Better to change some values into random ones and put that same key into the udp-listener-decryp

 key = b'GxLP1dAs6U6DxGvQ0pppIdgJcnPOtaL5bpuwehbWn9k='


 # ---------------------------------


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
  print("\nEncrypted UDP packet was sent!\n")
 except:
  print("\nEncrypted UDP packet was not sent.\n")

 # Close the socket
 sock.close()


except KeyboardInterrupt:
    print("\n")
    exit()
except:
    print('\nSomething went wrong, maybe the target values.\n')
    exit()
