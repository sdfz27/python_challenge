#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      hoh
#
# Created:     05/05/2011
# Copyright:   (c) hoh 2011
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
import urllib2
from collections import defaultdict


word_dict = defaultdict(int)
def permutation(str):

    if len(str) ==1:
        return [[str[0]]]

    result =[]
    for c in str:
        strnext = list(str)
        strnext.remove(c)
        p = permutation(strnext)
        for mylist in p:
            mylist.append(c)
            result.append(mylist)

    return result

def analyze():
    with open('c:/data.txt') as f:
        for line in f:
            for c in line:
                word_dict[c] +=1
    print word_dict


def main():
    urlhandle = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/ocr.html')
    for line in urlhandle:
        print line
    pass

if __name__ == '__main__':
   main()
   #analyze()
   #a=['a','e','i','l','q','u','t','y']
   #print len(permutation(a))
