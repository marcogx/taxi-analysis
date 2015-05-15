#!/usr/bin/env python

import sys

def parseInput():
    for line in sys.stdin:
        line = line.strip()
        values = line.split(',')
        if len(values)>1 and values[0]!='medallion':
            yield values

def mapper():
    f = open('BigEvent','r')
    line = f.readline().strip().split()
    EventMonth = line[0]
    for value in parseInput():
        total_amount = float(value[10])
        pickup_time = value[3]
        month = pickup_time.split('-')[1]
        day = pickup_time.split('-')[2].split()[0]
        if (EventMonth == month):
            print "%s\t%s" % (day, total_amount)

if __name__=='__main__':
    mapper()