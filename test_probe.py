from unittest import TestCase
from List5_Zad1 import Probe

__author__ = 'r.lukaszewski'

src_url = "http://solarplexus6.github.io/ExtPython/"

def perform_test (src_url, level):
    urls = []
    fun = lambda url: urls.append(url)
    v = Probe()
    v.frisk(src_url, fun, level)
    return urls

class TestProbe(TestCase):
    def test_frisk_basic(self):
        result = perform_test(src_url, 1)

        self.assertCountEqual(["http://solarplexus6.github.io/ExtPython/",
                              "http://solarplexus6.github.io/ExtPython/pages/probeTest1.html",
                              "http://solarplexus6.github.io/ExtPython/pages/probeTest2.html",
                              "http://solarplexus6.github.io/ExtPython/pages/probeTest3.html"]
                             , result)

    def test_frisk_levels(self):
        result = perform_test(src_url, 2)

        self.assertCountEqual(["http://solarplexus6.github.io/ExtPython/",
                              "http://solarplexus6.github.io/ExtPython/pages/probeTest1.html",
                              "http://solarplexus6.github.io/ExtPython/pages/probeTest2.html",
                              "http://solarplexus6.github.io/ExtPython/pages/probeTest3.html",
                              "http://solarplexus6.github.io/ExtPython/pages/levelTwoProbeTest.html"]
                             , result)

    def test_frisk_circular(self):
        result = perform_test(src_url, 4)

        self.assertCountEqual(["http://solarplexus6.github.io/ExtPython/",
                              "http://solarplexus6.github.io/ExtPython/pages/probeTest1.html",
                              "http://solarplexus6.github.io/ExtPython/pages/probeTest2.html",
                              "http://solarplexus6.github.io/ExtPython/pages/probeTest3.html",
                              "http://solarplexus6.github.io/ExtPython/pages/levelTwoProbeTest.html"]
                             , result)