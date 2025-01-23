""" 
Create a socket program to connect to a predefined server (try https://iitj.ac.in/ use others
too).

AF_INET : IPv4 address Family
SOCK_STREAM : Connection-oriented TCP Protocol
"""

import socket
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created successfully")
except socket.error as e:
    print(f"Socket Creation failed with error: {e}")

## Finding the IP of iitj.ac.in
dest_ip = socket.gethostbyname("www.iitj.ac.in")

port = 80
s.connect((dest_ip, port))

print("Connected succesfully!")