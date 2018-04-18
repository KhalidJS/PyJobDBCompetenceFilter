import mysql.connector
from Config import *
import time
import re
import sys


class Filter:
    def __init__(self):
        try:

            cnx = mysql.connector.connect(option_files=Config.Option_File.value, option_groups='CloudDB')
            cur1 = cnx.cursor(buffered=True)
            cur2 = cnx.cursor(buffered=True)
            print('')
            print('Connection established')
            print('')
            antalkompetencer = 0
            antalannoncer = 0
            laa = 0
            with open(Config.SQL_Select_kompetence.value, 'r') as k:
                with open(Config.SQL_Select_Annonce.value, 'r') as a:
                    start_time = time.time()
                    for line_in_k in k:
                        for line_in_a in a:
                            cur1.execute(line_in_k)
                            cur2.execute(line_in_a)
                            for kompetencelabel, t in cur1:
                                antalkompetencer = antalkompetencer + 1
                                # print("%s %s" % (kompetencelabel,t))
                                if re.search('['+kompetencelabel + ']', t, re.IGNORECASE):
                                    print("Match on: %s : %s" % (kompetencelabel, t))
                                else:
                                    pass
                                    #print("no Match")
                                    #laa = laa + 1
                                    #print("%d" % laa)
                    print("Antal kompetencer: %d" % antalkompetencer)
                    print("antal annoncer %d" % antalannoncer)
                    end = time.time()
                    elapsed = end - start_time
                    print("Tid taget" + time.strftime("%H:%M:%S", time.gmtime(elapsed)))
        except mysql.connector.ProgrammingError as e:
            print('Something went wrong', e.args)
