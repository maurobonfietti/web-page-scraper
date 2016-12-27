#!/usr/bin/python

from HTMLParser import HTMLParser
from collections import defaultdict
from time import time
from urllib2 import urlopen

class Parser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.start = time()
        self.domain = ""
        self.i = 0
        self.total = 0
        self.tags = defaultdict(int)
    def handle_starttag(self, tag, attrs):
        self.tags[tag] += 1
    def run(self):
        print '\n[Tiny Web Page Scraper]\n'
        self.domain = raw_input("Enter a target domain, for example: http://ordergroove.com/company ==> ")
        if not self.domain:
            self.domain = "http://ordergroove.com/company"
        self.start = time()
        print "\nTarget Domain:", self.domain
        html = urlopen(self.domain).read()
        parser.feed(html)
        print '\nHtml Tags Most Used:'
        for tag in sorted(self.tags, key=self.tags.get, reverse=True):
            self.total += self.tags[tag]
            self.i += 1
            if self.i <= 5:
                print ('#%d: %s %s' % (self.i, tag, self.tags[tag]))
        print '\nTotal: %d Html Elements.' % self.total
        print "\nScraped in '%.3f' seconds.\n" % (time()-self.start)

parser = Parser()
parser.run()
