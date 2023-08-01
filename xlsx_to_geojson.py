# import geopandas as gpd
# import pandas as pd
#
# # Чтение файла Excel
# df = pd.read_excel('YsykAta.xlsx')
# print(df.columns.tolist())
# # Извлечение столбца с координатами x и y
# values_1 = df['Unnamed: 1'].tolist()[2:]
# values_2 = df['Unnamed: 2'].tolist()[2:]
# values_3 = df['Unnamed: 3'].tolist()[2:]
# values_4 = df['Unnamed: 4'].tolist()[2:]
# values_5 = df['Unnamed: 5'].tolist()[2:]
# values_6 = df['Unnamed: 6'].tolist()[2:]
#
# print(values_1)
# print(values_2)
# print(values_3)
# print(values_4)
# print(values_5)
# print(values_6)
#
# # # Создание геометрии точек
# # geometry = gpd.points_from_xy(x_values, y_values)
# #
# # # Создание GeoDataFrame
# # gdf = gpd.GeoDataFrame(df, geometry=geometry)
# #
# # # Сохранение в GeoJSON
# # gdf.to_file('YsykAta.geojson', driver='GeoJSON')


"""import pandas as pd
import geopandas as gpd
from shapely.geometry import Polygon

df = pd.read_excel('YsykAta.xlsx')
df = df.drop(df[df['Unnamed: 0'] == 'район'].index)
df = df.dropna(how='all')

# Преобразование координат в числа
df[['Latitude1', 'Longitude1']] = df['Unnamed: 1'].str.split(', ', expand=True).astype(float)
df[['Latitude2', 'Longitude2']] = df['Unnamed: 2'].str.split(', ', expand=True).astype(float)
df[['Latitude3', 'Longitude3']] = df['Unnamed: 3'].str.split(', ', expand=True).astype(float)
df[['Latitude4', 'Longitude4']] = df['Unnamed: 4'].str.split(', ', expand=True).astype(float)
df[['Latitude5', 'Longitude5']] = df['Unnamed: 5'].str.split(', ', expand=True).astype(float)
df[['Latitude6', 'Longitude6']] = df['Unnamed: 6'].str.split(', ', expand=True).astype(float)

# Создание полигонов
geometry = []
for index, row in df.iterrows():
    vertices = [
        (row['Longitude1'], row['Latitude1']),
        (row['Longitude2'], row['Latitude2']),
        (row['Longitude3'], row['Latitude3']),
        (row['Longitude4'], row['Latitude4']),
        (row['Longitude5'], row['Latitude5']),
        (row['Longitude6'], row['Latitude6'])
    ]
    polygon = Polygon(vertices)
    geometry.append(polygon)

# Создание GeoDataFrame с выбранными столбцами и полигонами
properties = ['Unnamed: 0', 'Unnamed: 7', 'Unnamed: 8', 'Unnamed: 9', 'Unnamed: 10']
gdf = gpd.GeoDataFrame(df[properties], geometry=geometry)

# Сохранение в GeoJSON
gdf.to_file('YsykAta1.geojson', driver='GeoJSON')"""


"""import pandas as pd
import geopandas as gpd
from shapely.geometry import Polygon

df = pd.read_excel('YsykAta.xlsx')
df = df.drop(df[df['Unnamed: 0'] == 'район'].index)
df = df.dropna(how='all')

# Преобразование координат в числа и создание полигонов
geometry = []
for index, row in df.iterrows():
    vertices = []
    for i in range(1, 7):
        coord = row[f'Unnamed: {i}']
        if isinstance(coord, str) and ', ' in coord:
            lat, lon = coord.split(', ')
            vertices.append((float(lon), float(lat)))
    if len(vertices) >= 3:
        polygon = Polygon(vertices)
        geometry.append(polygon)

# Создание GeoDataFrame с выбранными столбцами и полигонами
properties = ['Unnamed: 0', 'Unnamed: 7', 'Unnamed: 8', 'Unnamed: 9', 'Unnamed: 10']
gdf = gpd.GeoDataFrame(df[properties], geometry=geometry)

# Сохранение в GeoJSON
gdf.to_file('YsykAta.geojson', driver='GeoJSON')"""


# import pandas as pd
# import geopandas as gpd
# from shapely.geometry import Point
#
# df = pd.read_excel('YsykAta.xlsx')
# df = df.drop(df[df['Unnamed: 0'] == 'район'].index)
# df = df.dropna(how='all')
#
# # Преобразование координат в числа
# df[['Latitude', 'Longitude']] = df['Unnamed: 1'].str.split(', ', expand=True).astype(float)
#
# # Создание геометрии точек
# geometry = [Point(xy) for xy in zip(df['Longitude'], df['Latitude'])]
#
# # Создание GeoDataFrame с выбранными столбцами в качестве свойств
# properties = ['Unnamed: 0', 'Unnamed: 7', 'Unnamed: 8', 'Unnamed: 9', 'Unnamed: 10']
# gdf = gpd.GeoDataFrame(df[properties], geometry=geometry)
#
# # Сохранение в GeoJSON
# gdf.to_file('YsykAta.geojson', driver='GeoJSON')



### Ysyk-Ata
"""import pandas as pd
import geopandas as gpd
from shapely.geometry import Polygon

df = pd.read_excel('YsykAta.xlsx')
df = df.drop(df[df['Unnamed: 0'] == 'район'].index)
df = df.dropna(how='all')

# Преобразование координат в числа и создание полигонов
geometry = []
for index, row in df.iterrows():
    vertices = []
    for i in range(1, 7):
        coord = row[f'Unnamed: {i}']
        if isinstance(coord, str) and ', ' in coord:
            lat, lon = coord.split(', ')
            vertices.append((float(lon), float(lat)))
    if isinstance(row['Unnamed: 1'], str) and ', ' in row['Unnamed: 1']:
        lat, lon = row['Unnamed: 1'].split(', ')
        vertices.append((float(lon), float(lat)))
    if len(vertices) >= 3:
        polygon = Polygon(vertices)
        geometry.append(polygon)

# Создание GeoDataFrame с выбранными столбцами и полигонами
properties = ['Unnamed: 0', 'Unnamed: 7', 'Unnamed: 8', 'Unnamed: 9', 'Unnamed: 10']
gdf = gpd.GeoDataFrame(df[properties], geometry=geometry)

# Сохранение в GeoJSON
gdf.to_file('YsykAta2.geojson', driver='GeoJSON')"""



import pandas as pd
import geopandas as gpd
from shapely.geometry import Polygon

df = pd.read_excel('panfilov.xlsx')
df = df.iloc[1:]  # Удаление первой строки

# Проверка наличия столбца 'Unnamed: 7' и его добавление
if 'Unnamed: 7' not in df.columns:
    df['Unnamed: 7'] = None

# Преобразование координат в числа и создание полигонов
geometry = []
for index, row in df.iterrows():
    vertices = []
    for i in range(1, len(row), 2):
        if pd.notnull(row[i]) and pd.notnull(row[i + 1]):
            try:
                lat = float(row[i + 1])
                lon = float(row[i])
                vertices.append((lon, lat))
            except ValueError:
                continue
    if len(vertices) >= 3:
        polygon = Polygon(vertices)
        geometry.append(polygon)

# Создание GeoDataFrame с выбранными столбцами и полигонами
properties = ['район', '1 точка', 'Unnamed: 3', '2 точка', 'Unnamed: 5', '3 точка', 'Unnamed: 7', 'вид культуры']
gdf = gpd.GeoDataFrame(df[properties], geometry=geometry)

# Сохранение в GeoJSON
gdf.to_file('Panfilov.geojson', driver='GeoJSON')



