import re
import Competences
import regex
import MessageFilter

if __name__ == '__main__':
    filter = MessageFilter.MessageFilter()
    for k in filter.GetJobAnnonceBodies():
        m = regex.search('(C#){1}',k,regex.IGNORECASE)
        if m:
           print("-------------------------")
           print("Match %s" % k)

