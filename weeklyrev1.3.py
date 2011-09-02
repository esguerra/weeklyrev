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
import re
 
start = time.time()

feeds = ['http://feeds.nature.com/nature/rss/current',
        'http://www.sciencemag.org/rss/current.xml',
        'http://www.pnas.org/rss/current.xml']

for url in feeds: 
  feed_data = feedparser.parse(url)
  maxi=len(feed_data.entries)
  print feed_data.feed.title.encode('utf-8')
  item=0
  items=range(int(maxi))
  for item in items:
      thedata = feed_data.entries
      print thedata[item].title.encode('utf-8')
      print thedata[item].description.encode('utf-8')
      print thedata[item].link.encode('utf-8')
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
## http://www.feedparser.org/docs/index.html  << All the meat is there!
## http://www.wellho.net/resources/ex.php4?item=y104/lister << Remember lists
