import json


def load_data(path):
    data = json.load(open(path, "r", encoding="utf8"))
    return data

def get_biggest_bar(data):
    pass


def get_smallest_bar(data):
    pass


def get_closest_bar(data, longitude, latitude):
    pass


if __name__ == '__main__':
    p = "bars.json"
    print(load_data(p))
