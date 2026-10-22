# Python Lab 4 – Generators, Closures, and Utility Modules

## Overview

This lab demonstrates advanced Python programming concepts, including generators, closures, file input/output (I/O), and working with built-in modules such as `os`, `datetime`, and `calendar`.

## Project Structure

```text
python-lab4-generators-utilities/
├── fibonacci_generator.py
├── multiplier_closure.py
├── diary.py
├── diary.txt
├── calendar_utility.py
└── README.md
```

## Task 1 – Fibonacci Generator

**File:** `fibonacci_generator.py`

Created a generator function named `gen_fibonacci(n)` that produces the first `n` Fibonacci numbers using the `yield` keyword.

### Sample Output

```text
First 10 Fibonacci Numbers:
Fibonacci Number: 0
Fibonacci Number: 1
Fibonacci Number: 1
Fibonacci Number: 2
Fibonacci Number: 3
Fibonacci Number: 5
Fibonacci Number: 8
Fibonacci Number: 13
Fibonacci Number: 21
Fibonacci Number: 34
```

## Task 2 – Multiplier Closure

**File:** `multiplier_closure.py`

Created a function called `make_multiplier(factor)` that returns an inner function. The inner function remembers the multiplication factor even after the outer function finishes executing.

### Sample Output

```text
Multiplier Closure Results:
7 multiplied by 3 = 21
7 multiplied by 10 = 70
```

## Task 3 – Diary Entry Program

**File:** `diary.py`

Developed a diary program that uses the `os` module to check whether `diary.txt` exists, creates the file if necessary, and uses file I/O to append timestamped diary entries.

The program also reads and displays all saved entries and handles file-related errors using `try` and `except`.

### Sample Output

```text
Diary file already exists.
Enter your diary entry: I practiced using the os and datetime modules.

Diary entry saved successfully.

All Diary Entries:
2026-10-21 23:03:23 - Today I learned about Python file handling.
2026-10-21 23:04:04 - I practiced using the os and datetime modules.
```

## Task 4 – Date and Calendar Utility

**File:** `calendar_utility.py`

Created a program that accepts a year and month, displays the corresponding calendar, retrieves today's date, and checks whether today falls within the selected month.

The program also validates user input and handles invalid values.

### Sample Output – Current Month

```text
Enter a year: 2026
Enter a month (1-12): 10

Calendar for the Selected Month:
    October 2026
Mo Tu We Th Fr Sa Su
          1  2  3  4
 5  6  7  8  9 10 11
12 13 14 15 16 17 18
19 20 21 22 23 24 25
26 27 28 29 30 31

Today's Date: October 21, 2026
Today is October 21, 2026 and falls within the selected month.
```

### Sample Output – Different Month

```text
Enter a year: 2025
Enter a month (1-12): 3

Calendar for the Selected Month:
     March 2025
Mo Tu We Th Fr Sa Su
                1  2
 3  4  5  6  7  8  9
10 11 12 13 14 15 16
17 18 19 20 21 22 23
24 25 26 27 28 29 30
31

Today's Date: October 21, 2026
Today's date does not fall within the selected month.
```

### Error Handling Tests

**Invalid month (13):**

```text
Invalid Input: Month must be between 1 and 12.
```

**Invalid month (0):**

```text
Invalid Input: Month must be between 1 and 12.
```

**Invalid year input (`abc`):**

```text
Invalid Input: invalid literal for int() with base 10: 'abc'
```

## How to Run the Programs

Open a terminal in the project directory and execute:

```powershell
python fibonacci_generator.py
python multiplier_closure.py
python diary.py
python calendar_utility.py
```

The programs use Python's standard library and do not require additional packages.

## What I Learned

In this lab, I learned how to:

- Create generator functions using `yield`.
- Generate Fibonacci numbers without storing the entire sequence in a list.
- Create closures using nested functions.
- Use `os.path.exists()` to check whether a file exists.
- Create, append to, and read text files.
- Use the `with` statement to manage files.
- Generate timestamps using `datetime.now()`.
- Format dates using `strftime()`.
- Display monthly calendars using the `calendar` module.
- Validate user input and handle errors using `try` and `except`.

This lab helped me understand how to create reusable, efficient, and reliable Python programs using generators, closures, file operations, and utility modules.