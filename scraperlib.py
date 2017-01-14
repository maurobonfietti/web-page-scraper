#!/usr/bin/python

import argparse
from lxml import html
from time import time
from HTMLParser import HTMLParser
from collections import defaultdict
from urllib2 import urlopen, URLError, HTTPError

class Scraper(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.i = 0
        self.total = 0
        self.domain = ""
        self.html_string = ""
        self.start_time = time()
        self.tags = defaultdict(int)
    def handle_starttag(self, tag, attrs):
        self.tags[tag] += 1
    def print_title(self, text):
        print('\n\x1b[1;37;44m' + text + '\x1b[0m')
    def print_result(self, text):
        print('\n\x1b[1;37;42m' + text + '\x1b[0m')
    def print_success(self, text):
        print('\n\x1b[1;32;40m' + text + '\x1b[0m')
    def print_warning(self, text):
        print('\n\x1b[1;33;40m' + text + '\x1b[0m')
    def print_error(self, text):
        print('\n\x1b[1;31;40m' + text + '\x1b[0m')
    def start(self):
        parser = argparse.ArgumentParser(description='A very tiny web page scraper written in Python.')
        parser.add_argument('-v', '--version', action='version', version='%(prog)s version 0.1.2')
        parser.add_argument('-u', '--url', type=str, help='target domain url, for example: https://github.com/')
        args = parser.parse_args()
        self.domain = args.url
        self.print_title('[Welcome!]')
        self.print_title('[Tiny Web Page Scraper]')
    def open_url(self):
        if not self.domain:
            self.domain = "https://github.com/"
        while True:
            self.start_time = time()
            print "\nTarget Domain:", self.domain
            try:
                self.html_string = urlopen(self.domain).read()
                break
            except HTTPError as e:
                self.print_error("[ERROR] The server couldn't fulfill the request.")
                self.print_error('Error Code: %s. Error Reason: %s.' % (e.code, e.reason))
            except URLError as e:
                self.print_error("[ERROR] We failed to reach a server.")
                self.print_error('Error Reason: %s.' % e.reason)
            msg = "\nUPS! Failed to get the html page. Please, retry again with another url address: "
            self.domain = raw_input(msg)
            if not self.domain:
                self.domain = "https://github.com/"
    def open_html_file(self):
        self.start_time = time()
        print "\nLoading HTML From File:"
        file = open('html.file', 'r')
        self.html_string = file.read()
    def get_stats(self):
        self.print_result('Html Tags Most Used:')
        for tag in sorted(self.tags, key=self.tags.get, reverse=True):
            self.total += self.tags[tag]
            self.i += 1
            if self.i <= 5:
                print ('#%d: %s %s' % (self.i, tag, self.tags[tag]))
        self.print_result('Total: %d Html Elements.' % self.total)
    def get_seo_stats(self):
        self.print_title('[Seo Information]')
        self.check_title_tag()
        self.check_h1_tag()
    def check_title_tag(self):
        tree = html.fromstring(self.html_string)
        title = tree.find(".//title").text
        if len(title) > 10 and len(title) < 700:
            msg = '[GOOD] The title tag is between 10 and 70 characters long.'
            self.print_success(msg)
        else:
            msg = '[WARNING] The title tag is NOT between 10 and 70 characters long.'
            self.print_warning(msg)
            print "Tag title:", title
    def check_h1_tag(self):
        tree = html.fromstring(self.html_string)
        tagh1 = tree.xpath('//h1')
        if len(tagh1) == 1:
            self.print_success('[GOOD] Only one <H1> tag per page.')
        else:
            self.print_warning('[WARNING] Use only one <h1> tag per page.')
            print "Total Tags h1:", len(tagh1)
    def end(self):
        print "\nWeb Page Scraped in '%.3f' seconds.\n" % (time()-self.start_time)
