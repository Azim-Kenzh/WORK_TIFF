# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/


import re
import json

def parse_sql_to_json(file_path):
    with open(file_path, 'r') as sql_file:
        sql_content = sql_file.read()

    # Используем регулярные выражения для поиска данных в файле .sql
    # Предполагается, что данные находятся в формате INSERT INTO и указаны в VALUES
    # В зависимости от структуры вашего .sql файла, возможно, потребуется настроить регулярное выражение
    pattern = r"INSERT INTO .+? VALUES \((.+?)\);"
    matches = re.findall(pattern, sql_content, re.DOTALL)

    data = []
    for match in matches:
        # Разбиваем строку на значения, предполагая, что они разделены запятой
        values = match.split(',')

        # Очищаем каждое значение от лишних пробелов и кавычек
        cleaned_values = [value.strip().strip("'") for value in values]

        data.append(cleaned_values)

    # Преобразуем данные в формат JSON и сохраняем в новый файл
    with open('output.json', 'w') as json_file:
        json.dump(data, json_file, indent=2)

if __name__ == "__main__":
    sql_file_path = "calpasia1_fund.sql"
    parse_sql_to_json(sql_file_path)
