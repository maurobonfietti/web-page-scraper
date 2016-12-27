#!/usr/bin/python

from ScraperLib import Scraper

scraper = Scraper()
scraper.init()
scraper.openurl()
scraper.feed(scraper.html)
scraper.execute()
