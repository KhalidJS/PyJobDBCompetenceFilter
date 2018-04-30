from mysql.connector import connect, ProgrammingError
import time
from Filter import ContentFilter, MessageFilter
from Channel import MessageEndPoint
import datetime


class MessageChannel:

    def __init__(self):
        # variables
        self.content = ContentFilter.ContentFilter()
        self.messagefilter = MessageFilter.MessageFilter()
        self.messageEndPoint = MessageEndPoint.MessageEndPoint()

    def fetchAndFilterDataFromDB(self, option_file, option_groups):
        # connecting to Mysql server
        try:
            connection = connect(option_files=option_file, option_groups=option_groups)
            print('Connecting to hostname: %s  with port: %s' % (connection.server_host, connection.server_port))
            print('successfully connected to hostname: %s\n' % connection.server_host)
            print('Fetch for data and filter started: {%s}\n' % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            cursor = connection.cursor()
            cursor.execute(self.content.getSpecifiedContent())
            startTimer = time.time()
            for comptence_ID, advert_ID, competence, advert_blobtext, advert_title, advert_url in cursor:
                if self.messagefilter.checkMatchForJobAdvertAndCompetence(competenceTitle=competence,
                                                                          advertBody=advert_blobtext):
                    self.messagefilter.setAdvertIDAndCompetenceID(advertID=advert_ID, competenceID=comptence_ID)
                    self.messagefilter.setAdvertTitleAndURL(advertTitle=advert_title, advertURL=advert_url)
                    self.messageEndPoint.storeIDs(self.messagefilter.getadvertID(),
                                                  self.messagefilter.getcompetenceID())
                    self.insertDataToDB(self.messageEndPoint)
                    # file = open('T.txt','a')
                    # file.write(str(self.messageEndPoint.getadvertID()) + ' : ' + str(self.messageEndPoint.getcompetenceID()) + '\n')

            elapsed = time.time() - startTimer
            duration = time.strftime('%H:%M:%S', time.gmtime(elapsed))
            print('Took: %s' % duration)
        except ProgrammingError as e:
            print(e.args)
        finally:
            pass
            # cursor.close()
            # connection.close()

    def insertDataToDB(self, messageEndPoint):
        advertID = messageEndPoint.getadvertID()
        competenceID = messageEndPoint.getcompetenceID()
        # file = open('t.txt','w')
        # file.write(str(advertID) + str(competenceID))
        try:
            # connection = connect(option_files=option_files, option_groups=option_groups)
            connection = connect(user='root', host='localhost', password='?', database='sys')
            cursor = connection.cursor()
            print('{%s}: Inserting data into database' % datetime.datetime.now().strftime('%H:%M:%S'))
            cursor.execute('insert into annonce_kompetence values (%s,%s)' % (advertID, competenceID))
            connection.commit()
        except:
            # If there is any case of error - Rollback
            connection.rollback()
        finally:
            cursor.close()
            connection.close()

    def getMessageEndPoint(self):
        return self.messageEndPoint
