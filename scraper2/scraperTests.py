#!/usr/bin/python

from ScraperLib import Scraper
from lxml import html
import unittest

scraper = Scraper()
scraper.start()
scraper.openurl()
#scraper.openhtmlfile()
scraper.feed(scraper.htmlstring)
scraper.getstats()
#scraper.getseostats()
scraper.end()

tree = html.fromstring(scraper.htmlstring)
title = tree.find(".//title").text
body = tree.xpath('//body/text()')

class ScraperTests(unittest.TestCase):
    def test1(self):
        self.failUnless(len(scraper.htmlstring) > 0)
    def test2(self):
        self.failUnless(len(body) > 0)
    def test3(self):
        self.failUnless(len(title) > 0)
    def test4(self):
        self.failUnless(len(scraper.tags) > 0)
    def test5(self):
        self.failUnless(scraper.total > 0)

def main():
    unittest.main()

if __name__ == '__main__':
    main()
