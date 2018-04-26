#!/usr/bin/env python
"""
================================================================================
File:        weeklyrev.py
Authors:     Mauricio Esguerra
Start:       Friday, October 7 2011
Update:      Thursday, April 2018
Email:       mauricio.esguerra@gmail.com

Description:
             I got bored of spending a lot of time reviewing
             the top journals for news related to my research
             and for news that I find most interesting.
             So this is an attempt to automate this task.
Aims:
           * send e-mail on Sunday nites with queries based
             on main keywords, most likely looking for the
             query terms in the titles field.

           * perhaps increase the keywords to authors.
================================================================================
"""
import time
import feedparser
import re
import smtplib
import os

from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders


start = time.time()

# Variable Definitions
mail_user = "weeklyrevs@gmail.com"
mail_pwd = "xxx"
feeds = ['http://feeds.nature.com/nature/rss/current',
        'http://www.sciencemag.org/rss/current.xml',
        'http://feeds.nature.com/nsmb/rss/current',
        'http://www.pnas.org/rss/current.xml',
        'http://feeds.aps.org/rss/recent/prl.xml',
        'http://nar.oxfordjournals.org/rss/current.xml',
        'http://rnajournal.cshlp.org/rss/current.xml',
        'http://bioinformatics.oxfordjournals.org/rss/current.xml',
        'https://www.cell.com/cell/current.rss',
        'https://www.journals.elsevier.com/journal-of-molecular-biology/rss'
        ]
search_fields = [
    ('Title:', 'title', None),
    ('Abstract:', 'description', None),
    ('URL:', 'link', None)]
keywords = ['RNA','DNA','Triplex','DNA Triplex',
            'RNA folding', 'life origin']
indent = u' '*4




def mail(to, subject, text, attach):
   msg = MIMEMultipart()

   msg['From'] = mail_user
   msg['To'] = to
   msg['Subject'] = subject

   msg.attach(MIMEText(text))

   part = MIMEBase('application', 'octet-stream')
   part.set_payload(open(attach, 'rb').read())
   Encoders.encode_base64(part)
   part.add_header('Content-Disposition',
           'attachment; filename="%s"' % os.path.basename(attach))
   msg.attach(part)

   mailServer = smtplib.SMTP("smtp.gmail.com", 587)
   #mailServer = smtplib.SMTP("smtp.fastbit.se", 25)
   mailServer.ehlo()
   mailServer.starttls()
   mailServer.ehlo()
   mailServer.login(mail_user, mail_pwd)
   mailServer.sendmail(mail_user, to, msg.as_string())
   # Should be mailServer.quit(), but that crashes...
   mailServer.quit()
   
 

#def review():
file = open('weekinreview.txt','w')


#def review:{}
#def readurl(feeds):
#     """Read URL"""     

 
for url in feeds: 
  feed_data = feedparser.parse(url)
  maxi=len(feed_data.entries)
  print >> file, feed_data.feed.title.encode('utf-8')
  print >> file,  u'==================================================='
  item=0
  items=range(int(maxi))
  for item in items:
      thedata = feed_data.entries
#      One can make it case insensitive adding re.findall("term",item,re.I)      
#      b = re.findall("RNA", thedata[item].description, re.I)
      b = re.findall("RNA", thedata[item].description)      
      if b:
            print >> file, thedata[item].title.upper().encode('utf-8')
            print >> file, u'----------------------------------------'
            print >> file, thedata[item].description.encode('utf-8')
            print >> file, thedata[item].link.encode('utf-8')
            print >> file, u'----------------------------------------'
#            print >> file,  indent, u'---'
#            print b.group()
#            howmany=len(b)
#            print howmany
#            print b
  print >> file, u'                               '

end = time.time()
print >> file, 'fetch took %0.3f s' % (end-start)
 





#review(feeds,fields,keywords)
#mail("mauricio.esguerra@gmail.com",
#   "Automated Weekly Literature Review",
#   " ",
#   "weekinreview.txt")



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
## http://kutuma.blogspot.com/2007/08/
## sending-emails-via-gmail-with-python.html  << Sends email

#
# The idea would be that Pubmed should allow me to do the same search so that I
# wouldn't have to loose time on this. For now this is what you get using 
# pubmed.
#
# Search using:
# RNA[Title/Abstract] AND ("2011/08/07"[PDat] : "2011/09/05"[PDat]) AND 
# (Nature[Journal] OR Science[Journal])
# And then compare results with weeklyrev1.6 and you'll see the difference.
# The difference is that it's not up to date with the latest issues of nature and science.
