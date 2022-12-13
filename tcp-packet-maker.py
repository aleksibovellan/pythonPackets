# pythonPackets v.1.3
# tcp-packet-maker.py
#
# Aleksi Bovellan
#
# Creates a custom TCP packet by asking the user to fill values to the packet fields.
# Run with 'sudo python3 tcp-packet-maker.py'


import socket


# Default values for the fields in the TCP packet
source_ip = '127.0.0.1'
dest_ip = '127.0.0.1'
source_port = 12345
dest_port = 80
seq_num = 0
ack_num = 0
data = ''


print('')
try:

 # Prompt the user to enter values for each field in the TCP packet:
 source_ip = input(
     'Enter the source IP address (default: 127.0.0.1): ') or source_ip
 dest_ip = input(
     'Enter the destination IP address (default: 127.0.0.1): ') or dest_ip

 # Check that the IP addresses are valid
 try:
     socket.inet_aton(source_ip)
     socket.inet_aton(dest_ip)
     TARGET_IP = dest_ip
 except socket.error:
     print('Invalid IP address')
     exit()

 source_port = input('Enter the source port (default: 12345): ') or source_port

 # Check that the source port is a valid integer
 try:
     source_port = int(source_port)
     if source_port < 0 or source_port > 65535:
         raise ValueError
 except ValueError:
     print('Invalid port number')
     exit()

 dest_port = input('Enter the destination port (default: 80): ') or dest_port

 # Check that the destination port is a valid integer
 try:
     dest_port = int(dest_port)
     PORT = dest_port
     if dest_port < 0 or dest_port > 65535:
         raise ValueError
 except ValueError:
     print('Invalid port number')
     exit()

 seq_num = input('Enter the sequence number (default: 0): ') or seq_num

 # Check that the sequence number is a valid integer
 try:
     seq_num = int(seq_num)
     if seq_num < 0:
         raise ValueError
 except ValueError:
     print('Invalid sequence number')
     exit()

 ack_num = input('Enter the acknowledgement number (default: 0): ') or ack_num

 # Check that the acknowledgement number is a valid integer
 try:
     ack_num = int(ack_num)
     if ack_num < 0:
         raise ValueError
 except ValueError:
     print('Invalid acknowledgement number')
     exit()

 # Prompt the user to enter the data to be sent in the packet
 data = input(
     "\nEnter the message to be sent in the TCP packet's payload field: ")

 # Create the TCP packet using the specified values
 tcp_packet = socket.inet_aton(source_ip) + socket.inet_aton(dest_ip) + \
     source_port.to_bytes(2, byteorder='big') + dest_port.to_bytes(2, byteorder='big') + \
     seq_num.to_bytes(4, byteorder='big') + ack_num.to_bytes(4, byteorder='big') + \
     data.encode('utf-8')

 # Print the created TCP packet
 print('\nTCP packet created (raw): ', tcp_packet, '\n')

 # Ask the user if the TCP packet should be sent
 send = input('Do you want to send the packet to the destination? (y/n): ')

 # Send the packet if the user confirmed
 if send.lower() == 'y':
     # Connect to the destination
     # Create a socket for sending the TCP packet
     print('\nTrying to connect to destination ...')
     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     sock.connect((dest_ip, dest_port))
     # Send the TCP packet (assuming the variable "tcp_packet" is a byte type object representing the packet)
     sock.sendall(tcp_packet)
     # Close the socket
     sock.close()
     print('\nTCP packet was sent!\n')
 else:
     print('\nTCP packet was not sent.\n')

except KeyboardInterrupt:
    print("\n")
    exit()
except:
    print('\nSomething went wrong, maybe some of the values.\n')
    exit()
