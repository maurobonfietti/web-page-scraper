#!/usr/bin/python

from scraperlib import Scraper

scraper = Scraper()
scraper.start()
scraper.open_url()
scraper.feed(scraper.html_string)
scraper.get_stats()
scraper.get_seo_stats()
scraper.end()
