#!/usr/bin/env python

""" Find neighboring polygons for each polygon """
import json


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
    with open("config.json", "r") as f:
        data = json.load(f)
    with open("config.json", "w") as f:
        data['nbhd'] = nbhd
        data['featureCount'] = feature_count
        json.dump(data, f)
    return nbhd
