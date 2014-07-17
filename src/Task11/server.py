# coding=utf-8
# Project Interpreter Version: 2.7.6
import socket
import threading
import time
import sys

reload(sys)
sys.setdefaultencoding('utf8')


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
            print "get message from thread:" + self.remoteHost + ":" + msgFromClient.rstrip('\n')
            clientSocket.send(
                msgFromClient.rstrip('\n') + " " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '\n')
        self.clientSocket.close()

    def stopThread(self):
        self.keepRunning = False
        self.clientSocket.close()


tcpServer()