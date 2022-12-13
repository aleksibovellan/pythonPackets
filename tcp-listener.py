# pythonPackets v.1.3
# tcp-listener.py
#
# Aleksi Bovellan
#
# Listens for TCP packets on port set below.
# Run with 'sudo python3 tcp-listener.py'


import struct
import binascii
import socket
import os, signal
import time


try:


 # Set the listening port manually here if typing is not needed.
 # Remember in that case to comment out the below 'input' line for port.

 # PORT = 80

 # Prompt the user for the listening  port:

 PORT = int(input('\nEnter the port number to listen for TCP packets: '))


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

 # create a socket object
 serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

 # get local machine name
 host = socket.gethostname()

 # bind to the port
 serversocket.bind((host, PORT))

 # queue up to 5 requests
 serversocket.listen(5)

 print(f'\nWaiting for TCP packets on port {PORT} ...')

 while True:

    # establish a connection
    clientsocket, addr = serversocket.accept()

    print("\nGot a connection from %s" % str(addr))

    # receive data from the client
    try:
     data = clientsocket.recv(1024)
     print("Received a TCP packet: %s" % data.decode())
    except:
     print("Received a TCP packet with changed field values: %s" % data)

     # Define the field names for the TCP packet
     field_names = ['source_ip', 'destination_ip', 'source_port', 'destination_port', 'sequence_number', 'acknowledgment_number',
                    'data_offset', 'reserved', 'flags', 'window_size', 'checksum', 'urgent_pointer', 'options', 'payload']

     # Convert the raw byte TCP packet to plain text
     text = binascii.hexlify(data).decode('ascii')

     # Print the plain text representation of the TCP packet
     for i, field in enumerate(field_names):

      # Parse the IP addresses, ports, and payload
      if field in ['source_ip', 'destination_ip']:

       # Convert the hexadecimal representation to an IP address
       value = '.'.join(str(int(text[i*8+j:i*8+j+2], 16))
                        for j in range(0, 8, 2))

      elif field in ['source_port', 'destination_port']:

       # Convert the hexadecimal representation to a port number
       value = int(text[i*8:i*8+4], 16)

      elif field == 'payload':

       # Convert the hexadecimal representation of the payload to its ASCII representation
       value = binascii.unhexlify(text[i*8:(i+1)*8]).decode('ascii')

      else:

       # Keep the hexadecimal representation for other fields
       value = text[i*8:(i+1)*8]

      # Print the field name and value if it has a value

      if value:
       print('  {}: {}'.format(field, value))

     # strip off the leading "b'" and trailing "'" characters from the raw data
     datastring = str(data)
     datastring = datastring[2:-1]

     # find the last "\x00" occurence in the data to find payload section
     last_null_index = datastring.rfind("x00")

     # get the substring starting after the last "\x00" character
     output_str = datastring[last_null_index + 3:]

     # print the output
     print("  payload:", output_str)

     # send a thank you message to the client
     clientsocket.send(b'Thank you for connecting')

     # close the connection
     clientsocket.close()

except KeyboardInterrupt:
 print("\n")
 exit()

except:
 print('\nSomething went wrong, maybe the port number.\n')
 exit()
