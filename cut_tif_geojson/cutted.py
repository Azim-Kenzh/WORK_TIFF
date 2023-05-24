import os

from osgeo import gdal

outputpath = 'Result_GEOJSON_BANDS/'
os.makedirs(outputpath, exist_ok=True)
inputpath = '../mosaik/Result/KR_BAND.tif'
polygon = 'json/KR_GEOJSON.geojson'

cutted_image = gdal.Warp(destNameOrDestDS=f"{outputpath}FULL_KR_BAND_GEOJSON.tif",
                         srcDSOrSrcDSTab=inputpath,
                         cutlineDSName=polygon,
                         cropToCutline=True,
                         copyMetadata=True,
                         dstNodata=0)
cutted_image = None
