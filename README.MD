# Json analyzer

This module helps you analyze JSON objects interactively if you don't know their structure and want to determine the correct path to certain data.  
This significantly speeds up the development process for a beginner who finds it difficult to navigate the JSON object.

Please note: JSON only allows key names to be strings.

## Usage

Call the module from the command line.

#### Analaze json file:
```bash
python main.py --json-filename "example.json"
```

#### Analyze string json:
```bash
python main.py --json-string '{\"user\":{\"id\":1070,\"id_str\":\"1070\"}}'
```

## Example
```bash
python main.py --json-filename "example.json"
```

```bash
Json object was loaded. It's raw length is 77675 symbols

The type of this object is <class 'list'>
Length of this <class 'list'> is 20
Available keys: ['0', '1', ..., '16', '17', '18', '19']

Please input the key you want to open:
>>> 0

The type of this object is <class 'dict'>, reference path to object: obj_initial[0]
Available keys: dict_keys(['created_at', 'id', ...,'favorited', 'retweeted'])

Please input the key you want to open:
If you want to go level back press enter
>>> id

The type of this object is <class 'int'>, reference path to object: obj_initial[0][id]
Single object reached. Here it is:
>>>>> 1000020000236390000 <<<<<

If you want to go level back press enter
To stop the program enter "stop"
>>> stop

```