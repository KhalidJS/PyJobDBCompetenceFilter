import mysql.connector
import Configuration.AppSettings


class DBManager:
    def __init__(self):
        # My version
        self.option_file = Configuration.AppSettings.AppSettings.Option_File.value
        self.option_groups = Configuration.AppSettings.AppSettings.Option_groups.value
        self.connection = mysql.connector.connect(option_files=self.option_file, option_grups=self.option_groups)
        self.cursor = self.connection.cursor()
        # Alternativ version
        # self.hostname = ''
        # self.user = ''
        # self.password = ''
        # self.database = ''
        # cnx = mysql.connector.connect(user=user,hostname=hostname,password=password,database=database)

    def connect(self):
        # Just for connecting to Mysql server
        cnx = mysql.connector.connect(option_files=self.option_file, option_groups=self.option_groups)
        cur = cnx.cursor()
        print('successfully connected')
