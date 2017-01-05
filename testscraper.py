#!/usr/bin/python

from scraperlib import Scraper
import unittest

scraper = Scraper()
#scraper.openurl('https://google.com.ar/')
#scraper.openurl('http://google.com/404-1234567890-not-exits')
#scraper.openurl('https://www.microsoft.com/es-ar/')
#scraper.openurl('http://example.com')
#scraper.openurl('http://localhost')
#scraper.openurl('')
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
