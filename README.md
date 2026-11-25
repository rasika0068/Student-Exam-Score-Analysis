# Student Exam Score Analysis

## Project Overview
Student Exam Score Analysis is a Python and MySQL-based project designed to manage and analyse student examination marks. It retrieves student records from a MySQL database and calculates total marks, percentages, grades, and pass/fail results.

## Features
- Store student marks in a MySQL database.
- Retrieve student records using Python.
- Calculate total marks out of 500.
- Calculate student percentages.
- Assign grades based on percentage.
- Display pass/fail results.

## Technologies Used
- Python
- MySQL
- SQL
- MySQL Connector for Python
- CSV

## Project Structure
```text
Student-Exam-Score-Analysis/
├── README.md
├── .gitignore
├── requirements.txt
├── student_scores.csv
├── student_analysis.py
├── database_analysis.py
└── queries.sql
```

## How to Run

1. Clone the repository.
2. Create and activate a Python virtual environment.
3. Install dependencies:
   `pip install -r requirements.txt`
4. Create the MySQL database and students table.
5. Insert the student records.
6. Run:
   `python3 database_analysis.py`

## Learning Outcomes
- Python programming and CSV file handling.
- SQL database creation and queries.
- Connecting Python applications with MySQL.
- Basic database operations and result analysis.