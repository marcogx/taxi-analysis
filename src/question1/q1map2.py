#!/usr/bin/env python
import sys

def parseInput():
    for line in sys.stdin:
        if len(line)>0:
            line = line.strip()
            yield line

def mapper():
	# output multiple driver's assigned neighbor and income
    for line in parseInput():
        neighbor, income = line.split('\t')
        print '%s\t%s' % (neighbor, income)

if __name__=='__main__':
    mapper()