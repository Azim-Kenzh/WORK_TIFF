# import os
# from osgeo import gdal, osr
# import fiona
# from shapely.geometry import shape
#
# # Открываем shapefile с использованием Fiona
# with fiona.open("gipro/картограмма.shp", "r") as shapefile:
#     geoms = [shape(feature["geometry"]) for feature in shapefile]
#     print(geoms)
# # Получаем границы из shapefile
# minx, miny, maxx, maxy = geoms[0].bounds
#
# # Устанавливаем систему координат
# srs = osr.SpatialReference()
# srs.ImportFromEPSG(4326)  # здесь используется WGS84
#
# # Папка с TIF файлами
# folder = "Tepke"
#
# # Получаем список всех TIF файлов в папке
# tif_files = [f for f in os.listdir(folder) if f.endswith('.tif')]
# print(tif_files)
# #
# # # Обрабатываем каждый TIF файл
# # for tif_file in tif_files:
# #     # Полный путь до файла
# #     full_path = os.path.join(folder, tif_file)
# #
# #     # Загружаем изображение
# #     ds = gdal.Open(full_path, gdal.GA_ReadOnly)
# #
# #     # Устанавливаем геопреобразование
# #     gt = [minx, (maxx - minx) / ds.RasterXSize, 0, maxy, 0, (miny - maxy) / ds.RasterYSize]
# #
# #     # Создаем новый файл из исходного изображения
# #     ds_out = gdal.GetDriverByName('GTiff').Create(f"output_{tif_file}", ds.RasterXSize, ds.RasterYSize, ds.RasterCount,
# #                                                   gdal.GDT_Byte)
# #     ds_out.SetGeoTransform(gt)
# #     ds_out.SetProjection(srs.ExportToWkt())
# #
# #     # Копируем данные
# #     for i in range(ds.RasterCount):
# #         band = ds.GetRasterBand(i + 1)
# #         data = band.ReadAsArray()
# #         out_band = ds_out.GetRasterBand(i + 1)
# #         out_band.WriteArray(data)
# #
# #     ds = None
# #     ds_out = None

# import rasterio
# from rasterio.warp import calculate_default_transform, reproject, Resampling
#
# dst_crs = 'EPSG:4326'
#
# with rasterio.open('Tepke/4368_4736-RGB-20cm.tif', 'r',
#                     GEOREF_SOURCES='NO_GEOTRANSFORM') as src:
#
#     transform, width, height = calculate_default_transform(
#         src.crs, dst_crs, src.width, src.height, *src.bounds)
#     kwargs = src.meta.copy()
#     kwargs.update({
#         'crs': dst_crs,
#         'transform': transform,
#         'width': width,
#         'height': height
#     })
#
#     with rasterio.open('output.tif', 'w', **kwargs) as dst:
#         for i in range(1, src.count + 1):
#             reproject(
#                 source=rasterio.band(src, i),
#                 destination=rasterio.band(dst, i),
#                 src_transform=src.transform,
#                 src_crs=src.crs,
#                 dst_transform=transform,
#                 dst_crs=dst_crs,
#                 resampling=Resampling.nearest)


import geopandas as gpd
import pandas as pd
import rasterio
from rasterio.transform import from_origin
from rasterio.crs import CRS

"""# Загрузите данные shapefile
# shp_data = gpd.read_file('gipro/картограмма.shp')
shp_data = gpd.read_file('eu.shp')
shp_data['FILENAME'] = shp_data['FILENAME'].str.replace('Z:\\2019 KYRGYZSTAN\\EXPORT FINAL\\ISSYK KUL LAKE 20CM\\', '').str.replace('TIFF ORTHO\\', '')
print(shp_data)
# Переберите все ваши файлы TIFF
for tiff_file in shp_data['FILENAME']:
    # Получите соответствующую запись из данных shapefile
    record = shp_data[shp_data['FILENAME'] == tiff_file].iloc[0]
    # Удалите текст " meters" и преобразуйте значения ширины и высоты пикселей в числовые
    pixel_width = pd.to_numeric(record['PIXEL_WIDT'].replace(' meters', ''))
    pixel_height = pd.to_numeric(record['PIXEL_HEIG'].replace(' meters', ''))

    # Задайте новую трансформацию
    new_transform = from_origin(record['UPPER_LE_X'], record['UPPER_LE_Y'], pixel_width, pixel_height)

    # Загрузите ваш файл TIFF
    with rasterio.open(f'blyaaaa/{tiff_file}', 'r+') as dst:
        # Задайте новую трансформацию и CRS
        dst.transform = new_transform
        dst.crs = CRS.from_epsg(4326)"""


# import geopandas as gpd
#
# # Загрузите ваш shapefile
# gdf = gpd.read_file("gipro/картограмма.shp")
#
# # Проверьте текущую проекцию
# print(gdf.crs)
#
# # Преобразуйте в WGS84 (EPSG:4326)
# gdf_wgs84 = gdf.to_crs("EPSG:4326")
#
# # Сохраните новый shapefile
# gdf_wgs84.to_file("eu.shp")


# shp_data = gpd.read_file('eu.shp')
# shp_data['FILENAME'] = shp_data['FILENAME'].str.replace('Z:\\2019 KYRGYZSTAN\\EXPORT FINAL\\ISSYK KUL LAKE 20CM\\', '').str.replace('TIFF ORTHO\\', '')
# print(shp_data)





"""import rasterio
from rasterio.transform import from_origin
from rasterio.crs import CRS

# Загрузка данных из файла tfw
with open('Tepke/4368_4736-RGB-20cm.tfw') as f:
    tfw_data = [float(line.strip()) for line in f]

# Создание трансформации Affine из данных tfw
transform = from_origin(tfw_data[4], tfw_data[5], tfw_data[0], -tfw_data[3])

# Чтение системы координат из файла .prj
with open('Tepke/картограмма.prj') as f:
    prj_text = f.read()
crs = CRS.from_string(prj_text)

# Обновление файла TIFF с новой CRS и трансформацией
with rasterio.open('Tepke/4368_4736-RGB-20cm.tif', 'r+') as dst:
    dst.crs = crs
    dst.transform = transform"""


"""import rasterio
from rasterio.transform import from_origin
from rasterio.crs import CRS
import os

# Установка переменной окружения PROJ_LIB
os.environ["PROJ_LIB"] = "venv/lib/python3.10/site-packages/pyproj/proj_dir/share/proj/proj.db"  # Замените на фактический путь к базе данных PROJ
# Загрузка данных из файла tfw
with open('Tepke/4368_4736-RGB-20cm.tfw') as f:
    tfw_data = [float(line.strip()) for line in f]

# Создание трансформации Affine из данных tfw
transform = from_origin(tfw_data[4], tfw_data[5], tfw_data[0], -tfw_data[3])

# Чтение системы координат из файла .prj
with open('Tepke/картограмма.prj') as f:
    prj_text = f.read()

# Обновление файла TIFF с новой CRS и трансформацией
with rasterio.open('Tepke/4368_4736-RGB-20cm.tif', 'r+') as dst:
    dst.crs = CRS.from_string(prj_text)
    print(dst.crs)
    dst.transform = transform
    # dst.crs = CRS.from_epsg(4326)"""


# import geopandas as gpd
# import pandas as pd
# import rasterio
# from rasterio.transform import from_origin
#
# # Load the shapefile data
# shp_data = gpd.read_file('eu.shp')
# shp_data['FILENAME'] = shp_data['FILENAME'].str.replace('Z:\\2019 KYRGYZSTAN\\EXPORT FINAL\\ISSYK KUL LAKE 20CM\\', '').str.replace('TIFF ORTHO\\', '')
#
# # Specify the output folder path
# output_folder = 'blyaaaa'
#
# # Iterate over the TIFF files
# for tiff_file in shp_data['FILENAME']:
#     # Get the corresponding record from the shapefile data
#     record = shp_data[shp_data['FILENAME'] == tiff_file].iloc[0]
#     pixel_width = pd.to_numeric(record['PIXEL_WIDT'].replace(' meters', ''))
#     pixel_height = pd.to_numeric(record['PIXEL_HEIG'].replace(' meters', ''))
#     new_transform = from_origin(record['UPPER_LE_X'], record['UPPER_LE_Y'], pixel_width, pixel_height)
#
#     # Open the input raster file
#     with rasterio.open(f'Tepke/{tiff_file}', 'r') as src:
#         # Check if the input raster has georeferencing information
#         if src.transform is not None:
#             # Create the output file path
#             output_file = f'{output_folder}/{tiff_file}'
#             # Create a new georeferenced TIFF file
#             with rasterio.open(output_file, 'w', driver='GTiff', width=src.width, height=src.height, count=src.count, dtype=src.dtypes[0], crs=src.crs, transform=new_transform) as dst:
#                 # Copy the data from the input raster to the output file
#                 dst.write(src.read())
#         else:
#             # Handle the case when the input raster doesn't have georeferencing information
#             print(f"The input raster file '{tiff_file}' doesn't have georeferencing information.")
#
# print(shp_data)


# from osgeo import gdal, osr
#
# # открыть исходный файл
# src_filename = 'OUTPUT.tif'
# src = gdal.Open(src_filename, gdal.GA_ReadOnly)
#
# # создать новую проекцию и установить ее
# src_srs = osr.SpatialReference()
# src_srs.ImportFromEPSG(4326)  # Замените XXXX на код EPSG исходной системы координат
# src.SetProjection(src_srs.ExportToWkt())
#
# # создать новую проекцию для выходного файла
# dst_srs = osr.SpatialReference()
# dst_srs.ImportFromEPSG(4326)  # Используем EPSG код для WGS84
#
# # преобразовать исходный файл
# dst_filename = 'OUTPUT_WGS84.tif'
# gdal.Warp(dst_filename, src, dstSRS=dst_srs)
#
# # закрыть файлы
# src = None


"""import rasterio
from rasterio.transform import from_origin

# Читаем данные из .tfw файла
with open('gipro/4368_4736-RGB-20cm.tfw') as f:
    content = f.readlines()
content = [x.strip() for x in content]

# Присваиваем значения переменным
pixel_width = float(content[0])
pixel_height = float(content[3])
xMin = float(content[4])
yMax = float(content[5])

# Открываем исходный .tif файл
with rasterio.open('gipro/4368_4736-RGB-20cm.tif') as src:
    data = src.read()

# Создаем трансформацию с использованием считанных значений
transform = from_origin(xMin, yMax, pixel_width, pixel_height)

# Создаем новый .tif файл с заданной системой координат и трансформацией
new_dataset = rasterio.open('output.tif', 'w', driver='GTiff',
                            height = data.shape[1], width = data.shape[2],
                            count=1, dtype=str(data.dtype),
                            crs='+proj=latlong',
                            transform=transform)

# Записываем данные в новый файл
new_dataset.write(data)
new_dataset.close()"""




"""from rasterio.warp import calculate_default_transform, reproject, Resampling
import rasterio
dst_crs = 'EPSG:4326' # WGS84

with rasterio.open('gipro/4368_4736-RGB-20cm.tif') as src:
    transform, width, height = calculate_default_transform(src.crs, dst_crs, src.width, src.height, *src.bounds)
    kwargs = src.meta.copy()
    kwargs.update({
        'crs': dst_crs,
        'transform': transform,
        'width': width,
        'height': height
    })

    with rasterio.open('output1.tif', 'w', **kwargs) as dst:
        for i in range(1, src.count + 1):
            reproject(
                source=rasterio.band(src, i),
                destination=rasterio.band(dst, i),
                src_transform=src.transform,
                src_crs=src.crs,
                dst_transform=transform,
                dst_crs=dst_crs,
                resampling=Resampling.nearest)"""

# import geopandas as gpd
# import pandas as pd
# import rasterio
# from rasterio.transform import from_origin
# from rasterio.crs import CRS
#
# # Загрузите данные shapefile
# # shp_data = gpd.read_file('gipro/картограмма.shp')
# shp_data = gpd.read_file('eu.shp')
# shp_data['FILENAME'] = shp_data['FILENAME'].str.replace('Z:\\2019 KYRGYZSTAN\\EXPORT FINAL\\ISSYK KUL LAKE 20CM\\', '').str.replace('TIFF ORTHO\\', '')
# print(shp_data.transform)


import geopandas as gpd
import pandas as pd
import rasterio
from rasterio.transform import from_origin
from rasterio.crs import CRS
from pyproj import Transformer

# Чтение данных из shapefile
shp_data = gpd.read_file('eu.shp')
shp_data['FILENAME'] = shp_data['FILENAME'].str.replace('Z:\\2019 KYRGYZSTAN\\EXPORT FINAL\\ISSYK KUL LAKE 20CM\\', '').str.replace('TIFF ORTHO\\', '')
print(shp_data)

# Перебор всех файлов TIFF
for _, row in shp_data.iterrows():
    tiff_file = row['FILENAME']
    # Удаление текста " meters" и преобразование ширины и высоты пикселей в числовой формат
    pixel_width = pd.to_numeric(row['PIXEL_WIDT'].replace(' meters', ''))
    pixel_height = pd.to_numeric(row['PIXEL_HEIG'].replace(' meters', ''))

    # Задание новой трансформации
    new_transform = from_origin(row['UPPER_LE_X'], row['UPPER_LE_Y'], pixel_width, pixel_height)

    # Загрузка TIFF файла
    with rasterio.open(f'blyaaaa/{tiff_file}', 'r+') as dst:
        # Создание объекта трансформера для преобразования координат
        transformer = Transformer.from_crs('EPSG:7684', 'EPSG:4326')

        # Обновление трансформации и системы координат
        dst.transform = new_transform
        dst.crs = CRS.from_epsg(4326)

        # Получение границ и преобразование в географическую систему координат
        bounds = dst.bounds
        coordinates = [
            transformer.transform(bounds.left, bounds.bottom),
            transformer.transform(bounds.right, bounds.bottom),
            transformer.transform(bounds.right, bounds.top),
            transformer.transform(bounds.left, bounds.top),
            transformer.transform(bounds.left, bounds.bottom)
        ]
        print(f"coordinates: {coordinates}")
