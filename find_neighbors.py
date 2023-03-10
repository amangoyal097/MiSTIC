#!/usr/bin/env python

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


def shp_neighbors(NeighborFile, prefix_Path):

    # vector = r'/home/anubhav/paper/mistic-tool/sample.shp'

    # open the vector layer
    vector_ds = ogr.Open(NeighborFile, gdalconst.GA_ReadOnly)
    vector_layer = vector_ds.GetLayer()

    feature_count = vector_layer.GetFeatureCount()
    print(feature_count)

    nbhd = {}
    names = []
    ids = {}

    for i in range(0, feature_count):

        feature1 = vector_layer.GetFeature(i)
        district1 = feature1.GetField("DIST")
        geom1 = feature1.GetGeometryRef()
        names.append(district1)
        nbhd[district1] = []

        for j in range(0, feature_count):
            if i == j:
                continue

            feature2 = vector_layer.GetFeature(j)
            district2 = feature2.GetField("DIST")
            geom2 = feature2.GetGeometryRef()

            if geom2.Intersects(geom1):
                nbhd[district1].append(district2)

    od = collections.OrderedDict(sorted(nbhd.items()))
    names.sort()

    index = 1
    for k, v in od.items():

        ids[index] = []
        for val in v:
            ind = names.index(val) + 1
            ids[index].append(ind)
        index += 1

    # Write to File

    filename = prefix_Path + "/neighbors.csv"

    with open(filename, "w") as fp:
        writer = csv.writer(fp, delimiter=",")
        for key in ids:
            writer.writerow(ids[key])

    print("neighbors.csv Created from Shapefile in Input Folder")
