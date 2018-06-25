import sys
import datetime
from mysql.connector import connect, Error
from Channel import MessageEndPoint
from AppConfiguration.AppSettings import AppSettings


class MessageFilter:

    def __init__(self):
        self.messageEndpoint = MessageEndPoint.MessageEndPoint()
        self.user = AppSettings.user.value
        self.password = AppSettings.password.value
        self.host = AppSettings.host.value
        self.database = AppSettings.database.value
        self.port = AppSettings.port.value

    def retrieveDataFromDB(self, competence_id, searchPatterns):
        self.messageEndpoint.advertID = []
        self.messageEndpoint.setCompetenceID(competence_id)
        if searchPatterns:
            searchEntries = searchPatterns.split('/')
            for searchEntry in searchEntries:
                self.singleSearch(searchstring=searchEntry)

    def insertDataToDB(self, messageEndPoint):
        competenceID = messageEndPoint.getcompetenceID()
        global connection
        global cursor
        try:
            connection = connect(user=self.user, password=self.password,
                                 host=self.host,
                                 database=self.database, port=self.port)
            cursor = connection.cursor()
            query = 'insert ignore into annonce_kompetence (annonce_id,kompetence_id) values'
            first = True
            for _id in self.messageEndpoint.getadvertID():
                if not first:
                    query += ','
                first = False
                query += "(%d,%d)" % (_id, competenceID)
            # print(query)
            print('{%s}: Inserting data into database' % datetime.datetime.now().strftime('%H:%M:%S'))
            cursor.execute(query)
            connection.commit()
        except Error as e:
            # If there is any case of error - Rollback
            print('An error has occurred', e.args)
            connection.rollback()
        finally:
            cursor.close()
            connection.close()

    def singleSearch(self, searchstring):
        global connection
        global cursor
        try:
            connection = connect(user=self.user, password=self.password,
                                 host=self.host,
                                 database=self.database, port=self.port)
            cursor = connection.cursor()
            query = "SELECT _id,title,searchable_body,url from JobDB.annonce a WHERE searchable_body REGEXP '%s'"
            if (AppSettings.advert.value):
                query += (" AND a._id="+AppSettings.advert.value)
            cursor.execute(query % searchstring)
            count = 0
            for _id, title, body, url in cursor:
                count += 1
                self.messageEndpoint.addAdvertID(_id)
                print("{%s} competence {%d} '%s' found at {%d}'%s' URL: %s" % (
                    datetime.datetime.now().strftime("%H:%M:%S"), self.messageEndpoint.getcompetenceID(), searchstring, _id, title, url))
            if count > 0:
                self.insertDataToDB(self.messageEndpoint)
                sys.stdout.flush()
        except Error as e:
            # If there is any case of error - Rollback
            print(e.args)
        finally:
            cursor.close()
            connection.close()
