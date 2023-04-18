from find_neighbors import shp_neighbors
from getLocation import getLocation
import operator
from collections import Counter
from write_output import writeOutputs
from utils import reprojectLayer
import json


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


def process_year(year, layer, location, neighbors, type):
    values = [-1]
    for index, poly in layer.iterrows():
        values.append(int(poly[str(year)]))
    directions = mark_directions(values, neighbors, type)
    foci = find_foci(directions)
    zone, zoneUnits = create_zone(directions, foci)
    validFoci = find_valid_foci(zone)
    lat = []
    long = []
    for f in foci:
        lat.append(location[f][1])
        long.append(location[f][0])
    return foci, zone, lat, long, validFoci, zoneUnits


def mistic(filePath, outputPath, outputProj, startYear, endYear, type):

    layer = reprojectLayer(filePath, outputProj)

    location = getLocation(layer)
    neighbors = shp_neighbors(layer)

    valid_foci_yr = []
    zone_units_yr = []
    foci_yr = []

    for year in range(startYear, endYear + 1):
        foci, zone, lat, long, validFoci, zoneUnits = process_year(
            year, layer, location, neighbors, type)
        foci_yr.append(foci)
        valid_foci_yr.append(validFoci)
        zone_units_yr.append(zoneUnits)
        writeOutputs(filePath, outputPath, foci, zone, lat, long, year)
    with open("config.json", "r") as f:
        data = json.load(f)
    with open("config.json", "w") as f:
        data['valid_foci'] = valid_foci_yr
        data['zone_units'] = zone_units_yr
        data['foci'] = foci_yr
        json.dump(data, f)
