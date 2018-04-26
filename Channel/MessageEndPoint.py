class MessageEndPoint:
    def __init__(self):
        self.advertID = 0
        self.competenceID = 0

    def storeIDs(self,advertID,competenceID):
        self.advertID = advertID
        self.competenceID = competenceID

    def getadvertID(self):
        return self.advertID

    def getcompetenceID(self):
        return self.competenceID
