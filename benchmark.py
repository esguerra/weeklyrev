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

feeds = ['http://feeds.nature.com/nature/rss/current',
        'http://www.sciencemag.org/rss/current.xml',
        'http://www.pnas.org/rss/current.xml']
 
for url in feeds:
  options = {
    'agent'   : '..',
    'etag'    : '..',
    'modified': feedparser._parse_date('Sat, 29 Oct 1994 19:43:31 GMT'),
    'referrer' : '..'
  }

  feed_data = feedparser.parse(url, **options)

  print len(feed_data.entries)
  print feed_data.feed.title.encode('utf-8')

end = time.time()
 
print 'fetch took %0.3f s' % (end-start)



