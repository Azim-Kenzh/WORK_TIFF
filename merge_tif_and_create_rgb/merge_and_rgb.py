import os
import glob
import time
from collections import defaultdict

import cv2
import numpy as np
import rasterio


"""Объеденение всех каналов в одну файл"""
# Определение пути к файлам
path = '../convert_jp2_to_tif/KR_BANDS_tif'
output_merge = 'Merge_Result'
os.makedirs(output_merge, exist_ok=True)

# Получение списка файлов
file_list = glob.glob(os.path.join(path, '*.tif'))

# Словарь для группировки файлов по тайлам и дате съемки
file_dict = defaultdict(list)

# Группировка файлов
for file in file_list:
    # извлечение названия файла без расширения
    basename = os.path.basename(file).split('.')[0]

    # извлечение идентификатора тайла и даты съемки
    tile_id, date_time, band, _ = basename.split('_')

    # группировка файлов
    file_dict[f"{tile_id}_{date_time}"].append((band, file))

# Установка порядка объединения
bands_order = ['B02', 'B03', 'B04']

# Объединение файлов
for key, files in file_dict.items():
    # сортировка файлов в соответствии с порядком bands_order
    files.sort(key=lambda x: bands_order.index(x[0]))

    # Открытие первого файла из списка для получения метаданных
    with rasterio.open(files[0][1]) as src:
        meta = src.meta
        meta.update(count=len(files))  # Установка количества каналов в метаданных
        meta.update(driver="GTiff")  # Установка типа драйвера в метаданных

    # Создание выходного файла с помощью метаданных и запись в него данных из всех файлов
    output_file = f"{output_merge}/{key}.tif"
    with rasterio.open(output_file, "w", **meta) as dst:
        for id, layer in enumerate(files, start=1):
            with rasterio.open(layer[1]) as src:
                dst.write(src.read(1), id)


time.sleep(10)
"""Преобразование в RGB"""
merge_bands_list = os.listdir(output_merge)
output_rgb = 'RESULT_RGB'
os.makedirs(output_rgb, exist_ok=True)
for band_rgb in merge_bands_list:
    # Открываем входной файл с помощью Rasterio
    with rasterio.open(f'{output_merge}/{band_rgb}') as src:
        # Читаем каналы красного, зеленого и синего цветов
        red = src.read(3)
        green = src.read(2)
        blue = src.read(1)

        # Масштабируем значения пикселей до диапазона от 0 до 255
        red = np.interp(red, (red.min(), red.max()), (0, 255)).astype('uint8')
        green = np.interp(green, (green.min(), green.max()), (0, 255)).astype('uint8')
        blue = np.interp(blue, (blue.min(), blue.max()), (0, 255)).astype('uint8')

        # Изменяем яркость и насыщенность каждого канала
        brightness = 50
        saturation = 1.5

        red = cv2.convertScaleAbs(red, alpha=1, beta=brightness)
        red = cv2.convertScaleAbs(red, alpha=saturation)

        green = cv2.convertScaleAbs(green, alpha=1, beta=brightness)
        green = cv2.convertScaleAbs(green, alpha=saturation)

        blue = cv2.convertScaleAbs(blue, alpha=1, beta=brightness)
        blue = cv2.convertScaleAbs(blue, alpha=saturation)

        # Создаем RGB изображение, объединив каналы в одно изображение
        rgb = np.dstack((red, green, blue))

        # Получаем метаданные из исходного файла и обновляем количество каналов и тип данных
        meta = src.meta.copy()
        meta.update(count=3, dtype='uint8')

        # Записываем RGB изображение в новый файл в формате GeoTIFF
        with rasterio.open(f"{output_rgb}/RGB_{band_rgb}", 'w', **meta) as dst:
            dst.write(rgb.transpose(2, 0, 1))