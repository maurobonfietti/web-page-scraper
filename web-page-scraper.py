#!/usr/bin/python

from urllib2 import urlopen
from HTMLParser import HTMLParser
from collections import defaultdict

class Parser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        tags[tag] += 1

i = 0
total = 0
tags = defaultdict(int)
domain = "http://ordergroove.com/company"
html = urlopen(domain).read()

parser = Parser()
parser.feed(html)

sortedtags = sorted(tags, key=tags.get, reverse=True)

for tag in sortedtags:
  total += tags[tag]

print '[TINY WEB PAGE SCRAPER]'
print 'TARGET DOMAIN ==>', domain
print 'TOP 5 HTML ELEMENTS MOST USED:'

for tag in sortedtags:
  print tag, '==>', tags[tag]
  i += 1
  if i == 5:
      break

print 'HTML TOTAL ==>', total, 'ELEMENTS.'
