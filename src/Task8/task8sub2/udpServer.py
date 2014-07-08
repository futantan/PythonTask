import socket
import time


def udpServer():
    address = ('localhost', 7890)
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    serverSocket.bind(address)

    while True:
        data, clientAddr = serverSocket.recvfrom(1024)
        if data == "quit":
            break
        serverSocket.sendto((data + " " + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))), clientAddr)
    serverSocket.close()


udpServer()