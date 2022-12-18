import MySQLdb as dbapi
import csv

dbServer='server'
dbPass='Root'
dbUser='Gustavo'

dbQuery='select * from table'

db=dbapi.connect(host=dbServer,user=dbUser,passwd=dbPass)
cur=db.cursor()
cur.execute(dbQuery)
result=cur.fetchall()

c = csv.writer(open("Q_1.csv","w"))
c.writerow(result)