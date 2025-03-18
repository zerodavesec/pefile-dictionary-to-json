import pefile
import json
from typing import Any

def convert_to_serializable(obj: Any) -> str | list[Any] | dict[str, Any] | Any:
    """Recursively convert non-serializable objects to serializable ones."""
    if isinstance(obj, bytes):
        return obj.hex()  
    elif isinstance(obj, (list, tuple)):
        return [convert_to_serializable(item) for item in obj]
    elif isinstance(obj, dict):
        return {key.decode('utf-8', errors='replace') if isinstance(key, bytes) else key: 
                convert_to_serializable(value) for key, value in obj.items()}
    else:
        return obj

def save_pe_info_to_json(pe_file_path: str, json_file_path: str) -> None:
    pe = pefile.PE(pe_file_path)
    
    pe_dict = pe.dump_dict()
    
    serializable_dict = convert_to_serializable(pe_dict)
    
    with open(json_file_path, 'w') as json_file:
        json.dump(serializable_dict, json_file, indent=4)

def main():
    pe_file_path = "/Users/dave/Downloads/7z2409-x64.exe"
    json_file_path = "/Users/dave/Downloads/7z2409-x64.json"
    save_pe_info_to_json(pe_file_path, json_file_path)

if __name__ == "__main__":
    main() 
