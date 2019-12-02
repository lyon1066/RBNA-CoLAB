# Rasberry PI IP address 192.168.88.229
# Pi chat program

import socket

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)