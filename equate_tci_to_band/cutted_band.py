from osgeo import gdal

band_file = '../cut_tif_geojson/Result_GEOJSON_BANDS/OSH_BAND_GEOJSON.tif'
tci_file = '../cut_tif_geojson/Result_GEOJSON/OSH_TCI_GEOJSON.tif'
output_file = 'resized_band.tif'  # Выходной файл с приведенным размером TCI

# Открываем файлы с помощью GDAL
band_ds = gdal.Open(band_file)
tci_ds = gdal.Open(tci_file)

if band_ds is not None and tci_ds is not None:
    band_width = band_ds.RasterXSize
    band_height = band_ds.RasterYSize
    tci_width = tci_ds.RasterXSize
    tci_height = tci_ds.RasterYSize

    # Находим минимальные размеры изображений
    min_width = min(band_width, tci_width)
    min_height = min(band_height, tci_height)

    # Изменяем размеры изображений
    resized_band = gdal.Translate(output_file, band_ds, width=min_width, height=min_height)
    resized_tci = gdal.Translate(output_file, tci_ds, width=min_width, height=min_height)

    # Освобождаем ресурсы
    band_ds = None
    tci_ds = None
    resized_band = None
    resized_tci = None

    print("Изображения успешно приведены к одинаковым размерам")
else:
    print("Не удалось открыть один или оба файла")

