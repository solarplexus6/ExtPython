"""Lista 2"""

__author__ = 'r.lukaszewski'

listItemFormat = "<li>{0}: {1}</li>";
htmlFormat = "<html>" \
             "<head>" \
             "  <title>Stan instancji klasy {0}</title>" \
             "</head>" \
             "<body>" \
             "  <h1>Stan instancji klasy {0}</h1>" \
             "  <ul>{1}</ul>" \
             "</body>" \
             "</html>"
# zad 1
class HtmlObject (object):
    def html(self):
        listStr = ""
        for name, val in self.__dict__.iteritems():
            listStr += listItemFormat.format(name, val)
        return htmlFormat.format(obj.__class__.__name__, listStr)

class ExHtmlObject (HtmlObject):
    def __init__(self):
        self.__privProperty1 = "privPropertyValue1"
        self.__privProperty2 = "privPropertyValue2"
        self.property = 1
    def getPrivProperty(self):
        return self.__privProperty1

obj = ExHtmlObject()
print obj.html()