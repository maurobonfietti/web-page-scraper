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

print '[Tiny Web Page Scraper]'

domain = raw_input("Enter a target domain, for example: http://ordergroove.com/company ==> ")

html = urlopen(domain).read()
parser = Parser()
parser.feed(html)

print
print "Target Domain:", domain
print
print 'Html Tags Most Used:'

for tag in sorted(tags, key=tags.get, reverse=True):
    total += tags[tag]
    i += 1
    if i <= 5:
        print ('#%d: %s %s' % (i, tag, tags[tag]))

print
print 'Total: %d Html Elements.' % total
print
