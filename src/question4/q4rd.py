#!/usr/bin/env python
import itertools, operator, sys

def parseInput():
    for line in sys.stdin:
        yield line.strip('\n').split('\t')

def reducer():
    f = open('BigEvent','r')
    line = f.readline().strip().split()
    EventName = line[3]
    print EventName
    EventDay = line[1].strip().split('-')
    for key, values in itertools.groupby(parseInput(), operator.itemgetter(0)):
        count = sum(map(float, zip(*values)[1]))
        #if (int(key) >=1) and (int(key) <6):
        if key in EventDay:
            print '%s\t%s' % (key, count)
        #print '%s\t%s' %(key,values)

if __name__=='__main__':
    reducer()