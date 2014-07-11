# Project Interpreter Version: 2.7.6
import MySQLdb
from warnings import filterwarnings

filterwarnings('ignore', category=MySQLdb.Warning)


class MySQL:
    def __init__(self, host='localhost', user='root', password='', port=3306, charset="utf8"):
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.charset = charset
        try:
            self.conn = MySQLdb.connect(host=self.host, port=self.port, user=self.user, passwd=self.password)
            self.conn.autocommit(True)
            self.conn.set_character_set(self.charset)
            self.cur = self.conn.cursor()
            self.createDdTable()
            self.greetUsers()
        except MySQLdb.Error as e:
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
            print("Mysql Error:%s\nSQL:%s" % (e, sql))

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
            print "inserted successfully"
            return n
        except MySQLdb.Error as e:
            print("Mysql Error:%s\nSQL:%s" % (e, sql))

    def greetUsers(self):
        print"""
----------------------------------------------------------------------------------------------
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


mysql = MySQL(password='fq930225')
while True:
    cmd = raw_input('>')
    if cmd == 'quit':
        break
    cmd = cmd.split(" ")
    if cmd[0] == 'query':
        num = mysql.query("select domainName,port from domaintest.domain_name where domainName=\'" + str(cmd[1]) + "\'")
        if num != 0:
            result = mysql.fetchRow()
            print 'domain name:' + result[0]
            print 'port:       ' + str(result[1])
    elif cmd[0] == 'register':
        mysql.insert("INSERT INTO domaintest.domain_name VALUES (" + cmd[1] + ");")
    else:
        print "your input has errors!"