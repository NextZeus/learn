#!/usr/bin/env python
# encoding: utf-8

'read text file -- read and display text file'

fname = raw_input('enter file name:')

print

# attempt to open file for reading
try:
    fobj = open(fname,'r')
except IOError, e:
    print '*** file open error:', e
else:
    #display contents to the screen
    for eachLine in fobj:
        print eachLine,
    fobj.close()
