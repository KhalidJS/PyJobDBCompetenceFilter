import re
import Competences
import regex
import MessageFilter

if __name__ == '__main__':
    filter = MessageFilter.MessageFilter()
    for com in filter.GetCompetences():
        for ann in filter.GetJobAnnonceBodies():
            m = regex.search('('+com+'){0}', ann, regex.IGNORECASE)
        if m:
            print("Match %s" % m.group())
