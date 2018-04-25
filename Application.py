from regex import sub,compile
from mysql.connector import connect,ProgrammingError
from Configuration.AppSettings import AppSettings
from Filter import ContentFilter

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
        # connecting to Mysql server
        try:
            connection = connect(option_files=self.option_file, option_groups=self.option_groups)
            cursor = connection.cursor()
            print('successfully connected')
            # with open(self.content.getSpecifiedContent(), 'r') as k:
            # for line in k:
            cursor.execute(self.content.getSpecifiedContent())
            for kom_id, ann_id, preflabel, ann_body in cursor:
                #
                # Use beautifulSoup to get the content of the annonce body
                #
                # MessageFilter Zone
                pattern = compile(r'\s+')
                body = sub(pattern, ' ', str(ann_body))
                # MessageFilter Zone
                print(body)
        except ProgrammingError as e:
            print(e.args)
        finally:
            cursor.close()
            connection.close()
