# pefile-dictionary-to-json

A Python utility to convert PE (Portable Executable) file metadata to JSON format, handling non-serializable byte data.

## Overview

This tool uses the `pefile` library to extract detailed information from Windows PE files and converts the resulting data structure into a 
JSON-serializable format. It automatically handles the conversion of binary data to hex strings, making it easy to store and analyze PE file 
metadata in a human-readable format.

## Features

- Extracts comprehensive PE file metadata using `pefile`
- Recursively converts byte data to hex strings
- Handles byte keys in dictionaries by converting them to UTF-8 strings
- Preserves nested data structures
- Outputs formatted JSON for easy reading and analysis

## Requirements

- Python 3.10+ (due to type annotation syntax)
- pefile library

## Installation

```bash
pip install pefile
```

Clone this repository:
```bash
git clone https://github.com/zerodavesec/pefile-to-json.git
cd pefile-to-json
```

## Usage

### Important: Configure File Paths

Before running the script, you must modify the following default paths in the script:

```python
# These are placeholder paths that MUST be changed:
pe_file_path = "/path/to/file.exe"  # Change to your PE file location
json_file_path = "/path/to/output/file.json"  # Change to your desired output location
```

### Running the Script

After modifying the paths, you can run the script directly:

```bash
python pe_to_json.py
```

### Using as a Module

You can also import and use the functions in your own code:

```python
from pefile_to_json import save_pe_info_to_json

# Convert a PE file to JSON (specify the actual paths)
save_pe_info_to_json("path/to/your/file.exe", "path/to/your/output.json")
```

You can also use the conversion function directly:

```python
from pefile_to_json import convert_to_serializable

# Convert any object with byte data to a serializable format
serializable_data = convert_to_serializable(your_data)
```

## Example Output

The resulting JSON file will contain all the PE file information with byte data converted to hex strings. For example:

```json
{
    "DOS_HEADER": {
        "e_magic": "4d5a",
        "e_cblp": 144,
        ...
    },
    "NT_HEADERS": {
        "Signature": "50450000",
        ...
    },
    ...
}
```

## Use Cases

- Malware analysis and research
- PE file structure exploration
- Creating datasets for machine learning on PE files
- Storing PE metadata in databases or file systems
- Sharing PE file analysis results in a universal format

## License

MIT

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
