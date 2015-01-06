#-*- coding:utf-8 -*-
'''
    @author:cuirqiang
    @date:2015-01-06
    @filename:readPic.py
'''
import MySQLdb as mdb
import sys

con = None
try:
    con = mdb.connect(host='localhost',user='root',passwd='123456',db='py')
    cur = con.cursor()
    cur.execute("SELECT Data FROM Images LIMIT 1")
    fout = open('Screenshot1.png','wb')
    fout.write(cur.fetchone()[0])
    fout.close()
    cur.close()
    con.close()
except mdb.Error,e:
    print "Error %d: %s" % (e.args[0],e.args[1])
    sys.exit(1)
