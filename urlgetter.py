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
    try:
        data = urllib.urlopen(url)
    except UnicodeDecodeError:
        data = []
    return data

def findUrlsInLine(line):
    p = urlParser()
    try:
        p.feed(line)
    except:
        return []
    return p.output_list

def findUrls(url):
    pageData = getData(url)
    
    #Extract urls
    lineUrls = [findUrlsInLine(line) for line in pageData.readlines()]

    #Flatten lists
    urlList = [item for sublist in lineUrls for item in sublist if item is not None]
    
    return urlList

def getUrls(url,origin):
    urlList = findUrls(url)
    urls = [urlChecker(x,origin) for x in urlList if urlChecker(x,origin) is not None] 
    return urls

def urlChecker(url,origin):
    if url.endswith('.pdf'):
        return None
    if url.endswith('.doc') or url.endswith('.docx'):
        return None
    if url.startswith(origin):
        return url
    if url.startswith('http://'):
        return None
    if url.startswith('https://'):
        return None
    if url.startswith('/'):
        return origin + url[1:]
    return origin + url
    
            





    
