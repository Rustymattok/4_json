import json
import argparse
import os


def load_data(file_path):
    if not os.path.exists(file_path):
        return None
    with open(file_path, 'r') as file_handler:
        json_code = json.load(file_handler)
        return json_code


def pretty_print_json(json_code):
    json_readable_user = json.dumps(json_code, ensure_ascii=False, indent=4)
    return json_readable_user


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', type=str, help="command - input file")
    return parser


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()
    if args.file is None:
        print("no Data for work")
    else:
        try:
            print(pretty_print_json(load_data(args.file)))
        except ValueError:
            print("not correct format")
