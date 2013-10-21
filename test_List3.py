from unittest import TestCase
from List3 import doskonale_funkcyjna, doskonale_skladana

__author__ = 'solarplexus'


class TestList3(TestCase):
    def test_doskonale_funkcyjna(self):
        self.assertListEqual([6, 28], doskonale_funkcyjna(100))
        self.assertListEqual([6, 28, 496], doskonale_funkcyjna(1000))
        self.assertListEqual([6, 28, 496, 8128], doskonale_funkcyjna(10000))

    def test_doskonale_skladana(self):
        self.assertListEqual([6, 28], doskonale_skladana(100))
        self.assertListEqual([6, 28, 496], doskonale_skladana(1000))
        self.assertListEqual([6, 28, 496, 8128], doskonale_skladana(10000))