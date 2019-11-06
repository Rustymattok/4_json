import json


def load_data(filepath):
    try:
        if filepath[-5:len(filepath)] != '.json':  # for format .json
            return 'not correct format'
        with open(filepath) as f:
            json_string = f.read()
            json_list = json.loads(json_string)
    except FileNotFoundError:
        return 'not correct way for File'
    return json_list


def pretty_print_json(json_list):
    json_visual = json.dumps(json_list, ensure_ascii=False, indent=4)
    return json_visual  # convert json_list to more readable format in console.


if __name__ == '__main__':
    filepath = input('enter file way: ')
    json_visual = pretty_print_json(load_data(filepath))
    print(json_visual)
