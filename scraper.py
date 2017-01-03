#!/usr/bin/python

from scraperlib import Scraper

scraper = Scraper()
scraper.start()
#scraper.openurl('http://ordergroove.com/company')
#scraper.openurl('http://ordergroove.com/404-1234567890-not-exits')
scraper.openurl('https://www.microsoft.com/es-ar/')
#scraper.openurl('http://example.com')
#scraper.openurl('http://localhost')
#scraper.openurl('')
scraper.feed(scraper.htmlstring)
scraper.getstats()
scraper.end()
