import MySQLdb

try:
    conn = MySQLdb.connect(host='localhost', user='root', passwd='930225', port=3306)
    cur = conn.cursor()

    cur.execute("create database if not exists domain")
    conn.select_db('domain')
    # cur.execute('create table')
    cur.execute("CREATE TABLE IF NOT EXISTS \
        domaintable(Id INT PRIMARY KEY AUTO_INCREMENT, DomainName VARCHAR(50),DomainPort INT)")

    cur.execute("drop table if exists Writers")
    cur.close()
    conn.close()

except MySQLdb.Error, e:
    print "Mysql Error %d: %s" % (e.args[0], e.args[1])