# Python Assignment 4: File Handling in Python

This repository contains solutions for Python Assignment 4, which includes two programming tasks demonstrating fundamental file handling operations in Python, including reading from files, writing to files, and error handling.

## Tasks

### Task 1: Read a File and Handle Errors

**File:** `t1_readfile.py`

A program that opens and reads a text file named `sample.txt`, prints its content line by line, and handles errors gracefully if the file does not exist.

**Features:**

- Opens and reads `sample.txt`
- Prints content line by line
- Handles `FileNotFoundError` if the file is missing
- Displays appropriate error message

**How to run:**

```bash
python t1_readfile.py
```

### Task 2: Write to File

**File:** `t2_write_file.py`

A program that demonstrates file writing operations by taking user input, writing it to a file, appending additional data, and displaying the final content.

**Features:**

- Accepts text input from the user to write to `output.txt`
- Appends additional data to the same file
- Reads and displays the complete file content
- Demonstrates write ('w') and append ('a') modes

**How to run:**

```bash
python t2_write_file.py
```

## Requirements

- Python 3.x

## Project Structure

```
assignment_4/
├── sample.txt          # Sample text file for Task 1
├── output.txt          # Output file created by Task 2
├── t1_readfile.py      # Task 1: File reading with error handling
├── t2_write_file.py    # Task 2: File writing and appending
├── screens/            # Screenshots of program execution
│   ├── terminal_t1.png
│   └── terminal_t2.png
└── README.md           # This file
```

## Screenshots

Execution screenshots are available in the `screens/` directory.
