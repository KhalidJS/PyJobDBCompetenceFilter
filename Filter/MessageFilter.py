import sys
import datetime
from mysql.connector import connect, Error
from Channel import MessageEndPoint
import AppConfiguration.AppSettings


class MessageFilter:

    def __init__(self):
        self.messageEndpoint = MessageEndPoint.MessageEndPoint()
        self.user = AppConfiguration.AppSettings.AppSettings.user.value
        self.password = AppConfiguration.AppSettings.AppSettings.password.value
        self.host = AppConfiguration.AppSettings.AppSettings.host.value
        self.database = AppConfiguration.AppSettings.AppSettings.database.value
        self.port = AppConfiguration.AppSettings.AppSettings.port.value

    def retrieveDataFromDB(self, competence_id, competence, altLabel):
        self.singleSearch(competence_id=competence_id, searchstring=competence)
        if altLabel:
            labels = altLabel.split('/')
            for label in labels:
                self.singleSearch(competence_id=competence_id, searchstring=label)

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
            print(f'Problem occured {e.args} : ')
            connection.rollback()
        finally:
            cursor.close()
            connection.close()

    def singleSearch(self, competence_id, searchstring):
        global connection
        global cursor
        try:
            connection = connect(user=self.user, password=self.password,
                                 host=self.host,
                                 database=self.database, port=self.port)
            cursor = connection.cursor()
            cursor.execute(
                "SELECT _id,title,searchable_body,url from JobDB.annonce WHERE searchable_body REGEXP '[[:<:]]%s[[:>:]]';" % searchstring)
            self.messageEndpoint.setCompetenceID(competence_id)
            count = 0
            for _id, title, body, url in cursor:
                count += 1
                self.messageEndpoint.addAdvertID(_id)
                print("{%s} competence {%d} '%s' found at {%d}'%s' URL: %s" % (
                    datetime.datetime.now().strftime("%H:%M:%S"), competence_id, searchstring, _id, title, url))
            if count > 0:
                self.insertDataToDB(self.messageEndpoint)
                sys.stdout.flush()
        except Error as e:
            # If there is any case of error - Rollback
            print(e.args)
        finally:
            cursor.close()
            connection.close()
