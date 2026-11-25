# 🎓 School Management System

A simple School Management System built with Python and Django. The application allows users to manage student records efficiently through a user-friendly interface.

The system implements CRUD (Create, Read, Update, Delete) operations, making it easy to add new students, view registered students, edit existing information, and delete student records.

## 🚀 Features

- **Add Students:** Register new students into the system.
- **View Students:** Display all registered students.
- **Edit Students:** Modify existing student information.
- **Update Students:** Save changes to student records.
- **Delete Students:** Remove student records from the database.
- **Search Students:** Search for students using their names.
- **Database Integration:** Store and manage student information using a database.
- **Django Admin:** Access the Django administration panel for backend management.

## 🛠️ Technologies Used

- Python
- Django
- HTML5
- CSS3
- MySQL
- Bootstrap (if used in the interface)

## 📂 Project Structure

```text
school_project/
│
├── manage.py
│
├── school_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── students/
│   ├── migrations/
│   ├── templates/
│   │   └── students/
│   │       └── home.html
│   │
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
└── db.sqlite3
```

## ⚙️ Installation and Setup

Follow these steps to run the project locally.

### 1. Clone the Repository

```bash
git clone YOUR_REPOSITORY_URL
```

### 2. Navigate to the Project Directory

```bash
cd school_project
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

**Mac/Linux:**

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install django mysqlclient
```

### 6. Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

### 8. Open the Application

Visit:

http://127.0.0.1:8000/students/

## 📋 Student Information

The application manages student records using the following information:

| Field | Description |
|---|---|
| Name | Student's full name |
| Age | Student's age |
| Course | Student's registered course |

## 🔄 CRUD Operations

The application demonstrates the four fundamental database operations:

| Operation | Description |
|---|---|
| Create | Add a new student |
| Read | Display registered students |
| Update | Edit existing student information |
| Delete | Remove a student from the database |

## 🎯 Project Objective

The main objective of this project is to demonstrate practical knowledge of Django web development, database integration, Django models, forms, views, URL routing, and CRUD operations.

It also serves as a practical introduction to building database-driven web applications using Python and Django.

## 👨‍💻 Developer

**Albert**

Software Engineer// Tech Enthusiast

Interested in Python, Django, JavaScript, React, MySQL, and Web Development.

---

⭐ If you find this project useful, feel free to explore it and learn from the implementation.
