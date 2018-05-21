import json


def load_data(path):
    data = json.load(open(path, "r", encoding="utf8"))
    return data


def get_biggest_bar(data):
    bb=0
    for i in data['features']:
        if bb <= i['properties']['Attributes']['SeatsCount']:
            bb = i['properties']['Attributes']['SeatsCount']
            name_of_biggest_bar = i['properties']['Attributes']['Name']
    print("max seats bar = ", name_of_biggest_bar, " (num of seats - ", bb, ")")


def get_smallest_bar(data):
    sb=0
    for i in data['features']:
        if sb >= i['properties']['Attributes']['SeatsCount']:
            sb = i['properties']['Attributes']['SeatsCount']
            name_of_smallest_bar = i['properties']['Attributes']['Name']
    print("min seats bar = ", name_of_smallest_bar, " (num of seats - ", sb, ")")


def get_closest_bar(data, longitude, latitude):
    min_distance = 1000
    for i in data['features']:
        distance = ((float(i['geometry']['coordinates'][0]) - longitude) ** 2 +
                        (float(i['geometry']['coordinates'][1]) - latitude) ** 2) ** (1/2)
        if distance < min_distance:
            min_distance = distance
            closest_bar_name = i['properties']['Attributes']['Name']
    print("name of closest bar - ", closest_bar_name)


if __name__ == '__main__':
    p = "bars.json"
    #print(load_data(p))
    get_biggest_bar(load_data(p))
    get_smallest_bar(load_data(p))
    longitude = float (input("Insert longitude: "))
    latitude = float(input("Insert latitude: "))
    get_closest_bar(load_data(p), longitude, latitude)