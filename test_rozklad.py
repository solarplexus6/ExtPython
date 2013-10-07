from unittest import TestCase
from math import pow
from List1 import rozklad, erat, primePower

__author__ = 'r.lukaszewski'

class TestRozklad(TestCase):
    def test_primePower(self):
        self.assertEqual(2, primePower(5, 75))
        self.assertEqual(2, primePower(2, 100))
    def test_rozklad(self):
        testN = 1000
        sieve = erat(testN)
        for x in range(2, testN):
            result = rozklad(x)
            if x in sieve:
                self.assertListEqual([], result)
            else:
                self.assertEqual(x, reduce(lambda x, y: x * pow(y[0], y[1]), result, 1))

    def test_erat(self):
        self.assertListEqual([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101], erat(102))