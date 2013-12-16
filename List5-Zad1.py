__author__ = 'r.lukaszewski'

import threading
import html.parser
from urllib.request import urlopen
import re

class Probe(object):

    class Thr(threading.Thread):
        """Klasa watkow"""

        class HParser(html.parser.HTMLParser):

            def __init__(self):
                self.vals = []
                html.parser.HTMLParser.__init__(self)

            def handle_starttag(self,tag,attrs):

                for (atr,val) in attrs:
                    if tag=='a' and atr=='href' and val[0:4]=='http': #val[-4:]=='html':
                         self.vals+=[val]

        def __init__(self):
            threading.Thread.__init__(self)

        def start(self,url,fun,gleb):
            self.url = url
            self.fun = fun
            self.gleb= gleb
            threading.Thread.start(self)

        def run(self):

            Probe.visited+=[self.url]

            if self.gleb>0:
                p = self.HParser()

                response = urlopen(self.url)
                p.feed(response.read().decode('utf-8'))

                p.close()
                for v in p.vals: #przeszukujemy podstrony
                    if not v in Probe.visited:
                        thr = Probe.Thr()
                        thr.start(v,self.fun,self.gleb-1)
                        Probe.threads += [thr]

            self.fun(self.url) #uruchamiamy akcje na biezacej stronie

    def frisk(self,url,fun,gleb):
        """metoda glowna uruchamiajaca modul"""
        Probe.visited = []
        Probe.threads = []

        thr = self.Thr()
        thr.start(url,fun,gleb)
        Probe.threads+=[thr]

        for t in Probe.threads:
            t.join()

#wyszukiwanie slowa Python
class Data(html.parser.HTMLParser):

            def __init__(self):
                self.wynik = False
                html.parser.HTMLParser.__init__(self)

            def handle_data(self,data):
                if re.search('Python',data):
                    self.wynik = True

def fpy(url):
    """Funkcja szukajaca"""
    try:
        response = urlopen(url)
    except:
        print("Error while opening", url)

    p = Data()
    p.feed(response.read().decode('utf-8'))
    if p.wynik: print(url,"\n")

#v = Probe()
#v.frisk('http://python.org',fpy,1)
