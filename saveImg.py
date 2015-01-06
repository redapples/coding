coding
======
#-*- coding:utf-8 -*-
'''
    @author:cuirqiang
    @date:2015-01-06
    @filename:savePic.py
'''
import MySQLdb as mdb
import sys

con = None

try:
    fin = open("Screenshot.png")
    img = fin.read()
    fin.close()
except IOError,e:
    print "Error %d: %s" %(e.args[0],e.args[1])
    sys.exit(1)
try:
    con = mdb.connect(host='localhost',user='root',passwd='123456',db='py')
    cur = con.cursor()
    cur.execute("CREATE TABLE Images( \
               Id INT PRIMARY KEY AUTO_INCREMENT,Data MEDIUMBLOB)")
    cur.execute("INSERT INTO Images SET Data='%s'" % mdb.escape_string(img))
    con.commit()
    cur.close()
    con.close()
except mdb.Error,e:
    print "Error %d: %s" % (e.args[0],e.args[1])
    sys.exit(1)
