# School Management System

## Overview

The School Management System is a web application built using Django and Django REST Framework. Application allows schools to manage their data, including students, teachers, departments, and associated information effectively.

## Features

- **School Model**: Manage multiple schools and their details.
- **Department Model**: Organize subjects into departments within each school.
- **Teacher Model**: Manage teacher profiles, including their associated departments.
- **Student Model**: Manage student profiles, including their marks, percentage, and associated teachers and departments.
- **RESTful API**: Full CRUD functionality for all models using Django REST Framework.

## Technologies Used

- **Django**: Web framework for building the application.
- **Django REST Framework**: Toolkit for building Web APIs.
- **SQLite**: Default database for development (can be switched to PostgreSQL or others).
- **Python**: Programming language used for backend development.
- **Postman**: To do CRUD operations.

## Getting Started

### Prerequisites

- Python 3.10
- pip install(Python package installer)
- Django
- Django REST Framework(Serializers)
- Django extensions
- Django unfold

### Installation

1. Clone the repository:

   ```bash
   git clone 
   cd Project location
2. Create a Virutal enviornment and activate it:
 
    ```cmd
    python -m venv envname
    source evname/Script/activate  
    ```
3. Install the required packages:

    ```python
    pip install -r requirements.txt
    ```
4. Apply migrations:

    ```python
    python manage.py migrate
    ```
5. Create a superuser(for admin access):

    ```pyhton
    python manage.py createsuperuser
    ```
6. Start an app

    ```python
    python manage.py startapp appname
    ```
7. Make Migrations
    ```Python
    python manage.py makemigrations
    ```
8. Migrate

    ```python
    python manage.py migrate
    ```
9. Run the server

    ```python
    python manage.py runserver
    ```
## Summary

The School Management System is a comprehensive web application designed to streamline the management of school-related data, including students, teachers, departments, and schools. Built with Django and Django REST Framework, it offers a robust backend with RESTful APIs for easy integration and data handling. Users can efficiently perform CRUD operations on all models, ensuring a smooth experience for administrators and educators alike.

The application can be extended or modified to fit specific school requirements, making it a flexible solution for educational institutions.
