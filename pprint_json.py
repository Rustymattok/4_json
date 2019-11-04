import json

# 'This method load json and convert it to dictionary String format.  '


def load_data(filepath):
    file_json = open(filepath)
    alcoshops_list = json.load(file_json)
    return alcoshops_list

# 'This method return string in valid json format with good visibility.  '


def pretty_print_json(alcoshops_list):
    json_shops = json.dumps(alcoshops_list, ensure_ascii=False, indent=4)
    return json_shops


if __name__ == '__main__':
    print(pretty_print_json(load_data("./data_file.json")))
