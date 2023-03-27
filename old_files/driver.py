#!/usr/bin/python

import csv
import operator

from collections import Counter
from itertools import zip_longest

# from images import images_foci

nbhd = []
loc = []
unit_Names = []
data = []
num_of_Years = 10
num_of_Units = 153
dPoly = (
    []
)  # Usage of this variable can be removed to reduce space, only per year info needed
foci = []
zone_Poly = []
zone_Units = []
valid_foci = []
freq_Poly = []

freq_Poly_Names = []  # Temporary


def read_Neighbors(filename):
    """Get the spatial neighbor for each county"""

    # file_Path = prefix_Path + '/neighbors.csv'
    f = open(filename)

    # No header in neighbors
    try:
        reader = csv.reader(f)
        for row in reader:
            temp = []
            for col in row:
                if col:
                    temp.append(int(col))
            nbhd.append(temp)
            # print temp
    finally:
        f.close()


def read_Locations(prefix_Path):
    """Get the centroid of each polygon"""

    file_Path = prefix_Path + "/location.csv"
    f = open(file_Path)

    # No header in location

    try:
        reader = csv.reader(f)
        for row in reader:
            temp = []
            unit_Names.append(str(row[0]))
            X = float(row[1])
            Y = float(row[2])
            temp.append(X)
            temp.append(Y)
            loc.append(temp)
    finally:
        f.close()


def read_file(filename):
    """Read contents of file"""

    f = open(filename, "r")
    row_Num = 0
    count = []
    try:
        reader = csv.reader(f)
        for row in reader:
            if row_Num == 0:
                header = row
                row_Num += 1
            else:
                count.append(float(row[1]))
    finally:
        f.close()

    # Find foci for this year
    dp = mark_directions(count)
    dPoly.append(dp)

    # focus_Year is list of foci's for that year
    focus_Year = find_foci(dp)
    foci.append(focus_Year)

    zone_Year, units_in_zone = create_zone(dp, focus_Year)
    zone_Poly.append(zone_Year)
    zone_Units.append(units_in_zone)

    valid_foci_Year = find_valid_foci(zone_Year)
    valid_foci.append(valid_foci_Year)


def mark_directions(count):
    """Mark direction towards maximum value neighbor for a time unit"""

    dp = []
    for i in range(0, num_of_Units):
        nb = nbhd[i]
        diffs = []
        for j in range(0, len(nb)):
            diffs.append(count[nb[j] - 1] - count[i])
        index, value = max(enumerate(diffs), key=operator.itemgetter(1))
        if sign(value) == -1 or sign(value) == 0:
            dp.append(0)
        else:
            dp.append(nb[index])

    return dp


def find_foci(dp):
    """Return list of foci for a time unit"""

    f = []
    index = 0
    for item in dp:
        if item == 0:
            f.append(index + 1)
        index += 1

    return f


def create_zone(dp, focus_Year):
    """Return list containing zoneID for each spatial unit"""

    zone = [0] * num_of_Units
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


def write_data(output_Path, start_Year, end_Year):
    """Write Data to output files"""

    header = []
    for val in range(start_Year, end_Year + 1):
        header.append(val)

    validFoci_names = []
    filename = output_Path + "/validFoci.csv"
    itemLength = len(valid_foci[0])
    # print valid_foci
    with open(filename, "w") as fp:
        writer = csv.writer(fp, delimiter=",")
        writer.writerow(header)
        for values in zip_longest(*valid_foci):
            writer.writerow(values)
            fn_temp = []
            for v in values:
                if v:
                    fn_temp.append(unit_Names[v - 1])
                else:
                    fn_temp.append("")
            validFoci_names.append(fn_temp)

    foci_names = []
    filename = output_Path + "/foci.csv"
    itemLength = len(foci[0])
    # print valid_foci
    with open(filename, "w") as fp:
        writer = csv.writer(fp, delimiter=",")
        writer.writerow(header)
        for values in zip_longest(*foci):
            writer.writerow(values)
            fn_temp = []
            for v in values:
                if v:
                    fn_temp.append(unit_Names[v - 1])
                else:
                    fn_temp.append("")
            foci_names.append(fn_temp)

    filename = output_Path + "/foci_names.csv"
    with open(filename, "w") as fp:
        writer = csv.writer(fp, delimiter=",")
        for values in foci_names:
            writer.writerow(values)

    filename = output_Path + "/validFoci_names.csv"
    with open(filename, "w") as fp:
        writer = csv.writer(fp, delimiter=",")
        for values in validFoci_names:
            writer.writerow(values)

    filename = output_Path + "/zonePoly.csv"
    itemLength = len(zone_Poly[0])
    # print valid_foci
    with open(filename, "w") as fp:
        writer = csv.writer(fp, delimiter=",")
        writer.writerow(header)
        for values in zip_longest(*zone_Poly):
            writer.writerow(values)

    header = ["Frequency", "No of Polygons"]
    filename = output_Path + "/freq_vs_poly.csv"
    itemLength = len(freq_Poly)  # itemLength not used anywhere, can be removed?
    # print valid_foci
    with open(filename, "w") as fp:
        writer = csv.writer(fp, delimiter=",")
        writer.writerow(header)
        for values in freq_Poly:
            writer.writerow(values)

    filename = output_Path + "/fp_names.csv"
    with open(filename, "w") as fp:
        writer = csv.writer(fp, delimiter=",")
        for values in freq_Poly_Names:
            writer.writerow(values)

    filename = output_Path + "/all_foci_gis.csv"
    all_foci = [list(col) for col in zip(*dPoly)]
    with open(filename, "w") as fp:
        writer = csv.writer(fp, delimiter=",")
        for row in all_foci:
            writer.writerow(row)

    print("Output files created")


def mistic(
    prefix_Path, output_Path, neighbor_file, sp_Units, time_Units, start_Year, end_Year
):

    file_Prefix = prefix_Path + "/DM_"
    cur_Year = int(start_Year)

    count_Year = 0
    num_of_Years = int(time_Units)
    num_of_Units = int(sp_Units)

    read_Neighbors(neighbor_file)
    read_Locations(prefix_Path)

    while count_Year < num_of_Years:
        filename = file_Prefix + str(cur_Year) + ".csv"
        cur_Year = cur_Year + 1
        count_Year = count_Year + 1
        read_file(filename)

    freq_vs_poly()
    write_data(output_Path, int(start_Year), int(end_Year))

    # images_foci(output_Path, neighbor_file, foci, loc, num_of_Years)


def freq_vs_poly():
    """Return frequency vs No of polygons occurrences"""

    poly_count = {}
    for i in range(1, num_of_Units + 1):
        poly_count[i] = 0

    for yr in range(num_of_Years):
        for ind in valid_foci[yr]:
            poly_count[ind] += 1

    """ fP_names is Temporary """

    fP = {}
    fP_names = {}
    for key in poly_count:
        if poly_count[key] in fP:
            fP[poly_count[key]] += 1
            fP_names[poly_count[key]].append(unit_Names[key - 1])
        else:
            fP[poly_count[key]] = 1
            fP_names[poly_count[key]] = list()
            fP_names[poly_count[key]].append(unit_Names[key - 1])

    for key in fP_names:
        temp = []
        temp.append(key)
        temp.append(fP_names[key])
        freq_Poly_Names.append(temp)

    sorted_fP = sorted(fP.items(), reverse=True)  # sorted_fP is List of Tuples

    for item in sorted_fP:
        temp = []
        temp.append(item[0])
        temp.append(item[1])
        freq_Poly.append(temp)


def sign(a):
    return (a > 0) - (a < 0)
