from osgeo import gdal

band_file = '../cut_tif_geojson/Result_GEOJSON_BANDS/NARYN_BAND_GEOJSON.tif'
tci_file = '../cut_tif_geojson/Result_GEOJSON/NARYN_TCI_GEOJSON.tif'

# Открываем файлы с помощью GDAL
band_ds = gdal.Open(band_file)
tci_ds = gdal.Open(tci_file)

if band_ds is not None and tci_ds is not None:
    band_width = band_ds.RasterXSize
    band_height = band_ds.RasterYSize
    tci_width = tci_ds.RasterXSize
    tci_height = tci_ds.RasterYSize

    print(f"Размеры band.tif: Width={band_width}, Height={band_height}")
    print(f"Размеры tci.tif: Width={tci_width}, Height={tci_height}")

    # Освобождаем ресурсы
    band_ds = None
    tci_ds = None
else:
    print("Не удалось открыть один или оба файла")
