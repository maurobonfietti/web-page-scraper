#!/usr/bin/python

from HTMLParser import HTMLParser
from collections import defaultdict
from time import time
from urllib2 import urlopen
from lxml import html

class Scraper(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.starttime = time()
        self.domain = ""
        self.i = 0
        self.total = 0
        self.tags = defaultdict(int)
        self.htmlstring = ""

    def handle_starttag(self, tag, attrs):
        self.tags[tag] += 1

    def start(self):
        print '\n[Welcome!]'
        print '\n[Tiny Web Page Scraper]'

    def openurl(self):
        self.domain = raw_input("\nEnter a target domain, for example: http://ordergroove.com/company ==> ")
        if not self.domain:
            self.domain = "http://ordergroove.com/company"
        self.starttime = time()
        print "\nTarget Domain:", self.domain
        self.htmlstring = urlopen(self.domain).read()

    def openhtmlfile(self):
        self.starttime = time()
        print "\nLoading HTML From File:"
        file = open('webpage.html', 'r')
        self.htmlstring = file.read()

    def execute(self):
        print '\nHtml Tags Most Used:'
        for tag in sorted(self.tags, key=self.tags.get, reverse=True):
            self.total += self.tags[tag]
            self.i += 1
            if self.i <= 5:
                print ('#%d: %s %s' % (self.i, tag, self.tags[tag]))
        print '\nTotal: %d Html Elements.' % self.total

    def checkseo(self):
        print "\n[CHECKING SEO TAGS]"
        tree = html.fromstring(self.htmlstring)
        title = tree.find(".//title").text
#        print title
#        print len(title)
        if len(title) > 10 and len(title) < 70:
            print "\n[GOOD] The title tag is between 10 and 70 characters long."
        else:
            print "\n[WARNING] The title tag is NOT between 10 and 70 characters long."

    def end(self):
        print "\nScraped in '%.3f' seconds.\n" % (time()-self.starttime)
