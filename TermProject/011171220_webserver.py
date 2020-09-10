# import socket module
from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)
# Prepare a sever socket
# Fill in start
host = '127.0.0.1'
port = 80  # for https
print('Ready to serve...')


serverSocket.bind((host, port))
serverSocket.listen(5)   # Sets socket to listening state with a queue

print("Listening for connections.. ")

# Fill in end
while True:
    # Establish the connection
    connectionSocket, addr = serverSocket.accept()

    try:
        message = connectionSocket.recv(1024)  # Fill in start #Fill in end
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()# Fillinstart#Fillinend
        # SendoneHTTPheaderlineintosocket
        # Fill instart
        connectionSocket.send('HTTP/1.0 200 OK\r\n\r\n'.encode())
        # Fill in end
        #Sendthecontentoftherequestedfiletotheclient
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.close()
    except IOError:
         # Send response message for file not found
         # Fill in start
         connectionSocket.send("HTTP/1.0 404 OK\r\n\r\n".encode())
         # Fill in end
         # Close client socket
         # Fill in start
         connectionSocket.close()
         # Fill in end
serverSocket.close()
