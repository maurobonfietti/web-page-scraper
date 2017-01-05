# web-page-scraper

A very tiny web page scraper written in Python :-)

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

Target Domain: https://github.com/

Html Tags Most Used:
#1: meta 52
#2: div 49
#3: a 34
#4: link 20
#5: li 12

Total: 256 Html Elements.

Web Page Scraped in '0.915' seconds.
```


## SCRAPER EXTRA:

Another scraper program but in one file script version.

```
$ cd tiny-web-page-scraper/
$ ./tiny-web-page-scraper.py
```
