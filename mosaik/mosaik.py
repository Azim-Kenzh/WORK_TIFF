import time

from osgeo import gdal
from rasterio.merge import merge
import rasterio as rio
from pathlib import Path

import os


def reproject_tiff(input_file, output_file, target_srs):
    gdal.Warp(output_file, input_file, dstSRS=target_srs)


input_dir = "../merge_tif_and_create_rgb/RESULT_RGB"

input_files = [os.path.join(input_dir, f) for f in os.listdir(input_dir) if f.endswith('.tif')]

output_dir = "KR_reproject_BANDS"

os.makedirs(output_dir, exist_ok=True)

target_srs = "EPSG:4326"

for input_file in input_files:
    file_name = os.path.splitext(os.path.basename(input_file))[0]
    output_file = os.path.join(output_dir, f"{file_name}.tif")
    reproject_tiff(input_file, output_file, target_srs)

# time.sleep(5)
path = Path(output_dir)
os.makedirs('Result', exist_ok=True)
output_path = 'Result/KR_BAND.tif'
raster_files = list(path.iterdir())
raster_to_mosiac = []
for p in raster_files:
    raster = rio.open(p)
    raster_to_mosiac.append(raster)

mosaic, output = merge(raster_to_mosiac)

output_meta = raster.meta.copy()
output_meta.update(
    {"driver": "GTiff",
     "height": mosaic.shape[1],
     "width": mosaic.shape[2],
     "transform": output,
     }
)

with rio.open(output_path, "w", **output_meta) as m:
    m.write(mosaic)