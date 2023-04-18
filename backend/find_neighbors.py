#!/usr/bin/env python

""" Find neighboring polygons for each polygon """
import json


def shp_neighbors(gdf):
    nbhd = {}
    for index, poly in gdf.iterrows():
        neighbors = [
            ind + 1 for ind in gdf[~gdf.geometry.disjoint(poly.geometry)].index.tolist()]
        if index + 1 in neighbors:
            neighbors.remove(index + 1)
        nbhd[index + 1] = neighbors
    with open("config.json", "r") as f:
        data = json.load(f)
    with open("config.json", "w") as f:
        data['nbhd'] = nbhd
        data['featureCount'] = len(gdf)
        json.dump(data, f)
    return nbhd
