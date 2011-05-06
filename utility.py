#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      hoh
#
# Created:     06/05/2011
# Copyright:   (c) hoh 2011
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import sys
import re
import urllib2
import HTMLParser
from BeautifulSoup import BeautifulSoup
class myHTMLParser(object):
    def __init__(self,url):
        self.__url= url

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self,value):
        self.__url = value

    def parseHTMLHint(self):
        try:
            _re = re.compile(r'<!--')
            _re1 = re.compile(r'-->')
            data = ""
            cout = 0
            page = urllib2.urlopen(self.__url)
            for line in page:
                if re.match(_re,line):
                    cout +=1
                if cout == 2:
                    if not re.match(_re1,line):
                        data += line
            print data
            """soup = BeautifulSoup(page)
            anchorTags = soup.findAll()
            for tags in anchorTags:
                print tags.name"""

        except HTMLParser.HTMLParseError:
            print "Fail to parse page"
        except urllib2.URLError:
            print "Fail to parse the url" + self.__url
def main():
    pass

if __name__ == '__main__':
    main()
    url = 'http://www.pythonchallenge.com/pc/def/ocr.html'
    test =myHTMLParser(url)
    test.parseHTMLHint()
