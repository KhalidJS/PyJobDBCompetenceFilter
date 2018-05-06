import datetime
import time
import os
import sys
from mysql.connector import connect, ProgrammingError,Error
from Channel import MessageEndPoint
from Filter import ContentFilter, MessageFilter


class MessageChannel:

    def __init__(self):
        # variables
        self.content = ContentFilter.ContentFilter()
        self.messagefilter = MessageFilter.MessageFilter()
        self.messageEndPoint = MessageEndPoint.MessageEndPoint()

    def fetchAndFilterDataFromDB(self, option_file, option_groups):
        # connecting to Mysql server
        try:
            connection = connect(user=os.environ['MYSQL_USER'], password=os.environ['MYSQL_PASSWORD'],
                                 host=os.environ['MYSQL_HOST'],
                                 database=os.environ['MYSQL_DATABASE'], port=os.environ['MYSQL_PORT'])
            print('Connecting to hostname: %s  with port: %s' % (connection.server_host, connection.server_port))
            print('successfully connected to hostname: %s\n' % connection.server_host)
            print('Fetch for data and filter started: {%s}\n' % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            cursor = connection.cursor()
            cursor.execute(self.content.getSpecifiedContent())
            startTimer = time.time()
            for competence_ID,competence in cursor:
                #print('Now filtering on %d' % c_ID)
                self.messagefilter.DBRegExp(competence_ID,competence)
                self.messageEndPoint.storeIDs(self.messagefilter.getadvertID(),self.messagefilter.getcompetenceID())
                # self.insertDataToDB(messageEndPoint=self.messageEndPoint)
                # Det tager 21:55 minutter om at køre og matche kompetencen med searchable_body
                sys.stdout.flush()
            elapsed = time.time() - startTimer
            duration = time.strftime('%H:%M:%S', time.gmtime(elapsed))
            print('Took: %s' % duration)
        except ProgrammingError as e:
            print(e.args)
        finally:
            cursor.close()
            connection.close()

    def insertDataToDB(self, messageEndPoint):
        advertID = messageEndPoint.getadvertID()
        competenceID = messageEndPoint.getcompetenceID()
        # file = open('t.txt','w')
        # file.write(str(advertID) + str(competenceID))
        try:
            # connection = connect(option_files=option_files, option_groups=option_groups)
            connection = connect(user=os.environ['MYSQL_USER'], password=os.environ['MYSQL_PASSWORD'],
                                 host=os.environ['MYSQL_HOST'],
                                 database=os.environ['MYSQL_DATABASE'], port=os.environ['MYSQL_PORT'])
            cursor = connection.cursor()
            print('{%s}: Inserting data into database' % datetime.datetime.now().strftime('%H:%M:%S'))
            cursor.execute(self.content.getspecifiedContentFromDBToInsert() + '(%s,%s)' % (advertID, competenceID))
            connection.commit()
        except Error as e:
            # If there is any case of error - Rollback
            print('Problem occured %s : ' % e.args)
            connection.rollback()
        finally:
            cursor.close()
            connection.close()

    def getMessageEndPoint(self):
        return self.messageEndPoint
