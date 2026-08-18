# Student Management System

A menu-driven Student Management System built with Python.

This project was built as part of my Python learning journey to practice core Python concepts, CRUD operations, JSON file handling, input validation, exception handling, custom exceptions, and modular code organization.

## Features

- Add a student
- List all students
- Search for a student by roll number
- Update student information
- Delete a student
- Validate student age
- Validate student marks
- Prevent duplicate roll numbers
- Prevent empty required fields
- Store student data persistently using JSON
- Handle invalid user input without crashing
- Generate unique student IDs

## Student Information

Each student record contains:

- ID
- Name
- Age
- Roll Number
- Marks
- Course
- Section

## Project Structure

```text
Student_Management_System/
│
├── .gitignore
├── README.md
├── main.py
├── student_manager.py
├── file_handler.py
└── students.json
```

## File Description

### `main.py`

The entry point of the application.

It displays the main menu and connects the user with the different student management operations.

### `student_manager.py`

Contains the main student management functionality, including:

- Adding students
- Listing students
- Searching students
- Updating students
- Deleting students
- Input validation
- Roll number validation
- Student display

### `file_handler.py`

Handles reading and writing student data using JSON.

### `students.json`

Stores student records so that the data remains available after the application is closed.

## Validation

The application includes validation for:

- Age must be between `0` and `120`
- Marks must be between `0` and `100`
- Required text fields cannot be empty
- Roll numbers must be unique
- Invalid numeric input is handled without crashing the application

## How It Works

The application follows a simple flow:

```text
User
  │
  ▼
main.py
  │
  ▼
student_manager.py
  │
  ▼
file_handler.py
  │
  ▼
students.json
```

The `main.py` file controls the application menu, while `student_manager.py` contains the student-related logic. The `file_handler.py` module is responsible for persistent JSON storage.

## How to Run

Make sure Python is installed on your system.

Clone the repository:

```bash
git clone https://github.com/AyeshaSIT/Student_Management_System.git
```

Navigate into the project directory:

```bash
cd Student_Management_System
```

Run the application:

```bash
python main.py
```

## Application Menu

```text
================================
Student Management System
================================
1. Add Student
2. List Students
3. Search Student
4. Update Student
5. Delete Student
0. Exit
```

## Example Student Record

```json
{
    "id": 1,
    "name": "Ayesha",
    "age": 26,
    "roll_no": "123",
    "marks": 97,
    "course": "BSCS",
    "section": "A"
}
```

## Concepts Demonstrated

This project demonstrates practical use of the following Python concepts:

- Variables and objects
- Data types
- Lists
- Dictionaries
- Mutable and immutable objects
- Functions
- Parameters and arguments
- Return values
- Conditional statements
- `for` loops
- `while` loops
- `break` and `continue`
- Exception handling
- Custom exceptions
- File handling
- JSON
- CRUD operations
- Input validation
- Modular programming
- Functions with single responsibilities
- Basic software design

## Error Handling

The application handles invalid user input using Python exception handling.

Examples include:

- Invalid numeric input
- Negative age
- Age greater than `120`
- Negative marks
- Marks greater than `100`
- Duplicate roll numbers
- Empty required fields
- Searching for a student that does not exist
- Deleting a student that does not exist

## Future Improvements

Possible future improvements include:

- Replace JSON storage with SQLite or another database
- Build a REST API using FastAPI
- Add authentication and authorization
- Add automated tests using `pytest`
- Add application logging
- Improve the command-line interface
- Add sorting and filtering functionality
- Add pagination for larger datasets
- Add a web-based frontend

## What I Learned

Through this project, I practiced moving from individual Python exercises to building a complete application.

The project helped me understand how to:

- Break a problem into smaller functions
- Separate application logic into modules
- Validate user input
- Handle exceptions gracefully
- Work with persistent JSON data
- Implement CRUD operations
- Use reusable helper functions
- Design a menu-driven application
- Refactor working code for better maintainability

## Project Status

**Completed**

The current version implements the core Student Management System functionality using Python and JSON storage.

