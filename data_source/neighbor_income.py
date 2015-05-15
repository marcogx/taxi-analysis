#!/usr/bin/env python
__author__ = 'spzhang'

zip_dict = {}
file1 = open('zip_2_neighbor.txt','r')
for line in file1:
    neighbor, zips = line.split('\t')
    for zip in zips.split(','):
        zip = zip.strip()
        zip_dict[zip] = neighbor

neighbor_income = dict()
file2 = open('zip_median.txt','r')
for line in file2:
    region, zip, income = line.split('\t')
    try:
        income = float(income)
    except Exception:
        pass
    zip=zip.strip()
    neighbor = zip_dict.get(zip)
    if neighbor:
        if neighbor in neighbor_income:
            neighbor_income[neighbor].append(income)
        else:
            neighbor_income[neighbor] = []
            neighbor_income[neighbor].append(income)

output = open('neighbor_median.txt', 'w')
for key in neighbor_income.keys():
    values = neighbor_income[key]
    median = values[len(values)/2]
    output.write('%s\t%f\n' % (key, median))
output.close()