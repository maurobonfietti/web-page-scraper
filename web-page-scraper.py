#!/usr/bin/python

print("[WEB-PAGE-SCRAPER]")
print("Coming Soon...")

from urllib2 import urlopen

h = urlopen("http://ordergroove.com/company").read()

print(h)

