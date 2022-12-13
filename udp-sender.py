# pythonPackets v.1.3
# udp-sender.py
#
# Aleksi Bovellan
#
# Sends a UDP packet from user input text to any ip address and port set below.
# Run with 'sudo python3 udp-sender.py'


import socket


try:


 # Set the destination IP address and port manually here if typing is not needed.
 # Remember in that case to comment out the below 'input' lines for IP and port.

 # TARGET_IP = '127.0.0.1'
 # PORT = 80

 # Prompt the user for the destination IP address and port:

 TARGET_IP = input('\nEnter the IP address where to send the UDP packet: ') 
 PORT = int(input('Enter the port number: '))


 # Prompt the user for the message to send:

 message = input("\nEnter the message to be sent in the UDP packet's payload field: ")


 # ---------------------------------


 # Create a UDP socket
 sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

 # Set the source IP and port
 sock.bind(('', 0))

 # Send the UDP packet to the target IP and port
 try:
  sock.sendto(message.encode(), (TARGET_IP, PORT))
  print("\nUDP packet was sent!\n")
 except:
  print("\nUDP packet was not sent.\n")

 # Close the socket
 sock.close()

except KeyboardInterrupt:
    print("\n")
    exit()
except:
    print('\nSomething went wrong, maybe the target values.\n')
    exit()
