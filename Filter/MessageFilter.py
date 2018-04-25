import regex
from bs4 import BeautifulSoup


class MessageFilter:
    def __init__(self):
        self.removeSpaces = regex.compile(r'\s+')
        self.advertID = 0
        self.competenceID = 0

    def checkMatchForJobAdvertAndCompetence(self, advertID, competenceID, advertbody, competencetitle):
        convertFromBlobToString = str(advertbody)
        soup = BeautifulSoup(convertFromBlobToString, 'html.parser')
        removeUnwantedData = soup.contents[0]
        messagebody = regex.sub(self.removeSpaces, ' ', removeUnwantedData)
        # match = regex.search(r'(' + competencetitle + '){1}',messagebody,regex.IGNORECASE | regex.MULTILINE)
        match = regex.search(r'\b(Specific Text)\b{1}', messagebody, regex.IGNORECASE)
        if match:
            self.advertID = advertID
            self.competenceID = competenceID
            print('MAtch on:' + str(advertID))
            return True
        else:
            # print('No Match')
            return False
