# EduMatrix

## Student Performance Intelligence System

EduMatrix is a console-based student record and performance analytics system built with Python, JSON file handling, exception handling, and NumPy.

## Features

- Add a student
- View all students
- Search for a student by ID
- Update student information
- Delete a student
- Enter and update marks
- Enter and update attendance
- Generate an individual result card
- Generate class analytics
- Calculate totals, averages, grades, and pass/fail status
- Calculate weighted scores with NumPy
- Generate subject statistics
- Generate student rankings
- Detect at-risk students
- Calculate improvement from previous marks
- Save data in readable JSON format
- Load saved data automatically when the program starts

## Project Structure

```text
EduMatrix/
├── main.py
├── validators.py
├── storage.py
├── analytics.py
├── reports.py
├── students.json
├── requirements.txt
└── README.md
```

## File Responsibilities

### `main.py`

Contains the main menu, student operations, and program flow.

### `validators.py`

Contains input validation functions for text, age, marks, attendance, and mark collection.

### `storage.py`

Handles saving and loading student data from `students.json`.

### `analytics.py`

Contains NumPy matrix creation, class statistics, ranking, risk analysis, and improvement analysis.

### `reports.py`

Contains student profiles, grades, attendance status, and result cards.

### `students.json`

Stores student records in readable JSON format.

## Installation

Open a terminal inside the `EduMatrix` folder and run:

```text
python -m pip install -r requirements.txt
```

## Run the Project

Run:

```text
python main.py
```

On some systems, use:

```text
python3 main.py
```

## Data Saving

Student data is saved automatically after:

- Adding a student
- Updating a student
- Deleting a student
- Updating marks
- Updating attendance
- Selecting Exit

The data is stored in:

```text
students.json
```

## Technologies

- Python
- NumPy
- JSON
- File handling
- Exception handling

## Limitations

This version does not use:

- A database
- Pandas
- Matplotlib
- Machine learning
- GUI
- Web technologies

## Future Improvements

- User login system
- Separate backup system
- Export reports
- Graphical user interface
- Database support
<br>
Author : Engineer Jatoi