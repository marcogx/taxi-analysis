#!/usr/bin/env python
import sys
from itertools import groupby

def parseInput():
    for line in sys.stdin:
        if len(line)>0:
            line = line.strip()
            yield line

def most_common(list):
    return max(set(list), key=list.count)

def reducer():
    current_key = None
    neighbor_list = []
    current_amount = 0.0

    # for each driver, assign him/her the neighbor with maximal frequency
    for line in parseInput():
        key, neighbor, amount = line.split('\t')
        if key == current_key:
            if amount == '-1': # location line
                neighbor_list.append(neighbor)
            else:
                try:
                    amount = float(amount)
                    current_amount += amount
                except Exception:
                    continue
        else: # key changes
            if current_key and neighbor_list:
                neighbor = most_common(neighbor_list)
                print "%s\t%s" % (neighbor, current_amount)
            current_key = key
            neighbor_list = []
            current_amount = 0.0
            if amount == '-1': # location line
                neighbor_list.append(neighbor)
            else:
                try:
                    amount = float(amount)
                    current_amount += amount
                except Exception:
                    continue
    if key == current_key: #final clean up
        if key == current_key and neighbor_list:
            neighbor = most_common(neighbor_list)
            print "%s\t%s" % (neighbor, current_amount)
if __name__=='__main__':
    reducer()