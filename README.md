# pythonPackets v. 1.3

## A useful collection of Python scrips ("sender and listener" pairs) for easy and fast transfering of text or data across the internet using just TCP and UDP packets created by Python. Includes also a custom TCP packet maker script for easy user-defined TCP packet field values to send.

Just by choosing the right pair of scripts, or script, you can use TCP or UDP packets to send any user data in an easy way.

For example, the "listener scripts" receive data sent from the "sender scripts". They ask the user to type in any relevant data when launched.

Packets can be sent normally, or they can also be easily end-to-end encrypted using symmetric Fernet AES128 in CBC mode with SHA256 HMAC message authentication. When choosing to use the encryption script pairs, you'll find the symmetric shared password already written inside both files of the chosen pair, and it should be changed to a new one before usage to enhance security.

Inside the scripts are variables for TARGET_IP and PORT, which can be changed into preferred static ones. Otherwise, the scripts ask to type in the IP address and port number manually everytime when launched.

These scripts run on Linux with 'sudo python3 script'. On MacOS, the encryption-senders have to be launched with 'sudo python3.9 script'.

May require 'pip3 install cryptography', and 'sudo apt install scapy' or "sudo apt install python3-scapy'.

## IMPORTANT: The most usual reasons for errors and crashes are:
- running Apache2 or some other webserver on port 80 at the same time
- conflicting firewall settings locally, or between the two points
- failing to install the suggested libraries above

These script's functions could also be integrated into some other existing systems needing TCP or UDP connections and/or encryption.

For more information on Fernet encryption: https://github.com/fernet/spec/blob/master/Spec.md
