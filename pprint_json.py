import json
import argparse
import os


def load_data(file_path):
    if not os.path.exists(file_path):
        return None
    with open(file_path, 'r') as file_handler:
        decoded_data = json.load(file_handler)
        return decoded_data


def pretty_print_json(decoded_data):
    encoded_data = json.dumps(decoded_data, ensure_ascii=False, indent=4)
    return encoded_data


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file',
                        required=True,
                        help="command - input file")
    return parser


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()
    try:
        print(pretty_print_json(load_data(args.file)))
    except ValueError:
        print("not correct format")
