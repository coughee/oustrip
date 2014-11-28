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
    urlList = [x for x in urlList if x is not None]
    for lines in urlList:
        u = urlChecker(lines,origin)
        if u is not None:
            urls.append(u)
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
    
            





    
