from regex import sub, compile
from mysql.connector import connect, ProgrammingError
from Configuration.AppSettings import AppSettings
from Filter import ContentFilter
from time import time
from Channel import MessageChannel


class Application:

    def __init__(self):
        # My version
        self.option_file = AppSettings.Option_File.value
        self.option_groups = AppSettings.Option_groups.value
        self.content = ContentFilter.ContentFilter()
        self.messageFilter = ''
        # Alternativ version
        # self.hostname = ''
        # self.user = ''
        # self.password = ''
        # self.database = ''
        # cnx = mysql.connector.connect(user=user,hostname=hostname,password=password,database=database)

    def TestConnection(self):
        try:
            connection = connect(option_files=self.option_file, option_groups=self.option_groups)
            cursor = connection.cursor()
            print('successfully connected')
        except ProgrammingError as e:
            print('An error has occurred')
        finally:
            cursor.close()
            connection.close()

    def run(self):
        DBCall = MessageChannel.MessageChannel()
        DBCall.fetchAndFilterDataFromDB(self.option_file, self.option_groups)
