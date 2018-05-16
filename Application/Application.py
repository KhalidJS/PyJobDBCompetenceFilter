from mysql.connector import connect, ProgrammingError
from AppConfiguration.Configuration.AppSettings import AppSettings
from Channel import MessageChannel


class Application:

    def __init__(self):
        # init variables
        self.user = AppSettings.user.value
        self.password = AppSettings.password.value
        self.host = AppSettings.host.value
        self.database = AppSettings.database.value
        self.port = AppSettings.port.value

    # Just for test purpose
    def testConnectionToDB(self):
        try:
            connection = connect(user=self.user, password=self.password, database=self.database, host=self.host, port=self.port)
            cursor = connection.cursor()
            print('successfully connected')
        except ProgrammingError as e:
            print('An error has occurred', e.args)
        finally:
            cursor.close()
            connection.close()

    def run(self):
        print('App Running.........')
        FetchData = MessageChannel.MessageChannel()
        FetchData.fetchAndFilterDataFromDB(user=self.user, password=self.password, host=self.host, database=self.database, port=self.port)
