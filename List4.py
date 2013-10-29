__author__ = 'r.lukaszewski'
import re

def words(stream):
    pMiddle = re.compile(r'\b\w+\b')
    pLineBegin = re.compile('\A\w+[^\s]')
    pLineEnd = re.compile('[^\s]\w+\Z')
    line = stream.readline()
    print line
    boundaryMatch = pLineBegin.match(line)
    if boundaryMatch:
        yield boundaryMatch
    for match in pMiddle.finditer(line):
        yield match.group()
    boundaryMatch = pLineEnd.match(line)

    while len(line) != 0:
        line = stream.readline()
        print line
        for match in pMiddle.finditer(line):
            yield match.group()