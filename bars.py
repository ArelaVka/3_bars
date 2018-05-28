import json
import sys
import os


def get_number(input_coord):
    try:
        float_input_coord = float(input_coord)
        return float_input_coord
    except ValueError:
        return None


def load_json_data(path_to_file):
    try:
        with open(path_to_file, "r", encoding="utf8") as opened_file:
            json_data = json.load(opened_file)
        return json_data["features"]
    except ValueError:
        return None


def get_biggest_bar(bars):
    biggest_bar_data = max(
        bars,
        key=lambda x: x["properties"]["Attributes"]["SeatsCount"])
    return biggest_bar_data


def get_smallest_bar(bars):
    smallest_bar_data = min(
        bars,
        key=lambda x: x["properties"]["Attributes"]["SeatsCount"])
    return smallest_bar_data


def get_closest_bar(bars, longitude, latitude):
    closest_bar_data = min(
        bars,
        key=lambda x: (
            (float(x["geometry"]["coordinates"][0]) - (longitude))**2 +
            (float(x["geometry"]["coordinates"][1]) - (latitude))**2)**(1/2))
    return closest_bar_data


def get_bar_name(bar_data):
    return bar_data["properties"]["Attributes"]["Name"]


if __name__ == "__main__":
    if len(sys.argv) > 1 and os.path.exists(sys.argv[1]):
        input_data = load_json_data(sys.argv[1])
    else:
        sys.exit("Your path is incorrect")
    if input_data:
        print("The biggest bar is ", get_bar_name(get_biggest_bar(input_data)))
        print("The smallest bar is ",
              get_bar_name(get_smallest_bar(input_data)))
        current_x_coord = get_number(input("Insert longitude: "))
        current_y_coord = get_number(input("Insert latitude: "))
        if current_x_coord and current_y_coord:
            print("The closest bar is ", get_bar_name(
                get_closest_bar(input_data, current_x_coord, current_y_coord)))
        else:
            sys.exit("You must enter numbers!")
    else:
        sys.exit("Your input file is not correct json")
