# Project Interpreter Version: 2.7.6
import socket
from sys import argv
import threading
import MySQLdb
from warnings import filterwarnings

# ignore warnings from MySQL
filterwarnings('ignore', category=MySQLdb.Warning)

passWord = None


def tcpServer():
    global clientSocket
    i = 0
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind(('', 5778))
    serverSocket.listen(10)
    testThread = HandleThread("testThread", None)
    testThread.start()
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
        self.mysql = MySQL(password=passWord, socket=cSocket)
        self.keepRunning = True
        self.clientSocket = cSocket

    def run(self):
        while self.keepRunning and self.clientSocket is not None:
            msgFromClient = self.clientSocket.recv(1024)
            print "get message from thread:" + self.getName() + ":" + msgFromClient
            if msgFromClient == "quit":
                self.keepRunning = False
                break
            msgFromClient = msgFromClient.split(" ")
            if msgFromClient[0] == 'query':
                num = self.mysql.query("select domainName,port from domaintest.domain_name where domainName=\'" + str(
                    msgFromClient[1]) + "\'")
                if num != 0:
                    result = self.mysql.fetchRow()
                    print 'domain name:' + result[0]
                    print 'port:       ' + str(result[1])
                    self.clientSocket.send('domain name:' + result[0] + '\n' + 'port:       ' + str(result[1]))
                else:
                    print("no data found!")
                    self.clientSocket.send('no data matches!')
            elif msgFromClient[0] == 'register':
                self.mysql.insert("INSERT INTO domaintest.domain_name VALUES (" + msgFromClient[1] + ");")
            else:
                print "your input has errors!"
                self.clientSocket.send("your input has errors!")

    def stopThread(self):
        self.keepRunning = False
        self.clientSocket.close()


class MySQL:
    def __init__(self, host='localhost', user='root', password='', port=3306, charset="utf8", socket=None):
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.charset = charset
        self.socket = socket
        try:
            self.conn = MySQLdb.connect(host=self.host, port=self.port, user=self.user, passwd=self.password)
            self.conn.autocommit(True)
            self.conn.set_character_set(self.charset)
            self.cur = self.conn.cursor()
            self.createDdTable()
            self.greetUsers()
        except MySQLdb.Error as e:
            log = "Mysql Error %d: %s" % (e.args[0], e.args[1])
            if self.socket is not None:
                self.socket.send(log)
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))

    def __del__(self):
        """close sth safely when you do not need them"""
        self.cur.close()
        self.conn.close()

    def createDdTable(self):
        self.cur.execute('CREATE DATABASE IF NOT EXISTS domaintest')
        self.cur.execute(
            'CREATE TABLE IF NOT EXISTS domaintest.domain_name (domainName VARCHAR(30) UNIQUE , port INT);')

    def query(self, sql):
        """ return the number of data, you can use fetchRow then to get the content of data"""
        try:
            n = self.cur.execute(sql)
            return n
        except MySQLdb.Error as e:
            log = "Mysql Error:%s\nSQL:%s" % (e, sql)
            if self.socket is not None:
                self.socket.send(log)
            print(log)

    def fetchRow(self):
        """get the data you have just queried"""
        result = self.cur.fetchone()
        return result

    def insert(self, sql):
        """inset the data into table
        data looks like: 'www.abc.com',9997
        """
        try:
            n = self.cur.execute(sql)
            if self.socket is not None:
                self.socket.send("inserted successfully")
            print "inserted successfully"
            return n
        except MySQLdb.Error as e:
            log = "Mysql Error:%s\nSQL:%s" % (e, sql)
            if self.socket is not None:
                self.socket.send(log)
            print("Mysql Error:%s\nSQL:%s" % (e, sql))

    def greetUsers(self):
        greeting = """----------------------------------------------------------------------------------------------
Hello, you have connected to the domain service successfully.
Welcome to use this domain system. You can use the Following command to interact with the system.
1. Search for domain:
Attention: put the 'query' before the domain you want to search
>query www.baidu.com
2. Register a domain name:
Attention: do not forget wrap your domain name with ', then the port
>register 'www.baidu.com',1234
3. press: quit to exit
>quit
----------------------------------------------------------------------------------------------"""
        if self.socket is not None:
            self.socket.send(greeting)
        print greeting


if len(argv) == 2:
    script, passWord = argv
    tcpServer()
else:
    # if the parameter is not correct, then exit
    print "your script is incorrect, please check it."
    exit()