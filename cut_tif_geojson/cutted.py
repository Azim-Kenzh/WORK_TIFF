import os

from osgeo import gdal

outputpath = 'Result_GEOJSON/'
os.makedirs(outputpath, exist_ok=True)
inputpath = '../mosaik/Result/Tepke20cm.tif'
polygon = 'json/Tepke.geojson'

cutted_image = gdal.Warp(destNameOrDestDS=f"{outputpath}Tepke_20cm(EPSG:7695).tif",
                         srcDSOrSrcDSTab=inputpath,
                         cutlineDSName=polygon,
                         cropToCutline=True,
                         copyMetadata=True,
                         dstNodata=0)
cutted_image = None
