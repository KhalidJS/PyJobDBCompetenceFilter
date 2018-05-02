from Application import Application
import mysql.connector
import os
import time

if __name__ == '__main__':
    #app = Application.Application()
    #app.run()
    connection = mysql.connector.connect(user=os.environ['MYSQL_USER'], password=os.environ['MYSQL_PASSWORD'],
                                 host=os.environ['MYSQL_HOST'],
                                 database=os.environ['MYSQL_DATABASE'], port=os.environ['MYSQL_PORT'])
    curosr = connection.cursor()
    start = time.time()
    curosr.execute("SELECT a._id,a.title from JobDB.annonce as a WHERE a.body REGEXP '^.*Bioanalytiker.*$';")
    for row in curosr:
        print('%s %s' % (row[0],row[1]))
    elapsed = time.time() - start
    duration = time.strftime('%H:%M:%S', time.gmtime(elapsed))
    print('%s' % duration)
