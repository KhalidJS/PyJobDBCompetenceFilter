import regex
import os
from bs4 import BeautifulSoup
import datetime
import time
from mysql.connector import connect, Error


class MessageFilter:
    def __init__(self):
        self.removeSpaces = regex.compile(r'\s+')
        self.advertID = 0
        self.competenceID = 0
        self.URL = ''
        self.advert_title = ''

    def checkMatchForJobAdvertAndCompetence(self, competenceTitle, advertBody):
        convertFromBlobToString = str(advertBody)
        self.DBRegExp(competenceTitle, advertBody)

    def getadvertID(self):
        return self.advertID

    def getcompetenceID(self):
        return self.competenceID

    def setAdvertTitleAndURL(self, advertTitle, advertURL):
        self.advert_title = advertTitle
        self.URL = advertURL

    def setAdvertIDAndCompetenceID(self, advertID, competenceID):
        self.advertID = advertID
        self.competenceID = competenceID

    def DBRegExp(self, competence_ID,competence):
        try:
            # connection = connect(option_files=option_files, option_groups=option_groups)
            connection = connect(user=os.environ['MYSQL_USER'], password=os.environ['MYSQL_PASSWORD'],
                                 host=os.environ['MYSQL_HOST'],
                                 database=os.environ['MYSQL_DATABASE'], port=os.environ['MYSQL_PORT'])
            cursor = connection.cursor()
            # print('{%s}: Inserting data into database' % datetime.datetime.now().strftime('%H:%M:%S'))
            cursor.execute(
                "SELECT _id,title,searchable_body,url from JobDB.annonce WHERE searchable_body REGEXP '%s';" % competence)
            for id, title, body, url in cursor:
                print("{%s} competence '%s' fount at '%s' URL: %s" % (datetime.datetime.now().strftime("%H:%M:%S"),competence, title,url))
                self.setAdvertIDAndCompetenceID(advertID=id,competenceID=competence)
        except Error as e:
            # If there is any case of error - Rollback
            print(e.args)
            #connection.rollback()
        finally:
            cursor.close()
            connection.close()

