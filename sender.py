# pythonPackets v.1.0
# sender.py
#
# Aleksi Bovellan
#
# Sends a TCP packet from user input text to any IP and port.
# Run with 'sudo python3 sender.py'

# Set the destination IP address and port

from socket import socket, AF_INET, SOCK_STREAM
TARGET_IP = '0.0.0.0'
PORT = 80


# Prompt the user for the message to send
message = input('\nEnter the message to send: ')

# Send the message to the target IP address and port


def send_message(message, target_ip, target_port):
    try:
        with socket(AF_INET, SOCK_STREAM) as s:
            s.connect((target_ip, target_port))
            s.sendall(message.encode())
            print("\nThe packet was sent!\n")
    except ConnectionRefusedError as error:
        print("\nCould not create a connection.\n")
    except:
        print("\nCould not create a connection.\n")


# Example usage
send_message(message, TARGET_IP, PORT)
