#!/usr/bin/python

from scraperlib import Scraper

scraper = Scraper()
scraper.start()
scraper.openurl('https://github.com/')
scraper.feed(scraper.htmlstring)
scraper.getstats()
scraper.end()
