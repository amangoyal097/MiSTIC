import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import random


def get_colors(n):
    colors = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
              for i in range(n)]
    return colors


def plot_foci(filePath, foci, zone, lat, long):

    colors = get_colors(len(foci))
    colorMap = {}
    for i, f in enumerate(foci):
        colorMap[f] = colors[i]
    zone_colors = [colorMap[z] for z in zone]
    map_df = gpd.read_file("../shapefile/district.shp")
    map_df['color'] = zone_colors
    zones = map_df.dissolve(by='color')
    df = pd.DataFrame(
        {
            'Latitude': lat,
            'Longitude': long})
    foci_df = gpd.GeoDataFrame(
        df, geometry=gpd.points_from_xy(df.Longitude, df.Latitude))
    fig, ax = plt.subplots(figsize=(15, 15))
    zones.boundary.plot(ax=ax, alpha=0.7, color=map_df['color'])
    foci_df.plot(ax=ax)
    plt.show()
