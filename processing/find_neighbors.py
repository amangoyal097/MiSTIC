#!/usr/bin/env python
import pandas as pd

""" Find neighboring polygons for each polygon """

try:
    from osgeo import gdal
except:
    import gdal
try:
    from osgeo import ogr
except:
    import ogr
try:
    from osgeo import gdalconst
except:
    import gdalconst

import collections
import csv


def shp_neighbors(NeighborFile):
    # vector_ds = ogr.Open(NeighborFile, gdalconst.GA_ReadOnly)
    # vector_layer = vector_ds.GetLayer()

    # feature_count = vector_layer.GetFeatureCount()

    # nbhd = {}

    # for i in range(0, feature_count):

    #     feature1 = vector_layer.GetFeature(i)
    #     district1 = i + 1
    #     geom1 = feature1.GetGeometryRef()
    #     nbhd[district1] = []

    #     for j in range(0, feature_count):
    #         if i == j:
    #             continue

    #         feature2 = vector_layer.GetFeature(j)
    #         district2 = j + 1
    #         geom2 = feature2.GetGeometryRef()

    #         if geom2.Intersects(geom1):
    #             nbhd[district1].append(district2)
    # return nbhd
    with open("../in_new/neighbors.csv") as f:
        ind = 1
        nbhd = {}
        for line in f:
            nbhd[ind] = []
            neighbors = line.split(",")
            for n in neighbors:
                if (n.isnumeric()):
                    nbhd[ind].append(int(n))
            ind += 1
        return nbhd
