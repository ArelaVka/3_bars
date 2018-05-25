import json


def is_number(input_data):
    try:
        float_input_data = float(input_data)
        return float_input_data
    except ValueError:
        return False


def open_json(path_to_file):
    try:
        with open(path_to_file, "r", encoding="utf8") as opened_file:
            json_data = json.load(opened_file)
        return json_data["features"]
    except ValueError:
        return False


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
        key=lambda x: ((float(x["geometry"]["coordinates"][0]) -
                        (longitude))**2 +
                       (float(x["geometry"]["coordinates"][1]) -
                        (latitude))**2)**(1/2))
    return closest_bar_data


'''
Комментарий про сделать if короче не понял.
Как ни крути, содержимое if не изменится в объемах.
Можно немного подробнее описать рекомендации.
'''

if __name__ == "__main__":
    input_path = input("Enter path: ")
    if open_json(input_path):
        print(
            "The biggest bar is ",
            get_biggest_bar(open_json(input_path))
            ["properties"]["Attributes"]["Name"])
        print("The smallest bar is ",
              get_smallest_bar(open_json(input_path))
              ["properties"]["Attributes"]["Name"])
        current_x_coord = is_number(input("Insert longitude: "))
        current_y_coord = is_number(input("Insert latitude: "))
        if is_number(current_x_coord) and is_number(current_y_coord):
            print("The closest bar is ",
                  get_closest_bar(open_json(input_path),
                                  current_x_coord,
                                  current_y_coord)
                  ["properties"]["Attributes"]["Name"])
        else:
            exit("you must enter numbers!")
    else:
        print("Your input file or path is incorrect")
