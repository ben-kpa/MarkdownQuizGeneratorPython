import tkinter as tk
from tkinter import filedialog
import os
from datetime import datetime

def print_instructions():
    instructions = """
    This script processes a Markdown (.md) file by performing the following operations:

    1. Removing all empty lines.
    2. Adding a new line before each H2 heading (lines starting with '## ').
    3. Adding '#card' to the end of the line before each H3 heading (lines starting with '### ').

    Instructions:
    1. When you run this script, a file dialog will open. Select the Markdown file you want to process.
    2. The processed content will be saved to a new file with '_processed_' followed by the current timestamp appended to the original file name.
    3. The new file will be saved in the same directory as the original file.

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

def remove_empty_lines(text):
    lines = text.split('\n')
    non_empty_lines = [line for line in lines if line.strip() != '']
    cleaned_text = '\n'.join(non_empty_lines)
    return cleaned_text

def add_new_line_before_heading_2(text):
    lines = text.split('\n')
    modified_lines = []
    for line in lines:
        if line.startswith('## '):
            modified_lines.append('')
        modified_lines.append(line)
    modified_text = '\n'.join(modified_lines)
    return modified_text

def add_card_before_heading_3(text):
    lines = text.split('\n')
    modified_lines = []
    for i in range(len(lines)):
        if lines[i].startswith('### '):
            if i > 0 and not lines[i-1].startswith('#'):
                modified_lines[-1] = modified_lines[-1] + ' #card'
        modified_lines.append(lines[i])
    modified_text = '\n'.join(modified_lines)
    return modified_text

def process_markdown(input_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            text = infile.read()
    except FileNotFoundError:
        print("Could not open the file!")
        return

    cleaned_text = remove_empty_lines(text)
    formatted_new_lines = add_new_line_before_heading_2(cleaned_text)
    final_text = add_card_before_heading_3(formatted_new_lines)

    output_file = f"{os.path.splitext(input_file)[0]}_processed_{get_current_datetime()}.md"

    try:
        with open(output_file, 'w', encoding='utf-8') as outfile:
            outfile.write(final_text)
        print(f"Processed file saved as: {output_file}")
    except IOError:
        print("Could not create the output file!")


print_instructions()
file_path = open_file_dialog()
if not file_path:
    print("No file selected!")
else:
    process_markdown(file_path)
