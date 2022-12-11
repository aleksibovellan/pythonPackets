# pythonPackets v. 1.2

A collection of Python scrips ("senders and listeners") for easy and fast transfering of any data across the internet using TCP and UDP packets.

Just by choosing the right pair of scripts, TCP and UDP packets can be sent normally, or they can easily be end-to-end encrypted using symmetric Fernet AES128 in CBC mode with SHA256 HMAC message authentication. When choosing to use the encryption script pairs, the symmetric shared password is written inside both files of the chosen pair and should be changed to a new one when used to enhance security.

The scripts have variables for TARGET_IP and PORT, which should be changed to real ones.

The sender scripts ask the data to be typed in when they are launched, and then that data will get sent, but the scripts can also be integrated into any other existing systems needing TCP or UDP connections with Python.

These scripts run on Linux with 'sudo python3 script', but on MacOS the encryption-senders have to be launched with 'sudo python3.9 script'.
They also may require 'pip3 install cryptography'.

More information on Fernet encryption: https://github.com/fernet/spec/blob/master/Spec.md
