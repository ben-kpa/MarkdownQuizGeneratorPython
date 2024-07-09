# Markdown Test Generator README

## Overview

This project contains two Python scripts designed to help you generate quizzes from Markdown files using a specific formatting style. The scripts will extract questions and answers based on headings and their respective contents, enabling you to create quizzes for self-testing purposes.

## Markdown Formatting Style

- **Heading 1 (`#`)**: Represents the main topic of the document.
- **Heading 2 (`##`)**: Represents quiz questions.
- **Heading 3 (`###`)**: Represents the answer to the preceding quiz question. This section may contain various subsections.

### Example Markdown Structure

```markdown
# Topic 1

## Question 1
Content for question 1.

### Answer 1
Explanation or details for answer 1.

## Question 2
Content for question 2.

### Answer 2
Explanation or details for answer 2.
```

## Scripts

### 1. `MarkdownTestGenerator.py`

This script processes a Markdown (.md) file by extracting specific sections, primarily focusing on Heading 1 (`#`) and Heading 2 (`##`) headers, along with the lines following a Heading 2 header until another header is encountered.

#### Instructions

1. Run the script.
2. A file dialog will open; select the Markdown file you want to process.
3. The script extracts:
   - Lines starting with `#` and `##`.
   - Lines following a `##` header until another header is encountered.
4. If a Heading 2 (`##`) header is followed by another Heading 1 (`#`) or Heading 2 (`##`) header, it appends a placeholder line `### try:\n\n\n` before adding the next header.
5. The processed content is saved to a new file with `_test_` followed by the current timestamp appended to the original file name.
6. The new file is saved in the same directory as the original file.

#### Example Output

Given the example Markdown structure, the output file will contain:

```markdown
# Topic 1
## Question 1
Content for question 1.
### try:



## Question 2
Content for question 2.
### try:



```

### 2. `MarkdownTestGeneratorSingleLine.py`

This script processes a Markdown (.md) file by extracting specific sections, but it combines the lines following each `##` header into a single line, separated by a space.

#### Instructions

1. Run the script.
2. A file dialog will open; select the Markdown file you want to process.
3. The script extracts:
   - Lines following a `##` header until another header is encountered.
   - These lines are combined into a single line separated by a space.
4. The processed content is saved to a new file with `_test_` followed by the current timestamp appended to the original file name.
5. The new file is saved in the same directory as the original file.

#### Example Output

Given the example Markdown structure, the output file will contain:

```markdown
Content for question 1.
Content for question 2.
```

## Common Features

- **File Selection**: Both scripts use a file dialog to select the Markdown file.
- **Output File**: The processed content is saved with a timestamp in the original file's directory.
- **Error Handling**: If no file is selected or if there is an issue reading/writing files, appropriate messages are displayed.

## Usage

1. **Ensure Python is installed** on your system.
2. **Install necessary libraries**: `tkinter` is used for the file dialog (usually included with Python).
3. **Run the scripts** using a Python interpreter.

```bash
python MarkdownTestGenerator.py
python MarkdownTestGeneratorSingleLine.py
```

4. **Follow the on-screen instructions** to select your Markdown file and generate the quiz content.

## Compiling to Executables

To release these scripts as executable files, you can use `poetry` and `PyInstaller`. Follow the steps below to compile the scripts.

### Prerequisites

- Ensure you have `poetry` and `PyInstaller` installed on your system.

### Steps

1. **Activate the virtual environment**:

```bash
poetry shell
```

2. **Run PyInstaller**:

```bash
pyinstaller --onefile MarkdownTestGenerator.py
pyinstaller --onefile MarkdownTestGeneratorSingleLine.py
```

This will create standalone executable files for each script in the `dist` directory.

## Conclusion

These scripts are useful tools for extracting and formatting quiz questions and answers from Markdown files. Customize and enhance them as needed to fit your specific requirements. Happy studying!