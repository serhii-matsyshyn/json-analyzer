""" Main module used to create map with the 10 nearest films locations in certain year
by provided console input
"""

# pylint: disable = import-error  # To disable import-error warning

import argparse
from typing import Callable
from logging import INFO, getLogger

from json_analyzer import JsonAnalyzer

getLogger().setLevel(INFO)


def parse_args() -> argparse.Namespace:
    """ Parses args using argparse
    python main.py --json-filename "example.json"
    python main.py --json-string '{\"user\":{\"id\":1070,\"id_str\":\"1070\"}}'
    """
    parser = argparse.ArgumentParser(
        description='''This module helps you analyze JSON objects interactively
        if you don't know their structure and want to determine
        the correct path to certain data.  '''
    )

    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument(
        '--json-filename',
        type=str,
        help='''Path to json file'''
    )
    group.add_argument(
        '--json-string',
        type=str,
        help='''Json string'''
    )
    return parser.parse_args()


def exception_handler(function: Callable,
                      args: argparse.Namespace):
    """ Function to catch unexpected exceptions """
    try:
        function(args)
    except (Exception,) as err:  # pylint: disable=broad-except
        # Catches all errors that were not caught by previous checks.
        print("Error: Unexpected exception occurred.")
        print(f"Detailed error: {err}")


def main_function(args: argparse.Namespace):
    """ Analyze by JsonAnalyzer by provided argparse.Namespace """
    JsonAnalyzer(json_filename=args.json_filename,
                 json_string=args.json_string).main()


def main():
    """ Main function of the program """
    args = parse_args()
    exception_handler(main_function, args)


if __name__ == '__main__':
    main()
