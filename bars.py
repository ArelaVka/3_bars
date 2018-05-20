import json


def load_data(path):
    data = json.load(open(path, "r", encoding="utf8"))
    return data


def get_biggest_bar(data):
    for i in data['features']:
        print(i['properties']['Attributes']['SeatsCount'])


def get_smallest_bar(data):
    pass


def get_closest_bar(data, longitude, latitude):
    pass


if __name__ == '__main__':
    p = "bars.json"
    print(load_data(p))
    get_biggest_bar(load_data(p))
