import tkinter as tk
from tkinter import filedialog
import os
from datetime import datetime

def print_instructions():
    instructions = """
    This script processes a Markdown (.md) file by extracting specific sections.

    Instructions:
    1. When you run this script, a file dialog will open. Select the Markdown file you want to process.
    2. The script will extract lines starting with '# ' (H1 headers) and '## ' (H2 headers), 
       as well as lines following an '## ' header until another header is encountered.
    3. The processed content will be saved to a new file with '_test_' followed by the current timestamp appended to the original file name.
    4. The new file will be saved in the same directory as the original file.

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
    previous_was_h2 = False
    copy = False

    for i, line in enumerate(lines):
        if line.startswith("# "):
            if previous_was_h2:
                selected_lines.append("### try:\n\n\n")
            selected_lines.append(line)
            previous_was_h2 = False
            copy = False
        elif line.startswith("## "):
            if previous_was_h2:
                selected_lines.append("### try:\n\n\n")
            selected_lines.append(line)
            previous_was_h2 = True
            copy = True
        elif line.startswith("###"):
            copy = False
        elif copy:
            selected_lines.append(line)

        # Check for the next header (## or #)
        if copy and (i+1 < len(lines)) and (lines[i+1].startswith("## ") or lines[i+1].startswith("# ")):
            copy = False

    # Handle the edge case for the last line
    if previous_was_h2:
        selected_lines.append("### try:\n\n\n")

    output_file = f"{os.path.splitext(input_file)[0]}_test_{get_current_datetime()}.md"

    try:
        with open(output_file, 'w', encoding='utf-8') as outfile:
            outfile.writelines(selected_lines)
        print(f"Processed file saved as: {output_file}")
    except IOError:
        print("Could not create the output file!")

if __name__ == "__main__":
    print_instructions()
    file_path = open_file_dialog()
    if not file_path:
        print("No file selected!")
    else:
        process_markdown(file_path)
