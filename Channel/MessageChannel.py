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
                self.messagefilter.DBRegExp(competence_ID,competence)
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
