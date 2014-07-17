# Project Interpreter Version: 2.7.6
import socket
import threading
import time


def tcpServer():
    global clientSocket
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind(('', 5778))
    serverSocket.listen(10)
    try:
        while True:
            clientSocket, (remoteHost, remotePort) = serverSocket.accept()
            print "[%s:%s] connected" % (remoteHost, remotePort)
            thread = HandleThread(remoteHost, clientSocket)
            thread.start()

    except BaseException, e:
        clientSocket.close()
        serverSocket.close()


class HandleThread(threading.Thread):
    def __init__(self, remoteHost, cSocket):
        threading.Thread.__init__(self)
        self.keepRunning = True
        self.remoteHost = remoteHost
        self.clientSocket = cSocket

    def run(self):
        while self.keepRunning and self.clientSocket is not None:
            msgFromClient = self.clientSocket.recv(1024)
            if not msgFromClient:
                print "connection end with :" + self.remoteHost
                break
            else:
                print "get message from thread:" + self.getName() + ":" + msgFromClient
            clientSocket.send(msgFromClient + " " + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

    def stopThread(self):
        self.keepRunning = False
        self.clientSocket.close()


tcpServer()