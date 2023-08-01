import time

from osgeo import gdal
from rasterio.merge import merge
import rasterio as rio
from pathlib import Path

import os


# def reproject_tiff(input_file, output_file, target_srs):
#     gdal.Warp(output_file, input_file, dstSRS=target_srs)
#
#
# input_dir = "../output"
#
# input_files = [os.path.join(input_dir, f) for f in os.listdir(input_dir) if f.endswith('.tif')]

output_dir = "Tepke_reproject"

# os.makedirs(output_dir, exist_ok=True)
#
# target_srs = "EPSG:4326"
#
# for input_file in input_files:
#     file_name = os.path.splitext(os.path.basename(input_file))[0]
#     output_file = os.path.join(output_dir, f"{file_name}.tif")
#     reproject_tiff(input_file, output_file, target_srs)

# time.sleep(5)
path = Path(output_dir)
os.makedirs('Result', exist_ok=True)
output_path = 'Result/Tepke20cm.tif'
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
     "transform": output
     }
)

with rio.open(output_path, "w", **output_meta) as m:
    m.write(mosaic)



"""from pathlib import Path
import os
import rasterio as rio
from rasterio.merge import merge
import numpy as np

output_path = 'Result/Tepke20cm__1.tif'
output_dir = "Tepke_4"
# Ensure the output directory exists
os.makedirs('Result', exist_ok=True)

path = Path(output_dir)
raster_files = list(path.iterdir())
raster_to_mosaic = []
for p in raster_files:
    raster = rio.open(p)
    raster_to_mosaic.append(raster)

mosaic, output = merge(raster_to_mosaic)

# Create an alpha band
alpha = np.where(mosaic[0] != 0, 255, 0).astype(np.uint8)

# Append alpha band to your mosaic
mosaic = np.vstack((mosaic, alpha[None, :, :]))

output_meta = raster_to_mosaic[0].meta.copy()
output_meta.update(
    {"driver": "GTiff",
     "height": mosaic.shape[1],
     "width": mosaic.shape[2],
     "transform": output,
     "count": mosaic.shape[0],  # Update band count to reflect added alpha band
     }
)

with rio.open(output_path, "w", **output_meta) as m:
    m.write(mosaic)"""


import numpy as np
import rasterio as rio
from rasterio.merge import merge
from pathlib import Path
import os

# def reproject_tiff(input_file, output_file, target_srs):
#     gdal.Warp(output_file, input_file, dstSRS=target_srs)
#
# input_dir = "../output"
# input_files = [os.path.join(input_dir, f) for f in os.listdir(input_dir) if f.endswith('.tif')]

output_dir = "Tepke_reproject"
# os.makedirs(output_dir, exist_ok=True)
#
# target_srs = "EPSG:4326"
#
# for input_file in input_files:
#     file_name = os.path.splitext(os.path.basename(input_file))[0]
#     output_file = os.path.join(output_dir, f"{file_name}.tif")
#     reproject_tiff(input_file, output_file, target_srs)
#
# path = Path(output_dir)
# os.makedirs('Result', exist_ok=True)
# output_path = 'Result/Tepke20cm.tif'
#
# raster_to_mosaic = []
# for p in path.iterdir():
#     with rio.open(p) as src:
#         # Read the raster as array (including the mask)
#         arr = src.read(masked=True)
#         raster_to_mosaic.append((arr, src.transform))
#
# mosaic, output = merge(raster_to_mosaic)
#
# output_meta = raster.meta.copy()
# output_meta.update(
#     {"driver": "GTiff",
#      "height": mosaic.shape[1],
#      "width": mosaic.shape[2],
#      "transform": output,
#      "nodata": src.nodata
#      }
# )
#
# with rio.open(output_path, "w", **output_meta) as m:
#     m.write(mosaic)

