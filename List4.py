__author__ = 'r.lukaszewski'
import re

def words(stream):
    pMiddle = re.compile(r'[^^]\b(\w+)\b[^\n]')
    pLineBegin = re.compile('^\w+')
    #pLineEnd = re.compile('[^\s]\w+\Z')
    line = stream.readline()
    boundaryMatch = pLineBegin.match(line)
    if boundaryMatch:
        yield boundaryMatch
    for match in pMiddle.finditer(line):
        yield match.group(1)
    #boundaryMatch = pLineEnd.match(line)

    while len(line) != 0:
        line = stream.readline()
        for match in pMiddle.finditer(line):
            yield match.group(1)