# Import socket module 
import socket                
  
# Create a socket object 
s = socket.socket()          
  
# Define the port on which you want to connect 
port = 9001                
  
# connect to the server on local computer 
s.connect(('192.168.88.178', port)) 
  
# receive data from the server 
print (s.recv(1024)) 
# close the connection 
s.close()  