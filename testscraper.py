#!/usr/bin/python

from scraperlib import Scraper
from lxml import html
import unittest

scraper = Scraper()
scraper.openurl('http://ordergroove.com/company')
#scraper.openurl('http://ordergroove.com/404-1234567890-not-exits')
#scraper.openurl('https://www.microsoft.com/es-ar/')
#scraper.openurl('http://example.com')
#scraper.openurl('http://localhost')
#scraper.openurl('')
#scraper.openhtmlfile()
scraper.feed(scraper.htmlstring)
scraper.getstats()
#scraper.getseostats()
scraper.end()

tree = html.fromstring(scraper.htmlstring)
taghtml = tree.xpath('//html')
tagbody = tree.xpath('//body')
tagtitle = tree.find(".//title").text

class ScraperTests(unittest.TestCase):
    def test1(self):
        self.failUnless(len(scraper.htmlstring) > 0)
    def test2(self):
        self.failUnless(len(taghtml) > 0)
    def test3(self):
        self.failUnless(len(tagbody) > 0)
    def test4(self):
        self.failUnless(len(tagtitle) > 0)
    def test5(self):
        self.failUnless(len(scraper.tags) > 0)
    def test6(self):
        self.failUnless(scraper.total > 0)

def main():
    unittest.main()

if __name__ == '__main__':
    main()
