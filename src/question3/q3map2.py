#!/usr/bin/env python
__author__ = 'spzhang'

import sys, datetime

def parseInput():
    for line in sys.stdin:
        if len(line)>0:
            line = line.strip()
            yield line

def mapper():
    # just sort the input by mapper
    for line in parseInput():
        pickup_date, time_interval = line.split('\t')
        print '%s\t%s' % (pickup_date, time_interval)

if __name__=='__main__':
    mapper()