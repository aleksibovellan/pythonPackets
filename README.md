# pythonPackets

A collection of Python scrips ("senders and listeners") for easy and fast transfering of any data across the internet using TCP and UDP packets.

Just by choosing the right pair of scripts, TCP and UDP packets can travel normally, or they can be end-to-end encrypted using symmetric Fernet AES128 in CBC mode with SHA256 HMAC message authentication. When choosing encryption scripts, the shared password is written inside both files of the chosen pair and should be updated to a new one.

They run on Linux with 'sudo python3 script', but on MacOS the encryption-senders have to be launched with 'sudo python3.9 script'.
Also may require 'pip3 install cryptography'.

More information on Fernet encryption: https://github.com/fernet/spec/blob/master/Spec.md

