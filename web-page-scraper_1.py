#!/usr/bin/python

from HTMLParser import HTMLParser
from collections import defaultdict
from time import time
from urllib2 import urlopen

class Parser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        tags[tag] += 1

i = 0
total = 0
tags = defaultdict(int)

print '\n[Tiny Web Page Scraper]\n'

domain = raw_input("Enter a target domain, for example: http://ordergroove.com/company ==> ")
if not domain:
    domain = "http://ordergroove.com/company"

start = time()

print "\nTarget Domain:", domain

html = urlopen(domain).read()
parser = Parser()
parser.feed(html)

print '\nHtml Tags Most Used:'

for tag in sorted(tags, key=tags.get, reverse=True):
    total += tags[tag]
    i += 1
    if i <= 5:
        print ('#%d: %s %s' % (i, tag, tags[tag]))

print '\nTotal: %d Html Elements.' % total
print "\nScraped in '%.3f' seconds.\n" % (time()-start)
