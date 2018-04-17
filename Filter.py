import mysql.connector
from Config import *

if __name__ == '__main__':
    try:
        cnx = mysql.connector.connect(option_files=Config.Option_File.value, option_groups='CloudDB')
        cur = cnx.cursor()
        print('')
        print('Connection established')
        print('')
        with open(Config.SQL_Select.value, 'r') as file:
            for line in file:
                cur.execute(line)
                for reg_id,name in cur:
                    print('ID {0}   {1} '.format(reg_id,name))
    except mysql.connector.ProgrammingError as e:
            print('Something went wrong', e.args)