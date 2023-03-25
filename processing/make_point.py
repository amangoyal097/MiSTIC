try:
    from osgeo import ogr
except:
    import ogr
import os


def generate_point_layer(lat, long):
    outSHPfn = 'test.shp'
    fieldName = 'ID'
    fieldType = ogr.OFTString
    fieldValue = 'centroid'
    shpDriver = ogr.GetDriverByName("ESRI Shapefile")
    if os.path.exists(outSHPfn):
        shpDriver.DeleteDataSource(outSHPfn)
    outDataSource = shpDriver.CreateDataSource(outSHPfn)

    crs = ogr.osr.SpatialReference()
    crs.ImportFromEPSG(4326)

    outLayer = outDataSource.CreateLayer(outSHPfn, crs, geom_type=ogr.wkbPoint)
    idField = ogr.FieldDefn(fieldName, fieldType)
    outLayer.CreateField(idField)
    for i in range(len(lat)):
        newPoint = ogr.Geometry(ogr.wkbPoint)
        newPoint.AddPoint(lat[i], long[i])
        featureDefn = outLayer.GetLayerDefn()
        outFeature = ogr.Feature(featureDefn)
        outFeature.SetGeometry(newPoint)
        outFeature.SetField(fieldName, fieldValue)
        outLayer.CreateFeature(outFeature)
