# sender.py

# Sends a TCP packet from user input text to port 80
# Fill in TARGET_IP
# Run with python3

from socket import socket, AF_INET, SOCK_STREAM

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
send_message(message, 'TARGET_IP', 80)
