# web-page-scraper

A very tiny web page scraper written in python :-)

For a target domain, sum all the html elements and display the top 5 most used tags, and their respective counts.


## HOW TO USE:

Download the source code and then run from the cli:

```
$ git clone https://github.com/maurobonfietti/web-page-scraper.git
$ cd web-page-scraper/
$ ./scraper.py
```


## RUN TESTS:

Run all tests for the web page scraper:

```
$ ./testscraper.py
```


## CLI OUTPUT EXAMPLE:

View a screen output example of the command line:

```

[Welcome!]

[Tiny Web Page Scraper]

Target Domain: http://ordergroove.com/company

Html Tags Most Used:
#1: div 129
#2: a 38
#3: li 35
#4: script 18
#5: link 10

Total: 276 Html Elements.

Web Page Scraped in '0.860' seconds.

```


## SCRAPER EXTRA:

Another scraper program but in one file script version ;-)

```
$ cd tiny-web-page-scraper/
$ ./web-page-scraper.py
```
