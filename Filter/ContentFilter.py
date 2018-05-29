

class ContentFilter:
    def __init__(self):
        self.SelectQuery = 'select _id, prefferredLabel, altLabels from kompetence'

    def getSpecifiedContent(self):
        query = self.SelectQuery
        return query
