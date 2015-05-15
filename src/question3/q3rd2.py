#!/usr/bin/env python

import sys

def parseInput():
    for line in sys.stdin:
        if len(line)>0:
            line = line.strip()
            yield line

def reducer():
    current_key = None
    current_total = 0
    current_count = 0
    for line in parseInput():
        pickup_date, time_interval = line.split('\t')
        try:
            time_interval = float(time_interval)
        except Exception:
            pass
        if current_key == pickup_date:
            # increase total amount and count for specific date
            current_count+=1
            current_total+=time_interval
        else:
            if current_key and current_count and current_total:
                sum = current_total
                avg = current_total/current_count
                print '%s\t%s\t%s' % (current_key, avg, sum)
            # reset
            current_key = pickup_date
            current_count = 0
            current_count += 1
            current_total = 0
            current_total += time_interval
    if current_key == pickup_date:
        if current_key and current_count and current_total:
            sum = current_total
            avg = current_total/current_count
            print '%s\t%s\t%s' % (current_key, avg, sum)

if __name__=='__main__':
    reducer()
