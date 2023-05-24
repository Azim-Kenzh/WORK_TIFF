import os

from osgeo import gdal

input_file = '../cut_tif_geojson/Result_GEOJSON/BATKEN_TCI_GEOJSON.tif'
output_file = 'RESULT_BATKEN_TCI_PX'
os.makedirs(output_file, exist_ok=True)

# Открываем входной файл с помощью GDAL
ds = gdal.Open(input_file)
if ds is not None:
    band = ds.GetRasterBand(1)
    xsize = band.XSize
    ysize = band.YSize

    out_path = output_file
    output_filename = 'KG_'
    num = 1  # Переменная для хранения номера файла

    tile_size_x = 640
    tile_size_y = 640

    # Обрезаем изображение сначала так, чтобы содержать первые верхние тайлы 320px
    for i in range(0, xsize, tile_size_x):
        for j in range(0, ysize, tile_size_y):

            output_file = os.path.join(out_path, output_filename + str(num) + "_CENTER.tif")
            num += 1  # Увеличиваем номер файла

            # Обрезаем изображение
            dst = gdal.Translate(output_file, ds, srcWin=[i, j, tile_size_x, tile_size_y])

    # Освобождаем ресурсы
    ds = None
    dst = None
else:
    print(f"Не удалось открыть файл: Bishkek.tif")