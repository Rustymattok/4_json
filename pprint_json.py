import json


def load_data(filepath):
    """
    Open json_file and convert it to the json_list.
    """
    try:
        with open(filepath) as f:
            json_string = f.read()
            json_list = json.loads(json_string)
    except FileNotFoundError:
        return 'not correct way for File'
    except Exception:
        return 'not correct format'
    return json_list


def pretty_print_json(json_list):
    """
    Convert json_list to readable format of json.
    """
    json_format = json.dumps(json_list, ensure_ascii=False, indent=4)
    return json_format


if __name__ == '__main__':
    filepath = input('enter file way: ')
    result = pretty_print_json(load_data(filepath))
    print(result)
