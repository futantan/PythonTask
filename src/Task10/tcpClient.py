# Project Interpreter Version: 2.7.6
import socket


def tcpClient():
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect(("localhost", 5778))
    print clientSocket.recv(1024)
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