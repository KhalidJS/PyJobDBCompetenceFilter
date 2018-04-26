import regex
from bs4 import BeautifulSoup
import datetime
import time


class MessageFilter:
    def __init__(self):
        self.removeSpaces = regex.compile(r'\s+')
        self.advertID = 0
        self.competenceID = 0
        self.URL = ''
        self.advert_title = ''

    def checkMatchForJobAdvertAndCompetence(self,competenceTitle,advertBody):
        convertFromBlobToString = str(advertBody)
        soup = BeautifulSoup(convertFromBlobToString, 'html.parser')
        removeUnwantedData = soup.contents[0]
        messagebody = regex.sub(self.removeSpaces, ' ', removeUnwantedData)
        match = regex.search(r'(' + competenceTitle + '){1}',messagebody,regex.IGNORECASE | regex.MULTILINE)
        #match = regex.search(r'leder{1}', messagebody, regex.IGNORECASE)
        if match:
            print("{%s} Competence: '%s' was found at: %s: %s" % (datetime.datetime.now().strftime('%H:%M:%S'),competenceTitle,self.advert_title,self.URL))
            return True
        else:
            # print('No Match')
            return False

    def getadvertID(self):
        return self.advertID

    def getcompetenceID(self):
        return self.competenceID

    def setAdvertTitleAndURL(self,advertTitle,advertURL):
        self.advert_title = advertTitle
        self.URL = advertURL

    def setAdvertIDAndCompetenceID(self,advertID,competenceID):
        self.advertID = advertID
        self.competenceID = competenceID
