#!/usr/bin/env python

import sys

def parseInput():
    for line in sys.stdin:
        line = line.strip()
        values = line.split(',')
        if len(values)>1 and values[0]!='medallion':
            yield values

def mapper():
    for value in parseInput():
        total_amount = float(value[10])
        pickup_time = value[3]
        date = pickup_time.split()[0]
        print "%s\t%s" % (date, total_amount)

if __name__=='__main__':
    mapper()