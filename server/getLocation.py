import json


def getXY(pt):
    return (pt.x, pt.y)


def getLocation(layer):
    count = 1
    location = {}
    for centroid in layer.centroid:
        location[count] = [centroid.x, centroid.y]
        count += 1
    with open("config.json", "r") as f:
        data = json.load(f)
    with open("config.json", "w") as f:
        data['loc'] = location
        json.dump(data, f)
    return location
