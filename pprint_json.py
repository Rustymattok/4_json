import json
import sys
import argparse


def load_data(data_file):
    """ Take data of file and convert it to json ."""
    convert_json = json.loads(data_file)
    return convert_json


def pretty_print_json(json_list):
    """ Make current json more structure from view ."""
    json_visual = json.dumps(json_list, ensure_ascii=False, indent=4)
    return json_visual


def create_parser():
    """ Prepare commands in console ."""
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command')
    input_parser = subparsers.add_parser('input',
                                         help="for input file")
    input_parser.add_argument('-i',  help="command for input file")
    input_parser.add_argument("file", type=argparse.FileType(),
                              help="the file for convert")
    run_parser = subparsers.add_parser('run', help="for test file")
    run_parser.add_argument("-r", type=argparse.FileType(),
                            default='test.json',
                            help="command for base file")
    return parser


if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])
    if namespace.command == "input":
        try:
            answer = namespace.file.read()
            print(answer)
            print(pretty_print_json(load_data(answer)))
        except ValueError:
            print("error syntax of file")
            sys.exit()
    elif namespace.command == "run":
        with open('test.json') as f:
            json_string = f.read()
            answer = json.loads(json_string)
        print(pretty_print_json(answer))
    else:
        print("smth wrong")
