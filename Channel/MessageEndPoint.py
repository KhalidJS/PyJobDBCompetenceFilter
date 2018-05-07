
class MessageEndPoint:

    def __init__(self):
        self.advertID = []
        self.competenceID = ''

    def getadvertID(self):
        return self.advertID

    def getcompetenceID(self):
        return self.competenceID

    def addAdvertID(self, _id):
        self.advertID.append(_id)

    def setCompetenceID(self, _id):
        self.competenceID = _id
