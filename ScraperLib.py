#!/usr/bin/python

from HTMLParser import HTMLParser
from collections import defaultdict
from time import time
from urllib2 import urlopen

class Scraper(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.start = time()
        self.domain = ""
        self.i = 0
        self.total = 0
        self.tags = defaultdict(int)
        self.html = ""

    def handle_starttag(self, tag, attrs):
        self.tags[tag] += 1

    def init(self):
        print '\n[Welcome!]'
        print '\n[Tiny Web Page Scraper]'

    def openurl(self):
        self.domain = raw_input("Enter a target domain, for example: http://ordergroove.com/company ==> ")
        if not self.domain:
            self.domain = "http://ordergroove.com/company"
        self.start = time()
        print "\nTarget Domain:", self.domain
        self.html = urlopen(self.domain).read()

    def openhtmlfile(self):
        self.start = time()
        print "\nLoading Target Domain From File:", self.domain
        file = open('webpage.html', 'r')
        self.html = file.read()

    def execute(self):
        print '\nHtml Tags Most Used:'
        for tag in sorted(self.tags, key=self.tags.get, reverse=True):
            self.total += self.tags[tag]
            self.i += 1
            if self.i <= 5:
                print ('#%d: %s %s' % (self.i, tag, self.tags[tag]))
        print '\nTotal: %d Html Elements.' % self.total
        print "\nScraped in '%.3f' seconds.\n" % (time()-self.start)

    def checkseo(self):
        import lxml.html
        tree = lxml.html.fromstring(self.html)
        title = tree.find(".//title").text
        print title
        print len(title)
        if len(title) > 10 and len(title) < 70:
            print "[GOOD] Title entre 10 y 70 chars..."
        else:
            print "[WARNING] Title recomendado entre 10 y 70 chars..."
