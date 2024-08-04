# Import socket module
from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)
# Prepare a server socket
# Fill in start
serverSocket.bind(('localhost', 6789))
serverSocket.listen(1)
# Fill in end
import os
while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()

    try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1].decode()  # Decode the bytes to a string

        f = open(filename[1:])
        outputdata = f.read()
        f.close()

        # Send one HTTP header line into the socket
        # Fill in start
        connectionSocket.send(b"HTTP/1.1 200 OK\r\n\r\n")
        # Fill in end

        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.close()

    except IOError:
        # Send response message for file not found
        # Fill in start
        connectionSocket.send(b"HTTP/1.1 404 Not Found\r\n\r\n")
        connectionSocket.send(b"<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n")
        # Fill in end

        # Close client socket
        # Fill in start
        connectionSocket.close()
        # Fill in end

serverSocket.close()
