import socket
import threading


def tcpServer():
    global clientSocket
    i = 0
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind(('', 5778))
    serverSocket.listen(10)
    try:
        while True:
            clientSocket, (remoteHost, remotePort) = serverSocket.accept()
            i += 1
            print "[%s:%s] connected" % (remoteHost, remotePort)
            thread = HandleThread("thread" + str(i), clientSocket)
            thread.start()

    except BaseException, e:
        clientSocket.close()
        serverSocket.close()


class HandleThread(threading.Thread):
    def __init__(self, name, cSocket):
        threading.Thread.__init__(self, name=name)
        self.keepRunning = True
        self.clientSocket = cSocket

    def run(self):
        while self.keepRunning:
            msgFromClient = self.clientSocket.recv(1024)
            print "get message from thread:" + self.getName() + ":" + msgFromClient
            if msgFromClient == "quit":
                self.keepRunning = False
                break
            self.clientSocket.send(msgFromClient + "by server")

    def stopThread(self):
        self.keepRunning = False
        self.clientSocket.close()


tcpServer()

# name = "abc"
# thread1 = ServerThread(name)
# thread1.start()
