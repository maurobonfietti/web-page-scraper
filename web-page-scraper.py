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

i = 0
total = 0
s = sorted(o, key=o.get, reverse=True)

for t in s:
  total += o[t]

print 'TOTAL HTML ELEMENTS:', total

print 'TOP 5 HTML ELEMENTS:'

for t in s:
  print t, o[t]
  i += 1
  if i == 5:
      break
