import mysql.connector
from Config import *
import time
import regex
import sys


class MessageFilter:
    def __init__(self):
        self.competences = []
        self.annoncebodies = []
    def GetCompetences(self):
        try:
            cnx = mysql.connector.connect(option_files=Config.Option_File.value, option_groups='CloudDB')
            cur = cnx.cursor()
            antalkompetencer = 0
            antalannoncer = 0
            with open(Config.SQL_Select_kompetence.value, 'r') as k:
                start_time = time.time()
                for line_in_k in k:
                    cur.execute(line_in_k)
                    for kompetence in cur:
                        antalkompetencer = antalkompetencer + 1
                        # print("%s %s" % (kompetencelabel,t))
                        # match_obj = regex.search(r'('+kompetencelabel+'){1}', t, regex.IGNORECASE | regex.M)
                        # print(kompetencelabel[0])
                        # bodies = bodies = regex.sub('\s+',' ',t[0],flags=regex.UNICODE)
                        # bodies = regex.sub('\s+',' ',t[0],flags=regex.UNICODE)
                        self.competences.append(kompetence[0])
                        # kompetence = ''.join(kompetencelabel)
                        # print(kompetence)
                        # m = regex.search('('+kompetence+'){1}',bodies, regex.IGNORECASE)
                        # if m:
                        # pass
                        # print(m.group(0))

                print("Antal kompetencer: %d" % antalkompetencer)
                print("antal annoncer %d" % antalannoncer)
                end = time.time()
                elapsed = end - start_time
                print("Tid taget" + time.strftime("%H:%M:%S", time.gmtime(elapsed)))
        except mysql.connector.ProgrammingError as e:
            print('Something went wrong', e.args)
        return self.competences
    def GetJobAnnonceBodies(self):
        try:
            cnx = mysql.connector.connect(option_files=Config.Option_File.value, option_groups='CloudDB')
            cur = cnx.cursor()
            with open(Config.SQL_Select_Annonce.value, 'r') as a:
                for line_in_a in a:
                    cur.execute(line_in_a)
                    for annonce in cur:

                        body = regex.sub('\s+', ' ', annonce[0], flags=regex.UNICODE)
                        self.annoncebodies.append(body)
                        #print(body)
        except mysql.connector.ProgrammingError as e:
            print('Something went wrong', e.args)
        return self.annoncebodies

    def filter(self):
        try:
            cnx = mysql.connector.connect(option_files=Config.Option_File.value, option_groups='CloudDB')
            cur = cnx.cursor()
            with open(Config.SQL_Select_Annonce_Kompetence.value, 'r') as k:
                 for line_in_k in k:
                     cur.execute(line_in_k)
                     startTimer = time.time()
                     for kom_id,ann_id,preflabel,ann_body in cur:
                         #body = regex.sub('\s+', ' ', ann_body[0], flags=regex.UNICODE)
                         pattern = regex.compile(r'\s+')
                         body = regex.sub(pattern,' ',ann_body)
                         #print(preflabel)
                         #print(body)
                         #print('-')
                        # match = regex.search('('+preflabel+'){1}',body,regex.IGNORECASE)
                         #if match:
                             #print("Match on %s" % preflabel)
                 elapsed = time.time() - startTimer
                 duration = time.strftime('%H:%M:%S',time.gmtime(elapsed))
                 print(duration)
                # Tager 15 minutter at gennemløbe 100000
        except mysql.connector.ProgrammingError as e:
            print('Something went wrong', e.args)
