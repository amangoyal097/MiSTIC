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


def shp_neighbors(vector_layer):
    feature_count = vector_layer.GetFeatureCount()
    nbhd = {}

    for i in range(0, feature_count):

        feature1 = vector_layer.GetFeature(i)
        district1 = i + 1
        geom1 = feature1.GetGeometryRef()
        nbhd[district1] = []

        for j in range(0, feature_count):
            if i == j:
                continue

            feature2 = vector_layer.GetFeature(j)
            district2 = j + 1
            geom2 = feature2.GetGeometryRef()

            if geom2.Intersects(geom1):
                nbhd[district1].append(district2)
    return nbhd
