import os, osgeo, math, numpy as np
from osgeo import gdal, ogr, osr
from scipy.spatial import Delaunay

root = "/Users/anubhav/Downloads/sample_data/"  # directory with input point shp
input_shp_full = root + "settlement_pnts_clip.shp"  # point shp
fieldUID = "ORIG_FID"  # field in point shp with pt IDs
out_dir = (
    root + "out-voronoi/"
)  # output directory to hold buffered points and Voronoi polygons
proj = 4326  # http://spatialreference.org/ref/epsg/wgs-84/

#################
### INPUT DATA ###
#################

# read in shp file
print("- reading", input_shp_full)
drv = ogr.GetDriverByName("ESRI Shapefile")
ptShp = drv.Open(input_shp_full)
ptLayer = ptShp.GetLayer(0)
ptSRS = ptLayer.GetSpatialRef()
x_min, x_max, y_min, y_max = ptLayer.GetExtent()

# collect point coordinates and ID
ptList = []
ptDict = {}
for pt in ptLayer:
    ID_index = pt.GetFieldIndex(fieldUID)
    ptID = pt.GetField(ID_index)
    ptGeom = pt.GetGeometryRef()
    ptX = float(str(ptGeom).split(" ")[1].strip("("))
    ptY = float(str(ptGeom).split(" ")[2].strip(")"))
    ptDict[ptID] = [
        ptX,
        ptY,
    ]  # a bit redundant to have dict and list, but list is used for Delaunay input
    ptList.append([ptX, ptY])

print("\t>> read", len(ptList), "points")
numPtList = np.array(ptList)  # set-up for input to Delaunay

#########################
### RADIAL BUFFER PTS ###
########################

# declare buffering distance in units appropriate for spatial reference system
# here, we're in WGS84 so we'll buffer by 1/100th of a degree
bufferDistance = 0.01  # degrees
print("- buffering", input_shp_full, "at", bufferDistance, "deg")

# set-up output buffered point shp
drv = ogr.GetDriverByName("Esri Shapefile")
buffShp = out_dir + input_shp_full.split("/")[-1].replace(".shp", "_buffer.shp")
if os.path.exists(buffShp):
    os.remove(buffShp)
ds = drv.CreateDataSource(buffShp)
layer = ds.CreateLayer("", None, ogr.wkbPolygon)
layer.CreateField(ogr.FieldDefn("Id", ogr.OFTInteger))
defn = layer.GetLayerDefn()

# run through points and buffer each by established distance
ptCounter = 0
for each in ptDict:
    ptLon = ptDict[each][0]
    ptLat = ptDict[each][1]
    # print "buffering point at lat-lon",ptLat,"-",ptLon
    pt_wkt = "POINT (" + str(ptLon) + " " + str(ptLat) + ")"
    pt = ogr.CreateGeometryFromWkt(pt_wkt)

    geom = pt.Buffer(bufferDistance)
    feat = ogr.Feature(defn)
    feat.SetField("Id", each)
    feat.SetGeometry(geom)
    layer.CreateFeature(feat)
    feat = geom = None
    ptCounter += 1

print("\t>> buffered", ptCounter, "points in")
layer = ds = None

########################
### VORONOI POLYGONS ##
########################

# References
# http://en.wikipedia.org/wiki/Circumscribed_circle#Circumscribed_circles_of_triangles
# https://stackoverflow.com/questions/12374781/how-to-find-all-neighbors-of-a-given-point-in-a-delaunay-triangulation-using-sci
# https://stackoverflow.com/questions/10650645/python-calculate-voronoi-tesselation-from-scipys-delaunay-triangulation-in-3d

# read in points to Delaunay function
print("- converting points in", input_shp_full, "to Voronoi polygons")
tri = Delaunay(numPtList)

# returns point locations of each triangle vertex
# tri.vertices: each row represents one simplex (triangle) in the triangulation,
# with values referencing indices of the input point list
p = tri.points[tri.vertices]

# find facets containing each input point
print("\tfinding Delaunay triangle facets")
triDict = {}
i = 0
# while i >exported '+str(ptCounter)+' Voronoi vertices'
nodeLayer = outNodeShp = None

# build polygons with vertices at identified nodes
# assign input shp pt IDs to polygons

# https://stackoverflow.com/questions/1709283/how-can-i-sort-a-coordinate-list-for-a-rectangle-counterclockwise
# https://gamedev.stackexchange.com/questions/13229/sorting-array-of-points-in-clockwise-order
# https://en.wikipedia.org/wiki/Graham_scan
def sortCCW(node):
    return math.atan2(node[1] - meanLat, node[0] - meanLon)


# set-up output polygon shp
vorShp = out_dir + input_shp_full.split("/")[-1].replace(".shp", "_voronoi.shp")
print("- creating output polygon shp", vorShp.split("/")[-1])
if os.path.exists(vorShp):
    os.remove(vorShp)
drv = ogr.GetDriverByName("ESRI Shapefile")
outShp = drv.CreateDataSource(vorShp)
layer = outShp.CreateLayer("", None, ogr.wkbPolygon)
layer.CreateField(ogr.FieldDefn("Id", ogr.OFTInteger))
layerDefn = layer.GetLayerDefn()

# find nodes surrounding polygon centroid
# sort nodes in counterclockwise order
# create polygon perimeter through nodes
print("- building Voronoi polygons around point...")
for pt in vorIdDict:
    print("\t", pt)
    meanLon = sum(node[0] for node in vorIdDict[pt]) / len(vorIdDict[pt])
    meanLat = sum(node[1] for node in vorIdDict[pt]) / len(vorIdDict[pt])
    hullList = vorIdDict[pt].tolist()
    hullList.sort(key=sortCCW)

    poly = ogr.Geometry(ogr.wkbPolygon)
    ring = ogr.Geometry(ogr.wkbLinearRing)
    i = 0
    for node in hullList:
        if i == 0:
            loopLon = node[0]  # grab first node to close ring
            loopLat = node[1]
        ring.AddPoint(node[0], node[1])
        i += 1
    ring.AddPoint(loopLon, loopLat)
    poly.AddGeometry(ring)
    feat = ogr.Feature(layerDefn)
    feat.SetField("Id", pt)
    feat.SetGeometry(poly)
    layer.CreateFeature(feat)
    feat = poly = ring = None
layer = outShp = None
