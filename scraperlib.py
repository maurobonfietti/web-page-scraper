#!/usr/bin/python

from HTMLParser import HTMLParser
from collections import defaultdict
from lxml import html
from time import time
from urllib2 import urlopen

class Scraper(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.i = 0
        self.total = 0
        self.domain = ""
        self.htmlstring = ""
        self.starttime = time()
        self.tags = defaultdict(int)
    def handle_starttag(self, tag, attrs):
        self.tags[tag] += 1
    def printtitle(self, text):
        print('\n\x1b[1;37;44m' + text + '\x1b[0m')
    def printresult(self, text):
        print('\n\x1b[1;37;42m' + text + '\x1b[0m')
    def printsuccess(self, text):
        print('\n\x1b[1;32;40m' + text + '\x1b[0m')
    def printwarning(self, text):
        print('\n\x1b[1;33;40m' + text + '\x1b[0m')
    def printerror(self, text):
        print('\n\x1b[1;31;40m' + text + '\x1b[0m')
    def start(self):
        self.printtitle('[Welcome!]')
        self.printtitle('[Tiny Web Page Scraper]')
    def openurl(self, url):
        if url:
            self.domain = url
        else:
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
    def getstats(self):
        self.printresult('Html Tags Most Used:')
        for tag in sorted(self.tags, key=self.tags.get, reverse=True):
            self.total += self.tags[tag]
            self.i += 1
            if self.i <= 5:
                print ('#%d: %s %s' % (self.i, tag, self.tags[tag]))
        self.printresult('Total: %d Html Elements.' % self.total)
    def getseostats(self):
        self.printtitle('[Seo Information]')
        self.checktitletag()
        self.checkh1tag()
    def checktitletag(self):
        tree = html.fromstring(self.htmlstring)
        title = tree.find(".//title").text
        if len(title) > 10 and len(title) < 700:
            self.printsuccess('[GOOD] The title tag is between 10 and 70 characters long.')
        else:
            self.printwarning('[WARNING] The title tag is NOT between 10 and 70 characters long.')
            print "Tag title:", title
    def checkh1tag(self):
        tree = html.fromstring(self.htmlstring)
        tagh1 = tree.xpath('//h1')
        if len(tagh1) == 1:
            self.printsuccess('[GOOD] Only one <H1> tag per page.')
        else:
            self.printwarning('[WARNING] Use only one <h1> tag per page.')
            print "Total Tags h1:", len(tagh1)
    def end(self):
        print "\nWeb Page Scraped in '%.3f' seconds.\n" % (time()-self.starttime)
