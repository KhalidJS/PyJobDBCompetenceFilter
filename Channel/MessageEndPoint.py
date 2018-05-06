class MessageEndPoint:
    def __init__(self):
        self.advertID = ''
        self.competenceID = ''

    def storeIDs(self,advertID,competenceID):
        self.advertID = advertID
        self.competenceID = competenceID

    def getadvertID(self):
        return self.advertID

    def getcompetenceID(self):
        return self.competenceID
