#!/usr/bin/env python3

import xmltodict
import json
from argparse import ArgumentParser, Namespace


def parse_args() -> Namespace:
    try:
        parser = ArgumentParser()
        parser.add_argument('xmlfile',
                            type=str,
                            help="Path to the XML formatted Nmap output file.")
        parser.add_argument('--json-output-file',
                            dest='json_file',
                            default='scan.json',
                            type=str,
                            help="Path to the saved JSON file. "
                                 "Default: scan.json")
        return parser.parse_args()
    except Exception as e:
        print("Error in parse_args", e)


def parse_xml_content(filename) -> dict:
    try:
        with open(filename, 'r') as f:
            content = f.read()
        return xmltodict.parse(content)
    except Exception as e:
        print("Error in parse_xml_content", e)


def convert_to_json(data) -> str:
    try:
        result = json.dumps(data, indent=4, sort_keys=True)
        return result
    except Exception as e:
        print("Error in convert_to_json", e)


def write_json_file(data, output_filename) -> None:
    try:
        with open(output_filename, 'w') as f:
            f.write(data)
        return None
    except Exception as e:
        print("Error in write_json_file", e)


if __name__ == "__main__":
    args = parse_args()

    xml_data = parse_xml_content(args.xmlfile)
    json_data = convert_to_json(xml_data)
    write_json_file(json_data, args.json_file)

    print(f"Complete! JSON output saved to {args.json_file}")
