#!/usr/bin/python

from urllib2 import urlopen
from HTMLParser import HTMLParser
from collections import defaultdict

tags = defaultdict(int)
domain = "http://ordergroove.com/company"
html = urlopen(domain).read()

class Parser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        tags[tag] += 1

parser = Parser()
parser.feed(html)

i = 0
total = 0
sortedtags = sorted(tags, key=tags.get, reverse=True)

for tag in sortedtags:
  total += tags[tag]

print '[TINY WEB PAGE SCRAPER]'
print
print 'TARGET DOMAIN ==>', domain
print
print 'TOP 5 HTML ELEMENTS MOST USED:'

for tag in sortedtags:
  print tag, '==>', tags[tag]
  i += 1
  if i == 5:
      break

print
print 'HTML TOTAL ==>', total, 'ELEMENTS.'
