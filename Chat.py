# CoLAB paired programming code 2019
#
# This code is from paired programming workshops
# --Verified first step, need to add next steps for chat function
#
# Contact John T Haworth for questions

# read ip address of the raspberry pi
import socket
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP
host_ip = get_ip()
print (host_ip)  # '192.168.88.229'