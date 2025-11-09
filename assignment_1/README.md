# Python Assignment 1

<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Completed-success.svg)

**A collection of basic Python programming exercises covering fundamental concepts**

</div>

---

## Overview

This repository contains solutions for Python Assignment 1, which focuses on fundamental Python programming concepts including:
- User input and output operations
- Basic mathematical operations
- String manipulation and formatting
- Variable handling and data types

## Features

- **Task 1**: Basic Mathematical Operations Calculator
- **Task 2**: Personalized Greeting Generator

---

## Prerequisites

Before running these programs, ensure you have the following installed:

- **Python 3.x** or higher
- A terminal or command prompt
- A text editor or IDE (optional)

To check your Python version:
```bash
python --version
# or
python3 --version
```

---

## Installation

1. Clone this repository or download the files:
```bash
git clone <repository-url>
cd assignment_1
```

2. No additional dependencies required - uses Python standard library only.

---

## Usage

### Task 1: Mathematical Operations

This program performs basic arithmetic operations on two numbers.

**Run the program:**
```bash
python task_1.py
# or
python3 task_1.py
```

**Example interaction:**
```
Task 1: Perform Basic Mathematical Operations
Enter the first number: 10
Enter the second number: 5
You entered: 10 and 5
Calculating results...
Addition: 15
Subtraction: 5
Multiplication: 50
Division: 2.0
```

**Features:**
- Accepts two integer inputs from the user
- Performs addition, subtraction, multiplication, and division
- Displays all results with clear labels

---

### Task 2: Personalized Greeting

This program creates a personalized welcome message using the user's name.

**Run the program:**
```bash
python task_2.py
# or
python3 task_2.py
```

**Example interaction:**
```
Task 2: Create a Personalized Greeting
Enter your first name: John
Enter your last name: Doe
Hello, John Doe! Welcome to Python programming.
```

**Features:**
- Captures user's first and last name
- Concatenates strings to create a personalized greeting
- Demonstrates string formatting techniques

---

## Project Structure

```
assignment_1/
│
├── task_1.py          # Mathematical operations program
├── task_2.py          # Personalized greeting program
├── screens/           # Screenshots folder
└── README.md          # Project documentation
```

---

## Code Breakdown

### Task 1 Code Overview
- Uses `input()` function to capture user data
- Converts string input to integers using `int()`
- Performs arithmetic operations: `+`, `-`, `*`, `/`
- Uses `print()` for formatted output

### Task 2 Code Overview
- Demonstrates string input handling
- Uses string concatenation with `+` operator
- Formats output with combined strings

---

## Screenshots

Screenshots of the program execution can be found in the [`screens/`](screens/) directory.

---

## Learning Outcomes

By completing this assignment, you will understand:

- How to use the `input()` function to get user input
- Type conversion in Python (`int()`, `str()`)
- Basic arithmetic operators
- String concatenation techniques
- Formatted output using `print()`
- Variable assignment and usage

---

## Error Handling

**Note:** The current implementations do not include error handling. Be aware of:

- **Task 1**: Non-integer inputs will cause a `ValueError`
- **Task 1**: Division by zero will cause a `ZeroDivisionError`

Future improvements could include try-except blocks for robust error handling.

---

## Future Enhancements

- [ ] Add input validation
- [ ] Implement error handling (try-except blocks)
- [ ] Add support for floating-point numbers in Task 1
- [ ] Create a menu-driven interface
- [ ] Add more mathematical operations (modulus, exponentiation)
- [ ] Unit tests for validation

---

## Contributing

This is an educational assignment project. If you have suggestions for improvements:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

---

## Author

**Akshari**

---

## License

This project is licensed under the MIT License - feel free to use this code for educational purposes.

---

## Acknowledgments

- Python Software Foundation for excellent documentation
- Educational institution for assignment guidelines

---

<div align="center">

**Happy Coding!**

Made with Python

</div>
