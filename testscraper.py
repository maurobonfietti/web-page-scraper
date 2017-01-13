#!/usr/bin/python

from scraperlib import Scraper
import unittest

scraper = Scraper()
#scraper.openurl()
scraper.openhtmlfile()
scraper.feed(scraper.htmlstring)
scraper.getstats()
#scraper.getseostats()
#scraper.end()

class ScraperTests(unittest.TestCase):
    def test_len_html_string(self):
        self.failUnless(len(scraper.htmlstring) > 0)
    def test_len_tags(self):
        self.failUnless(len(scraper.tags) > 0)
    def test_total_tags(self):
        self.assertEqual(scraper.total, 256)

def main():
    unittest.main()

if __name__ == '__main__':
    main()
