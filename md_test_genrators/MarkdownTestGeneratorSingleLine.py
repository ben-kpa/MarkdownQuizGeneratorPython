import tkinter as tk
from tkinter import filedialog
import os
from datetime import datetime

def print_instructions():
    instructions = """
    This script processes a Markdown (.md) file by extracting specific sections.

    Instructions:
    1. When you run this script, a file dialog will open. Select the Markdown file you want to process.
    2. The script will ignore lines starting with '# ' (H1 headers) and '## ' (H2 headers), 
       but it will extract lines following an '## ' header until another header is encountered.
    3. The lines after each '## ' header will be combined into a single line separated by a space ' '.
    4. The processed content will be saved to a new file with '_quiz_' followed by the current timestamp appended to the original file name.
    5. The new file will be saved in the same directory as the original file.

    Note:
    - If no file is selected, the script will terminate with a message indicating no file was selected.
    - Ensure the selected file has read permissions and the destination directory has write permissions.
    """
    print(instructions)

def open_file_dialog():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.askopenfilename(filetypes=[("Markdown Files", "*.md"), ("All Files", "*.*")])
    return file_path

def get_current_datetime():
    return datetime.now().strftime("%Y%m%d%H%M%S")

def process_markdown(input_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            lines = infile.readlines()
    except FileNotFoundError:
        print("Could not open the file!")
        return

    selected_lines = []
    current_section = []
    copy = False
    joinString = " "

    for line in lines:
        stripped_line = line.strip()
        if line.startswith("# "):
            copy = False
            if current_section:
                selected_lines.append(joinString.join(current_section))
                current_section = []
        elif line.startswith("## "):
            copy = True
            if current_section:
                selected_lines.append(joinString.join(current_section))
                current_section = []
        elif line.startswith("###"):
            copy = False
            if current_section:
                selected_lines.append(joinString.join(current_section))
                current_section = []
        elif copy and stripped_line:
            current_section.append(stripped_line)

    if current_section:
        selected_lines.append(joinString.join(current_section))

    output_file = f"{os.path.splitext(input_file)[0]}_quiz_{get_current_datetime()}.md"

    try:
        with open(output_file, 'w', encoding='utf-8') as outfile:
            for line in selected_lines:
                if line.strip():  # Ensures no empty lines are written
                    outfile.write(line + "\n")
        print(f"Processed file saved as: {output_file}")
    except IOError:
        print("Could not create the output file!")

print_instructions()
file_path = open_file_dialog()
if not file_path:
    print("No file selected!")
else:
    process_markdown(file_path)
