from mysql.connector import connect,ProgrammingError
import time
from Filter import ContentFilter,MessageFilter
from Channel import MessageEndPoint

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
            cursor = connection.cursor()
            print('successfully connected')
            cursor.execute(self.content.getSpecifiedContent())
            startTimer = time.time()
            for kom_id, ann_id, preflabel, ann_body in cursor:
                if self.messagefilter.checkMatchForJobAdvertAndCompetence(ann_id,kom_id,ann_body, preflabel):
                   self.messageEndPoint.storeIDs(self.messagefilter.advertID,self.messagefilter.competenceID)
            elapsed = time.time() - startTimer
            duration = time.strftime('%H:%M:%S', time.gmtime(elapsed))
            print('Took: %s' % duration)
        except ProgrammingError as e:
            print(e.args)
        finally:
            cursor.close()
            connection.close()



    def insertDataToDB(self,):
        # later
        pass