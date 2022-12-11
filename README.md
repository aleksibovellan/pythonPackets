# pythonPackets v. 1.2

A collection of Python scrips ("sender and listener" pairs) for easy and fast transfering of any data across the internet using TCP and UDP packets created by Python.

Just by choosing the right pair of scripts, TCP or UDP packets can transfer any user data in an easy way. The "listener scripts" receive the data sent from the "sender scripts". Packets can be sent normally, or they can also be easily end-to-end encrypted using symmetric Fernet AES128 in CBC mode with SHA256 HMAC message authentication. When choosing to use the encryption script pairs, the symmetric shared password is written inside both files of the chosen pair and should be changed to a new one to enhance security.

The scripts have variables for TARGET_IP and PORT, which should be changed to real ones. Otherwise they will connect to 0.0.0.0 on port 80.

The "sender scripts" ask the data to be typed in when the scripts are launched, and then that data will get sent, but the script's functions can also be integrated into any other existing systems needing TCP or UDP connections or encryption.

These scripts run on Linux with 'sudo python3 script', but on MacOS the encryption-senders have to be launched with 'sudo python3.9 script'.
They also may require 'pip3 install cryptography'.

More information on Fernet encryption: https://github.com/fernet/spec/blob/master/Spec.md
