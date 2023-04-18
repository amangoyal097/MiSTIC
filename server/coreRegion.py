import operator
import csv
from itertools import zip_longest
from math import *

sorted_rF = {}
core_classify_name = {-1: "None", 0: "CHD", 1: "CLD", 2: "CND"}
# -1 - None
# 0 - CHD
# 1 - CLD
# 2 - CND

max_prune_value = 0
min_freq_value = 0
cr_radius_value = 0


def convert_percent_to_time(min_sup_frac, itf, num_of_Years):
    """
    Convert initial threshold frequency and minimum support
    value percentages to time units.

    """
    msp = ceil((min_sup_frac / 100.0) * num_of_Years)
    itf = ceil((itf / 100.0) * num_of_Years)
    return msp, itf


def classify_params(max_prune_value, min_freq_value, num_of_Years):
    """
    Return minimum frequency of time units
    Enter percentage.

    """
    max_prune_value = [
        ceil((value / 100.0) * num_of_Years) for value in max_prune_value
    ]
    min_freq_value = [floor((value / 100.0) * num_of_Years)
                      for value in min_freq_value]

    return max_prune_value, min_freq_value


def classify(num_foci_cc, max_prune_value, min_freq_value, info, foci, core_classify):
    """
    Classify the ref_foci's into CHD, CLD and CND based on the max_Prune and
    min_Freq values given by user.

    """
    for i in range(num_foci_cc):
        num_zero_years = info[i].count(0)
        # Below 'freq' may not necessarily be the frequency of current_ref_focus
        freq = max(foci[i].values())
        ctype = -1
        if num_zero_years <= max_prune_value[0] and freq >= min_freq_value[1]:
            ctype = 0  # CHD
        elif num_zero_years > max_prune_value[1] and freq < min_freq_value[0]:
            ctype = 2  # CND
        else:
            ctype = 1  # CLD

        core_classify[i] = ctype


def find_ref_foci(itf_value, itf, output_Path, ref_foci, num_of_Units, num_of_Years, valid_foci):
    """
    Find initial list of ref foci.
    This list of foci is just an initial set to begin analysis [CC/CR] with.
    WHile doing CC/CR, the list might reduce as some of the foci may merge as per
    neighborhood constraints.

    The final number of core foci for CC and CR might be different.

    """

    rF = {}
    for i in range(1, num_of_Units + 1):
        rF[i] = 0

    for yr in range(num_of_Years):
        for ind in valid_foci[yr]:
            rF[ind] += 1

    global sorted_rF
    sorted_rF = sorted(rF.items(), key=operator.itemgetter(1), reverse=True)

    for tuples in sorted_rF:
        if tuples[1] >= itf_value:
            ref_foci.append(tuples[0])

    # Write sorted_rF to FILE
    # Write ref_foci to FILE
    header = ["initial TF", itf, itf_value]
    filename = output_Path + "/initial_ref_foci_{}.csv".format(itf)
    with open(filename, "w") as fp:
        writer = csv.writer(fp, delimiter=",")
        writer.writerow(header)
        for value in ref_foci:
            writer.writerow([value])

    return rF


def merge_adjacent_foci(mode, ref_foci, nbhd):
    """
    Incorrect logic. Remove this function.

    Merge foci which are adjacent.

    """
    for tuples in sorted_rF:
        polygon = tuples[0]
        if polygon in ref_foci:
            n = nbhd[str(polygon - 1)]
            # find neighbors of polygon
            # 2 levels for CR - ?
            # remove polygon from neighbors
            # find intersection with ref_foci
            common = list(set(n) & set(ref_foci))
            for element in common:
                ref_foci.remove(element)  # remove them from ref_foci


def find_core_zones(ccInfo, ref_foci, core_zone_influence, num_of_Years, zone_Units):

    for i in range(len(ref_foci)):
        zone_for_one_core = set()
        for j in range(num_of_Years):
            # zone_Units is list of dicts
            zone_elements = zone_Units[j]
            focus = ccInfo[i][j]
            if focus:
                zone_of_focus = zone_elements[str(focus)]
                zone_for_one_core = zone_for_one_core.union(set(zone_of_focus))

        core_id = ref_foci[i]
        zone_for_one_core = list(zone_for_one_core)
        if core_id not in zone_for_one_core:
            zone_for_one_core.append(core_id)

        core_zone_influence.append(zone_for_one_core)
        # print 'zone_for_one_core  {}:  {}'.format(ref_foci[i], zone_for_one_core)


def init(numFoci, crInfo, crFoci, num_of_Years):
    """Initialize global variables of this file to be used"""

    for i in range(numFoci):
        # ccInfo.append([0]*num_of_Years)
        crInfo.append([0] * num_of_Years)
        # ccFoci.append({})
        crFoci.append({})


def find_cc(itf_value, min_sup_value, ref_foci, all_foci_frequency, num_of_Years, valid_foci, foci, nbhd, loc):
    """Find Info about CC"""

    ccInfo = []
    ccFoci = []
    final_cc_foci = []
    processed_foci = []

    for i, focus in enumerate(ref_foci):

        if itf_value == 0:
            if all_foci_frequency[focus] < min_sup_value:
                break

        ccInfo_year = [0] * num_of_Years
        ccFoci_year = {}
        current_rF = focus
        ccPrev = current_rF
        processed_foci.append(focus)

        for j in range(num_of_Years):
            vF = valid_foci[j]
            F = foci[j]

            if ccPrev in vF:
                ccInfo_year[j] = ccPrev
            else:
                ccLoc = loc[str(ccPrev - 1)]  # ccLoc is [X Y]
                n = nbhd[str(ccPrev - 1)]  # n is list of neighbors
                I = list(set(n) & set(vF))  # find intersection with valid_foci
                if I:
                    # It cannot be a NS timestep as there are nbhd which are validfoci.
                    # It can still be NF timestep as they might not qualify min_sup criteria.
                    if len(I) > 1:
                        # More than one possible nbhd foci. Check min_dist from ccPrev
                        # and also if they are above min_sup.
                        nLoc = []
                        for polygon in I:
                            nLoc.append(loc[str(polygon - 1)])
                        ccDist = [0] * len(I)
                        for k in range(len(I)):
                            ccDist[k] = sqrt(
                                pow(ccLoc[0] - nLoc[k][0], 2)
                                + pow(ccLoc[1] - nLoc[k][1], 2)
                            )

                        nbhd_and_dist = zip(I, ccDist)
                        sorted_nbhd_and_dist = sorted(
                            nbhd_and_dist, key=operator.itemgetter(1)
                        )

                        for nbhd_poly, dist in sorted_nbhd_and_dist:
                            if all_foci_frequency[nbhd_poly] >= min_sup_value:
                                # Qualifies
                                ccInfo_year[j] = nbhd_poly
                                ccPrev = nbhd_poly
                                if (
                                    nbhd_poly in ref_foci
                                    and nbhd_poly not in processed_foci
                                ):
                                    # remove from ref_foci as it is now part of another core.
                                    ref_foci.remove(nbhd_poly)
                                break
                    else:
                        # Only one intersection. Check if it is above min_sup.
                        if all_foci_frequency[I[0]] >= min_sup_value:
                            # Qualifies
                            ccInfo_year[j] = I[0]
                            ccPrev = I[0]
                            if I[0] in ref_foci and I[0] not in processed_foci:
                                # remove from ref_foci as it is now part of another core.
                                ref_foci.remove(I[0])

            if ccInfo_year[j] in ccFoci_year:
                ccFoci_year[ccInfo_year[j]] += 1
            else:
                ccFoci_year[ccInfo_year[j]] = 1

        ccInfo.append(ccInfo_year)
        ccFoci.append(ccFoci_year)

    # At the end, ref_foci contains final list of cc ref foci.
    return ccInfo, ccFoci, processed_foci


def write_data_cc(
    output_Path,
    ccInfo,
    ccFoci,
    start_Year,
    end_Year,
    min_Support,
    ref_foci,
    core_classify_cc,
    core_zone_influence,
):
    """Write CC Core Data to files"""

    header = [""]
    for val in ref_foci:
        header.append(val)

    years = []
    for val in range(start_Year, end_Year + 1):
        years.append(val)

    ccInfo = [years] + ccInfo
    filename = output_Path + "/ccInfo_{}.csv".format(min_Support)

    core_id = ["core id"] + core_classify_cc
    core_type_names = ["core type"] + [core_classify_name[i]
                                       for i in core_classify_cc]
    with open(filename, "w") as fp:
        writer = csv.writer(fp, delimiter=",")
        writer.writerow(header)
        for values in zip_longest(*ccInfo):
            writer.writerow(values)
        writer.writerow(core_id)
        writer.writerow(core_type_names)

    header = []
    for val in ref_foci:
        header.append(val)
    filename = output_Path + "/core_zone_influence_{}.csv".format(min_Support)
    with open(filename, "w") as fp:
        writer = csv.writer(fp, delimiter=",")
        writer.writerow(header)
        for values in zip_longest(*core_zone_influence):
            writer.writerow(values)


def find_cr(numFoci, crInfo, crFoci, ref_foci, num_of_Years, valid_foci, foci, nbhd, loc):
    """Find Info about CR"""

    for i in range(numFoci):
        current_rF = ref_foci[i]

        for j in range(num_of_Years):
            vF = valid_foci[j]
            F = foci[j]

            if current_rF in vF:
                crInfo[i][j] = current_rF
            else:
                crLoc = loc[str(current_rF - 1)]  # crLoc is [X Y]
                n = nbhd[str(current_rF - 1)]  # n is list of neighbors
                temp = n
                # Adding 2nd level Neighbors to n to check for foci shift in current RF being considered
                # To be changed depending on CR value
                for k in range(len(n)):
                    temp = list(set(temp) | set(nbhd[str(n[k] - 1)]))
                temp.remove(current_rF)
                n = temp
                I = list(set(n) & set(vF))  # find intersection with valid_foci
                if I:
                    ind = 0
                    if len(I) > 1:
                        nLoc = []
                        for polygon in I:
                            nLoc.append(loc[str(polygon - 1)])
                        crDist = [0] * len(I)
                        for k in range(len(I)):
                            crDist[k] = sqrt(
                                pow(crLoc[0] - nLoc[k][0], 2)
                                + pow(crLoc[1] - nLoc[k][1], 2)
                            )
                        val = min(crDist)
                        ind = crDist.index(val)
                    crInfo[i][j] = I[ind]
            if not bool(crFoci[i]):  # can be removed
                crFoci[i][crInfo[i][j]] = 1
            else:
                # Search for crInfo[i][j] in crFoci[i]
                if crInfo[i][j] in crFoci[i]:
                    crFoci[i][crInfo[i][j]] += 1
                else:
                    crFoci[i][crInfo[i][j]] = 1


def write_data_cr(
    output_Path,
    crInfo,
    crFoci,
    start_Year,
    end_Year,
    min_Support,
    ref_foci,
    core_classify_cr,
):
    """Write CR Core Data to files"""

    header = [""]
    for val in ref_foci:
        header.append(val)

    years = []
    for val in range(start_Year, end_Year + 1):
        years.append(val)

    crInfo = [years] + crInfo
    filename = output_Path + "/crInfo_{}.csv".format(min_Support)

    core_id = ["core id"] + core_classify_cr
    core_type_names = ["core type"] + [core_classify_name[i]
                                       for i in core_classify_cr]
    with open(filename, "w") as fp:
        writer = csv.writer(fp, delimiter=",")
        writer.writerow(header)
        for values in zip_longest(*crInfo):
            writer.writerow(values)
        writer.writerow(core_id)
        writer.writerow(core_type_names)

    header = [""]
    for val in ref_foci:
        header.append(val)
    filename = output_Path + "/crFoci_{}.csv".format(min_Support)


def core_analysis(
    output_Path,
    start_Year,
    end_Year,
    itf,
    min_Support,
    max_Prune,
    min_Freq,
    cr_Radius,
    mode,
    data
):
    """
    Call relevant functions for core analysis.

    """
    # ccInfo = []
    # ccFoci = []
    crInfo = []
    crFoci = []
    ref_foci = []
    ref_foci_parent = []
    core_zone_influence = []

    itf = int(itf)  # in percentage
    min_Support = int(min_Support)  # in percentage
    max_Prune = int(max_Prune)  # in percentage
    min_Freq = int(min_Freq)  # in percentage

    if mode != 0:
        cr_radius_value = int(cr_Radius)

    # Percentage values for max_Prune and min_Freq are hard-coded for now.
    # Will be removed once the logic is clarified. Will have to modify design of UI
    # to accept two values for each param instead of one.
    max_Prune = [10, 30]
    min_Freq = [30, 70]

    # Get max_prune_value and min_freq_value in time units
    max_prune_value, min_freq_value = classify_params(
        max_Prune, min_Freq, end_Year - start_Year + 1)
    print(max_prune_value)
    print(min_freq_value)

    # Get minimum support value in time units
    min_sup_value, itf_value = convert_percent_to_time(
        min_Support, itf, end_Year - start_Year + 1)

    # Find initial set of reference foci to begin with
    all_foci_frequency = find_ref_foci(itf_value, itf, output_Path, ref_foci,
                                       data['featureCount'], end_Year - start_Year + 1, data['valid_foci'])

    # merge_adjacent_foci(mode, ref_foci) # need to send mode

    numFoci = len(ref_foci)
    ref_foci_parent = [-1] * numFoci
    init(numFoci, crInfo, crFoci, end_Year - start_Year + 1)

    ref_foci_cc = ref_foci[:]
    ref_foci_cr = ref_foci[:]

    if mode == 0:
        print(len(ref_foci_cc))
        ccInfo, ccFoci, ref_foci_new = find_cc(
            itf_value, min_sup_value, ref_foci_cc, all_foci_frequency, end_Year -
            start_Year +
            1, data['valid_foci'], data['foci'], data['nbhd'], data['loc']
        )
        ref_foci_cc = ref_foci_new
        print(ref_foci_cc)
        find_core_zones(ccInfo, ref_foci_cc, core_zone_influence,
                        end_Year - start_Year + 1, data['zone_units'])
        # merge_ref_foci(ref_foci_parent, ref_foci)
        # The method classify will classify all those ref_foci's before they were merged.
        # However, it is unclear whether the classification is to be done before or after merging.?
        num_foci_cc = len(ref_foci_cc)
        print("Num_foci_cc = ", num_foci_cc)
        core_classify_cc = [-1] * num_foci_cc
        classify(
            num_foci_cc,
            max_prune_value,
            min_freq_value,
            ccInfo,
            ccFoci,
            core_classify_cc,
        )
        write_data_cc(
            output_Path,
            ccInfo,
            ccFoci,
            int(start_Year),
            int(end_Year),
            min_Support,
            ref_foci_cc,
            core_classify_cc,
            core_zone_influence,
        )
    # if mode == 1:
    #     find_cr(numFoci, crInfo, crFoci, ref_foci)
    #     # core_classify_cr = [-1] * num_foci_cr
    #     classify(
    #         numFoci, max_prune_value, min_freq_value, crInfo, crFoci, core_classify_cr
    #     )
    #     write_data_cr(
    #         output_Path,
    #         crInfo,
    #         crFoci,
    #         int(start_Year),
    #         int(end_Year),
    #         min_Support,
    #         ref_foci,
    #         core_classify_cr,
    #     )
    # if mode == 2:
    #     find_cc(numFoci, ccInfo, ccFoci, ref_foci)
    #     find_cr(numFoci, crInfo, crFoci, ref_foci)
    #     classify(
    #         numFoci, max_prune_value, min_freq_value, ccInfo, ccFoci, core_classify_cc
    #     )
    #     write_data_cc(
    #         output_Path,
    #         ccInfo,
    #         ccFoci,
    #         int(start_Year),
    #         int(end_Year),
    #         min_Support,
    #         ref_foci,
    #         core_classify_cc,
    #     )
    #     classify(
    #         numFoci, max_prune_value, min_freq_value, crInfo, crFoci, core_classify_cr
    #     )
    #     write_data_cr(
    #         output_Path,
    #         crInfo,
    #         crFoci,
    #         int(start_Year),
    #         int(end_Year),
    #         min_Support,
    #         ref_foci,
    #         core_classify_cr,
    #     )
