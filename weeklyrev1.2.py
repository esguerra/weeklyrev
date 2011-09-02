#!/usr/bin/python
#####################################################################
## File:        weeklyrev.py
## Authors:     Mauricio Esguerra
## Date:        Monday, August 19, 2011
## Email:       mauricio.esguerra@gmail.com
##
## Description:
##              I got bored of spending a lot of time reviewing
##              the top journals for news related to my research
##              and for news that I find most interesting.
##              So this is an attempt to automate this task.
## Aims:
##            * send e-mail on Sunday nites with queries based
##              on main keywords, most likely looking for the
##              query terms in the titles field.
##
##            * perhaps increase the keywords to authors.
#####################################################################
import time
import feedparser

start = time.time()

#Set-up the list of urls which hold your rss
feeds = ["http://feeds.nature.com/nature/rss/current",
        "http://www.sciencemag.org/rss/current.xml",
        "http://www.pnas.org/rss/current.xml"]

search_fields = [
    ('Title:', 'title'),
    ('Abstract:', 'description'),
    ('URL:', 'link')]

keywords = ['RNA','DNA','Triplex','DNA Triplex',
            'RNA folding', 'life origin']

indent = u' '*4


# label corresponds to the labels in the search_fields{Title, Abstract, URL}
# prop  corresponds to the property from the feed {title,description,link}
for url in feeds:
    items = feedparser.parse(url)
    for item in items:
        for label, prop in search_fields:
            value = item[int(prop)]
    # Note: After value I have added value.encode otherwise
    # redirecting to stdout won't work.
    # http://stackoverflow.com/questions/5141559/unicodeencodeerror-ascii-codec
    # -cant-encode-character-u-xef-in-position-0-o
#    print  indent, label, value      
            print  indent, label, value.encode('ascii','ignore')
            print  indent, u'---'
#    return

end = time.time() 

print 'fetch took %0.3f s' % (end-start)



##
## REFERENCES:
## http://codeboje.de/Feeds-and-python-II/
## http://snippets.aktagon.com/snippets/208-How-to-parse-an-RSS-or-Atom-feed-
## with-Python-and-the-Universal-Feed-Parser-library
## http://www.ibm.com/developerworks/xml/library/x-tipufp/
## https://gitorious.org/redditron/redditron/blobs/master/bbctron.py
## http://www.feedparser.org/
##


#import feedparser
#d = feedparser.parse("http://feeds.nature.com/nature/rss/current")
#d = feedparser.parse(feeds)

#for i in range(len(d['entries'])):
#  print "Summary of Entry:"
#  print d.entries[i].summary 


