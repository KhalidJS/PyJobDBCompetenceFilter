from html.parser import HTMLParser
import urllib.request as urllib2
import regex
from bs4 import BeautifulSoup
from test import *

if __name__ == '__main__':
    file = open('MessageBody.html', 'r', encoding='utf8').read()
    soup = BeautifulSoup(file, 'html.parser')
    symbols = regex.sub('[\(\)\{\}<>/*\*#]', ' ', soup.text)
    removespaces = regex.compile(r'\s+')
    cleanup = regex.sub(removespaces, '\n', symbols)
    print(soup.contents[0])
