import os
from osgeo import gdal
import glob

# Путь к папке с файлами JP2
jp2_folder = "../KR_BANDS_TCL_jp2"

# Создание папки для сохранения файлов TIF
tif_folder = "KR_BANDS_tif"
os.makedirs(tif_folder, exist_ok=True)

# Получаем список файлов JP2 в папке
jp2_files = glob.glob(os.path.join(jp2_folder, "*.jp2"))

# Цикл по файлам JP2
for jp2_file in jp2_files:
    # Открываем JP2 файл
    dataset = gdal.Open(jp2_file)

    # Извлекаем имя файла без расширения
    file_name = os.path.splitext(os.path.basename(jp2_file))[0]

    # Путь и имя файла TIF
    tif_file = os.path.join(tif_folder, file_name + ".tif")

    # Сохраняем JP2 как TIF
    gdal.Translate(tif_file, dataset, format="GTiff")

    # Закрываем датасет
    dataset = None
