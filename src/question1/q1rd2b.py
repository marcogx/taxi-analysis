#!/usr/bin/env python

import sys

def parseInput():
    for line in sys.stdin:
        if len(line)>0:
            line = line.strip()
            yield line

def reducer():
    current_key = None
    current_list = []
    for line in parseInput():
        neighbor, income = line.split('\t')
        try:
            income = float(income)
        except Exception:
            pass
        if current_key == neighbor:
            current_list.append(income)
        else:
            if current_key and current_list:
                current_list.sort()
                median = current_list[len(current_list)/2]
                print '%s\t%s' % (current_key, median)
            current_key = neighbor
            current_list = []
            current_list.append(income)

    if current_key == neighbor:
        if current_key and current_list:
            current_list.sort()
            median = current_list[len(current_list)/2]
            print '%s\t%s' % (current_key, median)

if __name__=='__main__':
    reducer()
