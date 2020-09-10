
from socket import *   #for sockets
import time
import sys  #for exit

#We will create a socket, connect to gmail server


#create an AF_INET, STREAM socket (TCP)
s = socket(AF_INET,SOCK_STREAM)
 
print ('Socket Created\n')


dest_host = sys.argv[1]
dest_port = int(sys.argv[2]) # for https

s.connect((dest_host , dest_port))

message = "GET /"+ sys.argv[3]+" HTTP/1.1\r\n\r\n"  

try :
    #Set the whole string
    s.sendall(message.encode()) #python3 converts string into bytes
except error:
    #Send failed
    print ('Send failed')
    sys.exit()

print ('Message sent successfully')

#Receive Response
reply = s.recv(4096)#It must take a parameter which is the max size in bytes of the recieved message, generally a power of 2 

print(reply.decode())

s.close()