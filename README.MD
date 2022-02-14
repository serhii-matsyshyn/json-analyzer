# Json analyzer

This module helps you analyze JSON objects interactively if you don't know their structure and want to determine the correct path to certain data.  
This significantly speeds up the development process for a beginner who finds it difficult to navigate the JSON object.

Please note: JSON only allows key names to be strings.

## Usage

Call the module from the command line.

```bash
python main.py --json-filename "example.json"
```

```bash
python main.py --json-string '{\"user\":{\"id\":1070,\"id_str\":\"1070\"}}'
```
