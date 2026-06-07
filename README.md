# 🎓 Smart Student Manager

A console-based Student Management System built with Python using Object-Oriented Programming (OOP) principles and JSON file storage.

This project allows students to register, log in securely, access their academic records, view subject-wise marks, and generate a detailed report card.

---

## ✨ Features

### 🔐 User Authentication

* Student Registration
* Student Login
* Username validation
* Roll number verification during registration
* JSON-based user storage

### 📚 Student Records

* Preloaded student database
* Search students using Roll Number
* Retrieve student details from JSON storage

### 📊 Academic Performance

* View subject-wise marks
* Automatic total marks calculation
* Percentage calculation
* Grade generation
* School-style report card display

### 🗂 File Handling

* Uses JSON files instead of text files
* Structured data storage
* Easy data retrieval and management

### 🏗 Object-Oriented Design

* User class for authentication
* Student class for academic records
* Modular and maintainable code structure

---

## 📁 Project Structure

```text
studentmanager/
│
├── main.py
├── auth.py
├── student.py
├── person.py
├── users.json
├── students.json
└── README.md
```

---

## 🚀 Getting Started

### Clone the Repository

```bash
git clone <repository-url>
cd studentmanager
```

### Run the Project

```bash
python main.py
```

---

## 📋 Sample Menu

```text
=============================================
   ABC SCHOOL STUDENT MANAGEMENT SYSTEM
=============================================

1. Register
2. Login
3. Exit
```

After Login:

```text
==========================
 SMART STUDENT MANAGER
==========================
1. View Marks
2. View Report Card
3. Exit
```

---

## 🛠 Technologies Used

* Python 3
* JSON
* Object-Oriented Programming (OOP)
* File Handling

---

## 🎯 Learning Outcomes

This project demonstrates:

* Classes and Objects
* Inheritance
* File Handling
* JSON Operations
* Authentication Systems
* Data Validation
* Modular Programming
* Python Best Practices

---

## 📌 Future Improvements

* Password Hashing (bcrypt)
* Student Ranking System
* Attendance Management
* Marks Analytics
* SQLite Database Integration
* GUI Version using Tkinter
* Web Version using Flask

---
