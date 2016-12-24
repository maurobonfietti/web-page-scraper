#!/usr/bin/python

from urllib2 import urlopen
from HTMLParser import HTMLParser
from collections import defaultdict

o = defaultdict(int)
d = "http://ordergroove.com/company"
h = urlopen(d).read()

class P(HTMLParser):
    def handle_starttag(self, tag, attrs):
        o[tag] += 1

parser = P()
parser.feed(h)

for t in sorted(o, key=o.get, reverse=True):
  print t, o[t]
