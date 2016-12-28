#!/usr/bin/python

from ScraperLib import Scraper

scraper = Scraper()
scraper.start()
scraper.openurl()
#scraper.openhtmlfile()
scraper.feed(scraper.htmlstring)
scraper.getstats()
#scraper.getseostats()
scraper.end()
