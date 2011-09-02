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



#urls = ['http://feeds.nature.com/nature/rss/current',
#        'http://www.sciencemag.org/rss/current.xml',
#        'http://www.pnas.org/rss/current.xml']

import sys
import feedparser


search_fields = [
    ('Title:', 'title', None),
    ('Abstract:', 'description', 600),
    ('URL:', 'link', None),
]

indent = u' '*4

def feedinfo(url, output=sys.stdout):
    """
    Read an RSS or Atom feed from the given URL and output a feed
    report with all the key data
    """
    feed_data = feedparser.parse(url)
    channel, items = feed_data.feed, feed_data.entries
    #Display core feed data
    print >> output
    print >> output, "Feed items:"

    for item in items:
        for label, prop, trunc in search_fields:
            value = item[prop]
            if trunc:
                value = value[:trunc] + u'...'
            print >> output, indent, label, value
        print >> output, indent, u'---'
    return


if __name__ == "__main__":
    url = sys.argv[1]
    feedinfo(url)

#if __name__ == "__main__":
#    url = ['http://feeds.nature.com/nature/rss/current',
#        'http://www.sciencemag.org/rss/current.xml',
#        'http://www.pnas.org/rss/current.xml']
#    feedinfo(url)









