import json
from typing import Any


class JsonAnalyzer:
    def __init__(self, json_filename: str = None, json_string: str = None):
        self.run = None
        self.single_obj = False

        if json_filename:
            with open(json_filename, 'r', encoding='utf-8') as file:
                self.json_object = json.load(file)
        elif json_string:
            self.json_object = json.loads(json_string)
        else:
            raise Exception('Error: No json_filename or json_string supplied.')

        print(f"Json object was loaded. It's raw length is {len(json.dumps(self.json_object))} symbols")
        print()

    def get_json_part(self, obj: Any, key: Any):
        part = obj[key]

        return part

    def run_again(self):
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
        else:
            self.run = True
            return True

    def iterative_get_json_part(self, object_name='initial_object', obj=None):
        print(f'The type of this object is {type(obj)}')
        if type(obj) in (dict, list, set, tuple):
            while True:
                if type(obj) is dict:
                    keys = obj.keys()
                    print(f'Available keys: {keys}')
                else:
                    keys = [str(i) for i in range(len(obj))]
                    print(f'Length of this {type(obj)} is {len(obj)}')

                if len(keys) == 0:
                    print('Empty object.')

                while True:
                    print()
                    print('Please input the key you want to open:')
                    keys_obj = list(keys)
                    if object_name!='initial_object':
                        print('If you want to go level back press enter')
                        keys_obj += ['']
                    key = input('>>> ')
                    if key in keys_obj:
                        break
                    print('Error! Bad key provided. Please check spelling of a key')

                if key == '':
                    break

                print(f'Opening {object_name}["{key}"]')
                if type(obj) is not dict:
                    self.iterative_get_json_part(key, self.get_json_part(obj, int(key)))
                else:
                    self.iterative_get_json_part(key, self.get_json_part(obj, key))

                if self.single_obj:
                    self.single_obj = False
                    if not self.run_again():
                        break

        else:
            print()
            print('Single object reached. Here it is: ')
            print(f'>>>>> {obj} <<<<<')
            self.single_obj = True


    def main(self):
        self.iterative_get_json_part(obj=self.json_object)
