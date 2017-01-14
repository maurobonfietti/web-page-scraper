#!/usr/bin/python

from scraperlib import Scraper
import unittest

scraper = Scraper()
scraper.open_html_file()
scraper.feed(scraper.html_string)
scraper.get_stats()

class ScraperTests(unittest.TestCase):
    def test_len_html_string(self):
        self.failUnless(len(scraper.html_string) > 0)
    def test_len_tags(self):
        self.failUnless(len(scraper.tags) > 0)
    def test_total_tags(self):
        self.assertEqual(scraper.total, 256)

def main():
    unittest.main()

if __name__ == '__main__':
    main()
