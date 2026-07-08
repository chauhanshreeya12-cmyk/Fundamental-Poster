# Fundamental-Poster
# Interactive Personal Data Collector

## Overview
The **Interactive Personal Data Collector** is a simple Python program that collects a user's personal information through the command line. It demonstrates the use of Python data types, user input, formatted output, and the `datetime` module.

## Features
- Collects the following information from the user:
  - Name
  - Age
  - Height (in meters)
  - Favorite Number
- Displays:
  - Value entered
  - Data type of each value
  - Memory address of each variable using `id()`
- Calculates the user's approximate birth year based on the current year.
- Prints a thank-you message when the program ends.

## Technologies Used
- Python 3
- `datetime` module

## How to Run

1. Make sure Python 3 is installed on your computer.
2. Save the program as `personal_data_collector.py`.
3. Open a terminal or command prompt.
4. Run the program:

```bash
python personal_data_collector.py
```

## Example Output

```text
Welcome to the Interactive Personal Data Collector!

Enter your name: Alice
Enter your age: 20
Enter your height in meters: 1.65
Enter your favourite number: 7

Thank you! Here is the information we collected:

Name: Alice (Type: <class 'str'>, Memory Address: 140238...)
Age: 20 (Type: <class 'int'>, Memory Address: 9793696)
Height: 1.65 (Type: <class 'float'>, Memory Address: 140239...)
Favourite Number: 7 (Type: <class 'int'>, Memory Address: 9793280)

Your birth year is approximately: 2006

Thank you for using the Personal Data Collector. Goodbye!
```

## Bug in the Current Code

Your last `print()` statement contains a syntax error:

```python
print(f"Your birth year is approximately:{Your birth year is ")
```

Replace it with:

```python
print(f"Your birth year is approximately: {Birth_date}")
```

Also, correct the final message spelling:

```python
print("Thank you for using the Personal Data Collector. Goodbye!")
```

## Learning Concepts
This project demonstrates:
- Variables
- User Input (`input()`)
- Type Casting (`int()`, `float()`)
- Data Types
- Formatted Strings (f-strings)
- `type()` function
- `id()` function
- Importing Modules
- Using the `datetime` module
- Basic Arithmetic Operations

## Author
Created as a beginner Python practice project.
