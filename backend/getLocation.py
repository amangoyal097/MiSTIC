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
import os
import geopandas as gpd
import json


def getXY(pt):
    return (pt.x, pt.y)


def getLocation(filePath):
    vector_ds = ogr.Open(filePath, gdalconst.GA_ReadOnly)
    file_name = os.path.basename(filePath).split(".")[0]
    ly = vector_ds.ExecuteSQL(
        'SELECT ST_Centroid(geometry), * FROM ' + file_name, dialect='sqlite')
    feature = ly.GetNextFeature()
    count = 1
    location = {}
    while feature:
        geo = feature.GetGeometryRef()
        location[count] = [geo.GetX(), geo.GetY()]
        feature = ly.GetNextFeature()
        count += 1
    with open("config.json", "r") as f:
        data = json.load(f)
    with open("config.json", "w") as f:
        data['loc'] = location
        json.dump(data, f)
    return location
