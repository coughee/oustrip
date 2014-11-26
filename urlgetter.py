import urllib
import codecs
from sys import stdout
from HTMLParser import HTMLParser
from pattern.web import plaintext

class urlParser(HTMLParser):
    def __init__(self, output_list=None):
        HTMLParser.__init__(self)
        if output_list is None:
            self.output_list = []
        else:
            self.output_list = output_list
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            self.output_list.append(dict(attrs).get('href'))

def getData(url):
    data = urllib.urlopen(url)
    return data

def findUrlsInLine(line):
    p = urlParser()
    p.feed(line)
    return p.output_list

def findUrls(url):
    pageData = getData(url)
    urlList = []
    for lines in pageData.readlines():
        lineUrls = findUrlsInLine(lines)
        if(lineUrls is not []):
            for url in lineUrls:
                urlList.append(url)

    return urlList

def getUrls(url,origin):
    urlList = findUrls(url)
    urls = []
    prefix = url
    for lines in urlList:
        if lines is not None and lines.endswith('html'):
            if lines.startswith(origin):
                urls.append(lines)
            elif not lines.startswith('http://'):
                urls.append(origin + lines)
    return urls






    
