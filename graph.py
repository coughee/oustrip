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
        self.origurl = url

    def addUrl(self,url,children):
        self.urls.append(url)
        self.nodes.append(node(url,children))

    def visitUrl(self,url):
        children = ug.getUrls(url,self.origurl)
        if not url in self.urls:
            self.addUrl(url,children)

        for curl in children:
            if not curl in self.urls:
                self.visitUrl(curl)
url = 'http://physics.open.ac.uk/~jphague/'
f = graph(url)
f.visitUrl(url)
print f.urls
        

        
