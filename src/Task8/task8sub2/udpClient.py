import socket


def udpClient():
    address = ('localhost', 7890)
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print "enter quit to exit"
    while True:
        sendMessage = raw_input()
        clientSocket.sendto(sendMessage, address)
        if sendMessage == "quit":
            break
        print clientSocket.recvfrom(1024)[0]
    clientSocket.close()


udpClient()