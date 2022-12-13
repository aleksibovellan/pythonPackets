# pythonPackets v.1.3
# tcp-sender.py
#
# Aleksi Bovellan
#
# Sends a TCP packet from user input text to any IP address and port set below.
# Run with 'sudo python3 tcp-sender.py'


from socket import socket, AF_INET, SOCK_STREAM


try:


 # Set the destination IP address and port manually here if typing is not needed.
 # Remember in that case to comment out the below 'input' lines for IP and port.

 # TARGET_IP = '127.0.0.1'
 # PORT = 80

 # Prompt the user for the destination IP address and port:

 TARGET_IP = input('\nEnter the IP address where to send the TCP packet: ') 
 PORT = int(input('Enter the port number: '))


 # Prompt the user for the message to send:

 message = input("\nEnter the message to be sent in the TCP packet's payload field: ")


 # ---------------------------------
 

 # Send the message to the target IP address and port


 def send_message(message, target_ip, target_port):
     try:
         print("\nTrying to connect to destination ...")
         with socket(AF_INET, SOCK_STREAM) as s:
             s.connect((target_ip, target_port))
             s.sendall(message.encode())
             print("\nTCP packet was sent!\n")
     except ConnectionRefusedError as error:
         print("\nCould not create a connection.\n")
     except:
         print("\nCould not create a connection.\n")

except KeyboardInterrupt:
    print("\n")
    exit()
except:
    print('\nSomething went wrong, maybe the target values.\n')
    exit()

# Run program.
send_message(message, TARGET_IP, PORT)
