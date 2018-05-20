import json


def load_data(path):
    with open(path, "r") as f:
        data = json.loads(f.read())
    return data


def get_biggest_bar(data):
    pass


def get_smallest_bar(data):
    pass


def get_closest_bar(data, longitude, latitude):
    pass


if __name__ == '__main__':
    p = "bars.json"
    data = load_data(p)
