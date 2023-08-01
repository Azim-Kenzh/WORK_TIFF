import json

with open('ai_contour.json', 'r') as f:
    a = json.load(f)
    print(len([i for i in a if i['fields']['district'] in [2, 3, 5, 6, 8, 7, 14, 15, 16, 17, 18, 19, 20, 21]]))
    # for i in a:
        # district = i['district']
        # print(district)
        # if i['fields']['district'] in [2, 3, 5, 6, 8, 7, 14, 15, 16, 17, 18, 19, 20, 21]:
        #     print(i['fields']['polygon'])
