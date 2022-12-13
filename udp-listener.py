# pythonPackets v.1.3
# udp-listener.py
#
# Aleksi Bovellan
#
# Listens for UDP packets on port set below.
# Run with 'sudo python3 udp-listener.py'


import socket
import time
import os, signal


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

 # Create a UDP socket
 sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

 # Bind the socket to the target IP and port
 sock.bind(('', PORT))

 print(f'\nWaiting for UDP packets on port {PORT} ...')

 try:
  while True:
   # Receive the UDP packet
   data, addr = sock.recvfrom(1024)

   # Print the UDP packet in plain text
   print(f"\nGot a connection from {addr}")
   print("Received UDP packet: " + data.decode())

 except KeyboardInterrupt:
  print("\n")
  # Close the socket
  sock.close()
  exit()

except KeyboardInterrupt:
 print("\n")
 exit()

except:
 #print("\nSomething went wrong, maybe the port number\n")
 print("")
 exit()
