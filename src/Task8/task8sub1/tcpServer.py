import socket
import time

# here we did not use thread to handle a coming connection,
# so wo only communicate with a single client


def tcpServer():
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind(('', 5777))
    serverSocket.listen(1)
    clientSocket, (remoteHost, remotePort) = serverSocket.accept()
    print "[%s:%s] connected" % (remoteHost, remotePort)

    while True:
        messageFromClient = clientSocket.recv(1024)
        print "" + messageFromClient
        if messageFromClient == "quit":
            break
        clientSocket.send(messageFromClient + " " + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

    clientSocket.close()
    serverSocket.close()


tcpServer()
