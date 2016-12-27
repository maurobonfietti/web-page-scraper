#!/usr/bin/python

from ScraperLib import Scraper

scraper = Scraper()
scraper.start()
scraper.openurl()
#scraper.openhtmlfile()
scraper.feed(scraper.htmlstring)
scraper.execute()
#scraper.checkseo()
scraper.end()
