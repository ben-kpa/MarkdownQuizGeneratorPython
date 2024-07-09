import sys
import re
import os
from datetime import datetime

def process_markdown(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    output_lines = []
    capture = False

    for line in lines:
        if re.match(r'^## ', line):
            capture = True
            output_lines.append(line)
        elif re.match(r'^#', line):
            capture = False
        elif capture:
            output_lines.append(line)

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    base_name, ext = os.path.splitext(file_path)
    new_file_name = f"{base_name}_test_{timestamp}{ext}"
    
    with open(new_file_name, 'w', encoding='utf-8') as new_file:
        new_file.writelines(output_lines)
    
    print(f"Processed file saved as {new_file_name}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python process_markdown.py <markdown_file>")
    else:
        process_markdown(sys.argv[1])
