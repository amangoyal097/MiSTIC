from find_neighbors import shp_neighbors
from getLocation import getLocation
try:
    from osgeo import ogr
except:
    import ogr
try:
    from osgeo import gdalconst
except:
    import gdalconst
import operator
from collections import Counter
from write_output import writeOutputs
from utils import reprojectLayer


def sign(a):
    return (a > 0) - (a < 0)


def find_foci(dp):
    """Return list of foci for a time unit"""

    f = []
    index = 0
    for item in dp:
        if item == 0:
            f.append(index + 1)
        index += 1

    return f


def mark_directions(count, nbhd, type):
    """Mark direction towards maximum value neighbor for a time unit"""
    dp = []
    mul = 1 if type == 'max' else -1
    for i in range(1, len(count)):
        nb = nbhd[i]
        diffs = []
        for j in range(0, len(nb)):
            diffs.append(mul * (count[nb[j]] - count[i]))
        index, value = max(enumerate(diffs), key=operator.itemgetter(1))
        if sign(value) == -1 or sign(value) == 0:
            dp.append(0)
        else:
            dp.append(nb[index])

    return dp


def create_zone(dp, focus_Year):
    """Return list containing zoneID for each spatial unit"""

    zone = [0] * len(dp)
    units_in_zone = {}
    for i in range(0, len(focus_Year)):
        numZP = 0
        P = [focus_Year[i]]
        units_in_zone[focus_Year[i]] = []
        zone[focus_Year[i] - 1] = focus_Year[i]
        while P:
            N = []
            for index, value in enumerate(dp):
                if value == P[0]:
                    N.append(index + 1)

            if N:
                for j in range(0, len(N)):
                    zone[N[j] - 1] = focus_Year[i]
                P = P + N
                numZP = numZP + len(N)
                units_in_zone[focus_Year[i]].extend(N)

            P = P[1:]

    return zone, units_in_zone


def find_valid_foci(zone_Year):
    """Return the list of valid foci for each time unit"""

    vf = []
    frequency = Counter(zone_Year).items()
    for item in frequency:
        if item[1] > 1:
            vf.append(item[0])
    return vf


def process_year(year, vectorLayer, location, neighbors, type):
    featureCount = vectorLayer.GetFeatureCount()
    values = [-1]
    for i in range(featureCount):
        feature = vectorLayer.GetFeature(i)
        values.append(float(feature.GetField(str(year))))
    directions = mark_directions(values, neighbors, type)
    foci = find_foci(directions)
    zone, zoneUnits = create_zone(directions, foci)
    validFoci = find_valid_foci(zone)
    lat = []
    long = []
    for f in foci:
        lat.append(location[f][1])
        long.append(location[f][0])
    return foci, zone, lat, long


def mistic(filePath, outputPath, outputProj, startYear, endYear, type):

    reprojectLayer(filePath, outputProj)

    vectorDs = ogr.Open(filePath, gdalconst.GA_ReadOnly)
    vectorLayer = vectorDs.GetLayer()

    location = getLocation(filePath)
    neighbors = shp_neighbors(vectorLayer)

    for year in range(startYear, endYear + 1):
        foci, zone, lat, long = process_year(
            year, vectorLayer, location, neighbors, type)
        writeOutputs(filePath, outputPath, foci, zone, lat, long, year)
        break


# mistic("../shapefile/district.shp", 2001, 2010)
