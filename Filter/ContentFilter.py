import SqlQueries.SqlScripts

class ContentFilter:
    def __init__(self):
        self.readSelectQueryFile = SqlQueries.SqlScripts.Sql.SQL_Select_annonce_kompetence.value
        self.readInsertQueryFile = SqlQueries.SqlScripts.Sql.SQL_Insert_annoncekompetence.value

    def getSpecifiedContent(self):
        SelectQuery = open(self.readSelectQueryFile).read()
        return SelectQuery

    def getspecifiedContentFromDBToInsert(self):
        InsertQuery = open(self.readInsertQueryFile).read()
        return InsertQuery
