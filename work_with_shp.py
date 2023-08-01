#
# # Загрузите ваш shapefile
# gdf = gpd.read_file("SHP/asdf.shp")
# print(gdf)
# # Проверьте текущую проекцию
# print(gdf.crs)
#
# # Преобразуйте в WGS84 (EPSG:4326)
# gdf_wgs84 = gdf.to_crs("EPSG:7684")
#
# # Сохраните новый shapefile
# gdf_wgs84.to_file("1.shp")
# #
# #
# shp_data = gpd.read_file('1.shp')
# shp_data['FILENAME'] = shp_data['FILENAME'].str.replace('Z:\\2019 KYRGYZSTAN\\EXPORT FINAL\\ISSYK KUL LAKE 20CM\\', '').str.replace('TIFF ORTHO\\', '')
# print(shp_data)


# shp_data = gpd.read_file('SHP/Administrative/Settelment_pol.shp')
# print(shp_data)

"""import geopandas as gpd
shp_data = gpd.read_file('gipro/4368_4738-RGB-20cm.tif')

# shp_data.set_crs(epsg=4326, inplace=True)

# Reproject the data to the Kyrg-06 CRS
shp_data = shp_data.to_crs(epsg=7695)

polygons = shp_data['geometry']

# convert the polygons to a list for json serialization
polygons_list = [polygon.wkt for polygon in polygons]

print(polygons_list)"""
from shapely.ops import orient

"""import os
import rasterio
from rasterio.warp import calculate_default_transform, reproject, Resampling

src_dir = 'gipro'  # Source directory
dst_dir = 'output'  # Destination directory
dst_crs = 'EPSG:7695'  # Your desired CRS

if not os.path.exists(dst_dir):
    os.makedirs(dst_dir)

# List all .tif files in the source directory
src_files = [f for f in os.listdir(src_dir) if f.endswith('.tif')]

for src_file in src_files:
    src_path = os.path.join(src_dir, src_file)
    dst_path = os.path.join(dst_dir, src_file)

    with rasterio.open(src_path) as src:
        transform, width, height = calculate_default_transform(src.crs, dst_crs, src.width, src.height, *src.bounds)
        kwargs = src.meta.copy()
        kwargs.update({
            'crs': dst_crs,
            'transform': transform,
            'width': width,
            'height': height
        })

        with rasterio.open(dst_path, 'w', **kwargs) as dst:
            for i in range(1, src.count + 1):
                reproject(
                    source=rasterio.band(src, i),
                    destination=rasterio.band(dst, i),
                    src_transform=src.transform,
                    src_crs=src.crs,
                    dst_transform=transform,
                    dst_crs=dst_crs,
                    resampling=Resampling.nearest)"""

"""from shapely.geometry import mapping, shape, Polygon, MultiPolygon
import json


def enforce_right_hand_rule(geom_dict):
    geom = shape(geom_dict)
    if isinstance(geom, (Polygon, MultiPolygon)):
        geom = orient(geom, sign=1.0)  # в соответствии с правилом правой руки
    return mapping(geom)


# Пример использования этой функции
with open('forest.geojson', 'r') as f:
    data = json.load(f)

data['features'] = [{**feat, 'geometry': enforce_right_hand_rule(feat['geometry'])} for feat in data['features']]

with open('fixed_forest.geojson', 'w') as f:
    json.dump(data, f)"""


import json

with open('fixed_forest.geojson', 'r') as f:
    data = json.load(f)

if 'crs' in data:
    del data['crs']

with open('fixed_forest_crs.geojson', 'w') as f:
    json.dump(data, f)
