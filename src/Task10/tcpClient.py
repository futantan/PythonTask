import socket


def tcpClient():
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect(("localhost", 5778))
    print "enter quit to exit"
    sendMessage = ""
    while sendMessage != "quit":
        sendMessage = raw_input('>')
        clientSocket.send(sendMessage)
        if sendMessage == "quit":
            break
        print clientSocket.recv(1024)
    clientSocket.send(sendMessage)
    clientSocket.close()


tcpClient()