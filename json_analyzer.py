""" Module to analyze JSON objects interactively """

import json
from typing import Any

# pylint: disable = unidiomatic-typecheck


class JsonAnalyzer:
    """ JsonAnalyzer class responsible for the whole interactive analyzing process """

    def __init__(self, json_filename: str = None, json_string: str = None):
        self.run = None
        self.single_obj = False
        self.whole_path = []

        if json_filename:
            with open(json_filename, 'r', encoding='utf-8') as file:
                self.json_object = json.load(file)
        elif json_string:
            self.json_object = json.loads(json_string)
        else:
            raise Exception('Error: No json_filename or json_string supplied.')

        print(f"Json object was loaded. \
It's raw length is {len(json.dumps(self.json_object))} symbols")
        print()

    @staticmethod
    def get_json_part(obj: Any, key: Any):
        """ Get part of json object """
        part = obj[key]

        return part

    def run_again(self):
        """ Check if user wants to continue program running or stop the program """
        if self.run is False:
            return False

        print()
        print('If you want to go level back press enter')
        print('To stop the program enter "stop"')
        run = input('>>> ')
        print()
        if 'stop' in run:
            self.run = False
            return False

        self.run = True
        return True

    def print_full_path(self, obj):
        """ Prints full path to certain object """
        whole_path_str = ''.join([f'[{i}]' for i in self.whole_path])
        print(f'The type of this object is {type(obj)}\
{f", reference path to object: obj_initial{whole_path_str}" if whole_path_str else ""}')

    def objects_manager(self, object_name: str, obj: Any):
        """ Get json part interactively for big objects """
        while True:
            if self.run is False:
                break

            self.print_full_path(obj)

            if type(obj) is dict:
                keys_list = obj.keys()
            else:
                keys_list = [str(i) for i in range(len(obj))]
                print(f'Length of this {type(obj)} is {len(obj)}')

            if len(keys_list) == 0:
                self.whole_path.pop()
                print()
                print('Empty object, going back 1 level.')
                print()
                break

            print(f'Available keys: {keys_list}')

            while True:
                print()
                print('Please input the key you want to open:')
                keys_obj = list(keys_list)
                if object_name != 'initial_object':
                    print('If you want to go level back press enter')
                    keys_obj += ['']
                key = input('>>> ')
                print()
                if key in keys_obj:
                    break
                print('Error! Bad key provided. Please check spelling of a key')

            if key == '':
                self.whole_path.pop()
                break

            key_parsed = key
            if type(obj) is not dict:
                key_parsed = int(key_parsed)

            self.whole_path.append(key_parsed)
            self.iterative_get_json_part(key_parsed, self.get_json_part(obj, key_parsed))

            if self.single_obj:
                self.whole_path.pop()
                self.single_obj = False
                if not self.run_again():
                    break

    def iterative_get_json_part(self, object_name: str = 'initial_object',
                                obj: Any = None):
        """ Get json part interactively """

        if type(obj) in (dict, list, set, tuple):
            self.objects_manager(object_name, obj)
        else:
            self.print_full_path(obj)
            print('Single object reached. Here it is: ')
            print(f'>>>>> {obj} <<<<<')
            self.single_obj = True

    def main(self):
        """ Main function of class. Run interactive json analyzing """
        self.iterative_get_json_part(obj=self.json_object)
