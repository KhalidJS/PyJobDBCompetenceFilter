import Configuration.AppSettings

class ContentFilter:
    def __init__(self):
        self.readSQLFile = Configuration.AppSettings.AppSettings.SQL_Select_Annonce_Kompetence.value
        self.specifiedContent = ''

    def getSpecifiedContent(self):
        SQLQuery = open(self.readSQLFile).read()
        self.specifiedContent = SQLQuery
        return self.specifiedContent
