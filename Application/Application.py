from mysql.connector import connect, ProgrammingError
from AppConfiguration.Configuration.AppSettings import AppSettings
from Filter import ContentFilter
from Channel import MessageChannel


class Application:

    def __init__(self):
        # My version
        self.option_file = AppSettings.Option_File.value
        self.option_groups = AppSettings.Option_groups.value
        self.content = ContentFilter.ContentFilter()
        self.messageFilter = ''

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
        print('App Running.........')
        FetchData = MessageChannel.MessageChannel()
        FetchData.fetchAndFilterDataFromDB(self.option_file, self.option_groups)
