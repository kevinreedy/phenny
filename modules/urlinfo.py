#!/usr/bin/env python
import urllib
import random
import urllib2

import re, htmlentitydefs

def unescape(text):
    def fixup(m):
        text = m.group(0)
        if text[:2] == "&#":
            # character reference
            try:
                if text[:3] == "&#x":
                    return unichr(int(text[3:-1], 16))
                else:
                    return unichr(int(text[2:-1]))
            except ValueError:
                pass
        else:
            # named entity
            try:
                text = unichr(htmlentitydefs.name2codepoint[text[1:-1]])
            except KeyError:
                pass
        return text # leave as is
    return re.sub("&#?\w+;", fixup, text)

def tinyurl(url):
   f=urllib2.urlopen(url)
   target=f.geturl()
   return target

def gettitle(url):
   print "gettitle called with:"+url
   f=urllib.urlopen(url)
   data=f.read()
   start=data.find("<title>")+7
   end=data.find("</title>")
   title=data[start:end]
   #if title.count("YouTube"):
   #   title=title[(title.find("-")+2):len(title)]
   space=re.compile(" +")
   title=re.sub(space," ",title)
   title=title.strip()
   
   return title

def title (phenny, input):
   try:
      url = input.group(2)
      if url[0:4]<>"http":
         url="http://"+url
      title=gettitle(url)
      if title.count("ERROR")==0:
         phenny.reply(title) #input.sender+": "+title)
   except:
      print "groupfail"
title.rule = r'^\.title.*'

def titleauto (phenny, input):
   print input
   data = input
   data=  data.split()
   for item in data:
      if 'http' in item:
         url = item
   if not url:
      url=data
   newurl=tinyurl(url)
   title=gettitle(newurl)
   
   text=title
   if len(text)>80:
      text=text[0:80]
      text=text+"..."
   text = unescape(text)
   phenny.reply(text)
titleauto.rule = r'(^http:\/\/)(tinyurl.com/|bit.ly/|open.spotify|ln-s.net|youtube.com|www.youtube.com)([\>:A-Za-z0-9 ,./-?]*)'


if __name__ == '__main__': 
   print __doc__.strip()
