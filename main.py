import re
import Competences

if __name__ == '__main__':
    if Competences.Competences.Title1 is Competences.Competences.Title1:
        print('true')
    file = open('JobTitle.txt')
    JobTitle = file.read()
    for com in Competences.Competences:
        if re.search(com.value, JobTitle, re.M):
            print('Match on: %s' % com.value)
