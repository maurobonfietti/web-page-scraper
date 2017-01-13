#!/usr/bin/python

from scraperlib import Scraper

scraper = Scraper()
scraper.start()
scraper.openurl()
scraper.feed(scraper.htmlstring)
scraper.getstats()
scraper.end()
