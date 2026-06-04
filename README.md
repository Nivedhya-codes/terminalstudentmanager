# Terminal Student Manager

## Overview

Terminal Student Manager is a Python-based console application that helps manage student academic records. The program allows users to add students, store their marks, view subject-wise marks, and generate detailed report cards.

The project demonstrates important Object-Oriented Programming (OOP) concepts such as inheritance, abstraction, decorators, and file handling.

---

## Features

* Add new student records
* Store student information in a text file
* Search students using Roll Number
* View subject-wise marks
* Generate detailed report cards
* Calculate total marks and average
* Assign grades automatically
* Uses decorators to log report generation

---

## Technologies Used

* Python 3
* Object-Oriented Programming (OOP)
* File Handling
* Abstract Classes
* Decorators

---

## Project Structure

```text
TerminalStudentManager/
│
├── main.py
├── student.py
├── person.py
├── students.txt
└── README.md
```

---

## OOP Concepts Implemented

### Inheritance

The `Student` class inherits from the `Person` class.

### Abstraction

The `Report` abstract class contains the abstract method:

```python
generate_report()
```

which is implemented by the `Student` class.

### Decorators

The `log_report` decorator displays messages before and after generating a report.

### Encapsulation

Student information is stored and managed within the `Student` class through methods.

---

## Subjects Included

* Physics
* Mathematics
* Chemistry
* Computer Science
* English

---

## Grading System

| Average Marks | Grade |
| ------------- | ----- |
| 90 and above  | A+    |
| 80 - 89       | A     |
| 75 - 79       | B     |
| 65 - 74       | C     |
| Below 65      | Fail  |

---

## How to Run

1. Open the project folder.
2. Open a terminal.
3. Run:

```bash
python main.py
```

4. Choose an option from the menu.

---

## Menu Options

```text
1. Add Student
2. View Marks
3. View Report Card
4. Exit
```

---

## Sample Student Record

```text
1202,Aarav Nair,88,92,85,95,90
```

Format:

```text
RollNo,Name,Physics,Maths,Chemistry,Computer,English
```

---

## Learning Outcomes

This project helps understand:

* Classes and Objects
* Inheritance
* Abstract Classes
* Decorators
* Static Methods
* File Handling
* Menu-Driven Programming
* Data Management using Text Files

---
