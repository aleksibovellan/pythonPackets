# pythonPackets v. 1.3

A useful collection of Python scrips ("sender and listener" pairs) for easy and fast transfering of any data across the internet using just TCP and UDP packets created from Python.

Just by choosing the right pair of scripts, you can use TCP or UDP packets to send any user data in an easy way.

The "listener scripts" receive the data sent from the "sender scripts". Packets can be sent normally, or they can also be easily end-to-end encrypted using symmetric Fernet AES128 in CBC mode with SHA256 HMAC message authentication. When choosing to use the encryption script pairs, you'll find the symmetric shared password already written inside both files of the chosen pair, and it should be changed to a new one to enhance security.

The scripts have variables for TARGET_IP and PORT, which can be changed into preferred ones. Otherwise, the scripts ask to type in the IP address and port number manually when run.

The script's functions could also be integrated into some other existing systems needing TCP or UDP connections and/or encryption.

These scripts run on Linux with 'sudo python3 script'. On MacOS, the encryption-senders have to be launched with 'sudo python3.9 script'.

The scripts may require 'pip3 install cryptography', and 'sudo apt install scapy' or "sudo apt install python3-scapy'.

More information on Fernet encryption: https://github.com/fernet/spec/blob/master/Spec.md
