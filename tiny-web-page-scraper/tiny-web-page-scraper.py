#!/usr/bin/python

from HTMLParser import HTMLParser
from collections import defaultdict
from urllib2 import urlopen

class Parser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        tags[tag] += 1

i = 0
total = 0
tags = defaultdict(int)
domain = "https://github.com/"

html = urlopen(domain).read()
parser = Parser()
parser.feed(html)

print "Target Domain: '%s'.\n" % domain
print 'Html Tags Most Used:'

for tag in sorted(tags, key=tags.get, reverse=True):
    total += tags[tag]
    i += 1
    if i <= 5:
        print ('#%d: %s %s' % (i, tag, tags[tag]))

print '\nTotal:', total, 'Html Elements.\n'
