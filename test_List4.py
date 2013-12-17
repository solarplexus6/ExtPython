from __future__ import print_function
from unittest import TestCase
from List4 import words
from itertools import imap
import StringIO

__author__ = 'r.lukaszewski'

class TestList4(TestCase):
    def test_words(self):
        stringStream = StringIO.StringIO('asd    zxc klinia\nplinia srodek fgh')
        self.assertListEqual(['asd', 'zxc', 'srodek', 'fgh'], [x for x in words(stringStream)])
        stringStream.close()