__author__ = 'r.lukaszewski'

import threading
import html.parser
from urllib.request import urlopen, HTTPError
from urllib.parse import urljoin
import re

class Probe(object):

    class Thr(threading.Thread):
        """Klasa watkow"""

        class HParser(html.parser.HTMLParser):

            def __init__(self, url):
                self.vals = []
                self.url = url
                html.parser.HTMLParser.__init__(self)

            def handle_starttag(self,tag,attrs):

                for (atr,val) in attrs:
                    if tag=='a' and atr=='href':
                        if val[0:4]=='http':
                            self.vals+=[val]
                        else:
                            # dla relative url laczymy obecny path z nowym adresem
                            self.vals+=[urljoin(self.url, val)]

        def __init__(self, url,fun,gleb, parent):
            self.children = []
            self.url = url
            self.fun = fun
            self.gleb= gleb
            self.parent = parent
            threading.Thread.__init__(self)

        def start(self):
            threading.Thread.start(self)

        def run(self):

            self.parent.visited+=[self.url]

            if self.gleb>0:
                parser = self.HParser(self.url)

                contents = ""
                try:
                    response = urlopen(self.url)
                    contents = response.read().decode('utf-8')
                except HTTPError:
                    pass
                parser.feed(contents)

                parser.close()
                for v in parser.vals: #przeszukujemy podstrony
                    if not v in self.parent.visited:
                        thr = Probe.Thr(v,self.fun,self.gleb-1, self.parent)
                        thr.start()
                        self.parent.threads += [thr]
                        self.children += [thr]

            self.fun(self.url) #uruchamiamy akcje na biezacej stronie

            #czekamy na watki potomne
            for t in self.children:
                t.join()

    def __init__(self):
        self.visited = []
        self.threads = []

    def frisk(self,url,fun,gleb):
        """metoda glowna uruchamiajaca modul"""
        self.visited = []
        self.threads = []

        thr = self.Thr(url,fun,gleb, self)
        thr.start()
        self.threads+=[thr]

        for t in self.threads:
            t.join()

#wyszukiwanie slowa Python
class Data(html.parser.HTMLParser):

            def __init__(self):
                self.wynik = False
                html.parser.HTMLParser.__init__(self)

            def handle_data(self,data):
                if re.search('Python',data):
                    self.wynik = True

def searchPythonKeyword(url):
    """Funkcja szukajaca"""
    try:
        response = urlopen(url)
    except:
        print("Error while opening", url)

    p = Data()
    p.feed(response.read().decode('utf-8'))
    if p.wynik: print(url,"\n")

#v = Probe()
#v.frisk('http://python.org',searchPythonKeyword,1)
