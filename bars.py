import json


def is_number(input_data):
    try:
        float(input_data)
        return True
    except ValueError:
        return False


def is_json(input_data):
    try:
        json.load(open(input_data, "r", encoding="utf8"))
        return True
    except ValueError:
        return False


def load_data(file_path):
    with open(file_path, "r", encoding="utf8") as f:
        all_bars_data = json.load(f)
    return all_bars_data


def get_biggest_bar(input_data):
    biggest_bar_seats = max(input_data["features"], key=lambda x: x["properties"]["Attributes"]["SeatsCount"])
    return biggest_bar_seats["properties"]["Attributes"]["Name"]


def get_smallest_bar(input_data):
    smallest_bar_seats = min(input_data["features"], key=lambda x: x["properties"]["Attributes"]["SeatsCount"])
    return smallest_bar_seats["properties"]["Attributes"]["Name"]


def get_closest_bar(input_data, longitude, latitude):
    min_distance = 1000
    for current_record in input_data["features"]:
        distance = ((float(current_record["geometry"]["coordinates"][0]) - longitude) ** 2 +
                    (float(current_record["geometry"]["coordinates"][1]) - latitude) ** 2) ** (1 / 2)
        if distance < min_distance:
            min_distance = distance
            closest_bar_name = current_record["properties"]["Attributes"]["Name"]
    return closest_bar_name


if __name__ == "__main__":
    path_to_file = "bars.json"
    if is_json(path_to_file):
        print("The biggest bar is ", get_biggest_bar(load_data(path_to_file)))
        print("The smallest bar is ", get_smallest_bar(load_data(path_to_file)))
        current_x_coord = input("Insert longitude: ")
        while not is_number(current_x_coord):
            current_x_coord = input("Please insert correct longitude: ")
        else:
            current_y_coord = input("Insert latitude: ")
            while not is_number(current_y_coord):
                current_y_coord = input("Please insert correct latitude: ")
            else:
                print("The closest bar is ", get_closest_bar(load_data(path_to_file), float(current_x_coord),
                                                             float(current_y_coord)))
    else:
        print("Your input file is incorrect")