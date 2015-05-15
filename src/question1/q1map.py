#!/usr/bin/env python
import sys
sys.path.append('.')
import matplotlib
matplotlib.use('Agg')
from matplotlib.path import Path
from rtree import index as rtree
import numpy, shapefile, time

def findNeighborhood(location, index, neighborhoods):
    match = index.intersection((location[0], location[1], location[0], location[1]))
    for a in match:
        if any(map(lambda x: x.contains_point(location), neighborhoods[a][1])):
            return a
    return -1

def readNeighborhood(shapeFilename, index, neighborhoods):
    sf = shapefile.Reader(shapeFilename)
    for sr in sf.shapeRecords():
        if sr.record[1] not in ['New York', 'Kings', 'Queens', 'Bronx']: continue
        paths = map(Path, numpy.split(sr.shape.points, sr.shape.parts[1:]))
        bbox = paths[0].get_extents()
        map(bbox.update_from_path, paths[1:])
        index.insert(len(neighborhoods), list(bbox.get_points()[0])+list(bbox.get_points()[1]))
        neighborhoods.append((sr.record[3], paths))
    neighborhoods.append(('UNKNOWN', None))

def parseInput():
    for line in sys.stdin:
        line = line.strip()
        values = line.split(',')
        if len(values)>1 and values[0]!='medallion': 
            yield values

def mapper():
    index = rtree.Index()
    neighborhoods = []
    readNeighborhood('ZillowNeighborhoods-NY.shp', index, neighborhoods)
    
    # read taxi trip and fare data 
    for values in parseInput():
        pickup_neighborhood=-1        # default as first
        total = -1              # default as first
        drv_lcn  = values[1]
        if len(values) == 14: # trip_data
            pickup_location = (float(values[10]), float(values[11]))
            pickup_neighborhood = findNeighborhood(pickup_location, index, neighborhoods)
            print '%s\t%s\t%s' % (drv_lcn, neighborhoods[pickup_neighborhood][0], total)
        else: # trip_fare
            total = float(values[10])
            print '%s\t%s\t%s' % (drv_lcn, pickup_neighborhood, total)


if __name__=='__main__':
    mapper()