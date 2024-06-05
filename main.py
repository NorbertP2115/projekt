import sys

def parse_args():
    if len(sys.argv) != 3:
        print("Usage: program.exe pathFile1.x pathFile2.y")
        sys.exit(1)
    return sys.argv[1], sys.argv[2]

if __name__ == "__main__":
    input_file, output_file = parse_args()
    print(f"Input File: {input_file}, Output File: {output_file}")
    
import json

def load_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except json.JSONDecodeError:
        print("Invalid JSON format")
        sys.exit(1)
