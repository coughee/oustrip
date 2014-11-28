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
        self.currentUrls = []

    def addUrl(self,url,children):
        self.urls.append(url)
        self.nodes.append(node(url,children))

    def visitUrl(self,url):
        children = ug.getUrls(url,self.origin)

        if not url in self.urls:
            self.addUrl(url,children)
        else:
            return #return if the url has already been visited
            
        uniques = [curl for curl in children if curl not in self.urls and curl not in self.currentUrls]
        self.currentUrls.extend(uniques)

        
    def startCrawl(self):
        self.currentUrls.append(self.origin)
        for urls in self.currentUrls:
            self.visitUrl(urls)


    def printUrls(self,urllist):
        for url in urllist:
            print url
        
url = 'http://physics.open.ac.uk/~jphague/'
f = graph(url)
f.startCrawl()
f.printUrls(f.urls)
        

        
