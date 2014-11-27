import urlgetter as ug

class node:
    def __init__(self, url, children):
        self.url = url
        self.p = []
        self.c = children


class graph:
    def __init__(self,url):
        self.nodes = []
        self.urls = []
        self.origin = url

    def addUrl(self,url,children):
        self.urls.append(url)
        self.nodes.append(node(url,children))

    def visitUrl(self,url):
        children = ug.getUrls(url,self.origin)

        if not url in self.urls:
            self.addUrl(url,children)
            
        uniques = [curl for curl in children if curl not in self.urls]
        
        for curl in uniques:
            self.visitUrl(curl)
        print len(self.urls)
        
    def startCrawl(self):
        self.visitUrl(self.origin)

    def printUrls(self,urllist):
        for url in urllist:
            print url
        
url = 'http://www.open.ac.uk/'
f = graph(url)
f.startCrawl()
print f.urls
        

        
