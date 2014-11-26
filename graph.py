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

        for curl in children:
            if not curl in self.urls:
                self.visitUrl(curl)

    def startCrawl(self):
        self.visitUrl(self.origin)
        
url = 'http://physics.open.ac.uk/~jphague/'
f = graph(url)
f.startCrawl()
print f.urls
        

        
