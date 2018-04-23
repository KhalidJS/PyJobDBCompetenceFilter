from html.parser import HTMLParser
import urllib.request as urllib2
import regex
from bs4 import BeautifulSoup

if __name__ == '__main__':
    file = open('MessageBody.html','r',encoding='utf8').read()
    soup = BeautifulSoup(file,'html.parser')
    pattern = regex.compile(r'\s+')
    body = regex.sub(pattern, ' ', soup.contents[0])
    for script in soup(['script','style']):
        script.extract()

    # get text
    text = soup.get_text()

    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)
    symbols = regex.sub('[\(\)\{\}<>/*\*#]',' ',text)
    for l in soup.find_all('p'):
        print(l)

