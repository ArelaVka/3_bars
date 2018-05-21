import json


def load_data(file_path):
    all_bars_data = json.load(open(file_path, "r", encoding="utf8"))
    return all_bars_data


def get_biggest_bar(input_data):
    biggest_bar_seats = max(input_data['features'], key=lambda x: x['properties']['Attributes']['SeatsCount'])
    print("max seats bar = ", biggest_bar_seats['properties']['Attributes']['Name'], " (num of seats - ",
          biggest_bar_seats['properties']['Attributes']['SeatsCount'], ")")


def get_smallest_bar(input_data):
    smallest_bar_seats = min(input_data['features'], key=lambda x: x['properties']['Attributes']['SeatsCount'])
    print("min seats bar = ", smallest_bar_seats['properties']['Attributes']['Name'], " (num of seats - ",
          smallest_bar_seats['properties']['Attributes']['SeatsCount'], ")")


def get_closest_bar(input_data, longitude, latitude):
    min_distance = 1000
    for current_record in input_data['features']:
        distance = ((float(current_record['geometry']['coordinates'][0]) - longitude) ** 2 +
                    (float(current_record['geometry']['coordinates'][1]) - latitude) ** 2) ** (1 / 2)
        if distance < min_distance:
            min_distance = distance
            closest_bar_name = current_record['properties']['Attributes']['Name']
    print("name of closest bar - ", closest_bar_name)


if __name__ == '__main__':
    path_to_file = "bars.json"
    get_biggest_bar(load_data(path_to_file))
    get_smallest_bar(load_data(path_to_file))
    current_x_coord = float(input("Insert longitude: "))
    current_y_coord = float(input("Insert latitude: "))
    get_closest_bar(load_data(path_to_file), current_x_coord, current_y_coord)
