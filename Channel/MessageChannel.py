import datetime
import time
from mysql.connector import connect, ProgrammingError, Error
from Filter import ContentFilter, MessageFilter


class MessageChannel:

    def __init__(self):
        # variables
        self.content = ContentFilter.ContentFilter()
        self.messagefilter = MessageFilter.MessageFilter()

    def fetchAndFilterDataFromDB(self, user, password, host, database, port):
        # connecting to Mysql server
        global connection
        global cursor
        try:
            connection = connect(user=user, password=password, host=host, database=database, port=port)
            print('Connecting to hostname: %s  with port: %s' % (connection.server_host, connection.server_port))
            print('successfully connected to hostname: %s\n' % connection.server_host)
            print('Fetch for data and filter started: {%s}\n' % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            cursor = connection.cursor()
            cursor.execute(self.content.getSpecifiedContent())
            startTimer = time.time()
            for competence_ID, competence, altLabels in cursor:
                self.messagefilter.retrieveDataFromDB(competence_ID, competence, altLabels)
            elapsed = time.time() - startTimer
            duration = time.strftime('%H:%M:%S', time.gmtime(elapsed))
            print('Took: %s' % duration)
        except Error as e:
            print('An error has occurred', e.args)
        except ProgrammingError as p:
            print(p.args)
        finally:
            cursor.close()
            connection.close()
