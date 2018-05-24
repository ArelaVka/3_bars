import json


def is_number(input_data):
    try:
        float(input_data)
        return float(input_data)
    except ValueError:
        return False


def is_json(input_data):
    try:
        json.load(open(input_data, "r", encoding="utf8"))
        return True
    except ValueError:
        return False


def load_data(file_path):
    with open(file_path, "r", encoding="utf8") as json_file:
        all_bars_data = json.load(json_file)
    return all_bars_data["features"]


def get_biggest_bar(input_data):
    biggest_bar_data = max(input_data,
                           key=lambda x:
                           x["properties"]["Attributes"]["SeatsCount"])
    return biggest_bar_data


def get_smallest_bar(input_data):
    smallest_bar_data = min(input_data,
                            key=lambda x:
                            x["properties"]["Attributes"]["SeatsCount"])
    return smallest_bar_data


def get_closest_bar(input_data, longitude, latitude):
    closest_bar_data = min(input_data,
                           key=lambda x:
                           ((float(x["geometry"]["coordinates"][0]) -
                             (longitude)) ** 2 +
                            (float(x["geometry"]["coordinates"][1]) -
                             (latitude)) ** 2) ** (1 / 2))
    return closest_bar_data


if __name__ == "__main__":
    path_to_file = "bars.json"
    if is_json(path_to_file):
        print("The biggest bar is ",
              get_biggest_bar(load_data(path_to_file))
              ["properties"]["Attributes"]["Name"])
        print("The smallest bar is ",
              get_smallest_bar(load_data(path_to_file))
              ["properties"]["Attributes"]["Name"])
        current_x_coord = is_number(input("Insert longitude: "))
        current_y_coord = is_number(input("Insert latitude: "))
        if is_number(current_x_coord) and is_number(current_y_coord):
            print("The closest bar is ",
                  get_closest_bar(load_data(path_to_file),
                                  current_x_coord, current_y_coord)
                  ["properties"]["Attributes"]["Name"])
        else:
            exit("you must enter numbers!")
    else:
        print("Your input file is incorrect")
