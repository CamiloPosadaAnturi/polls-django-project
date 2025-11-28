# Survey System (Django)

A survey system built with **Django**, based on the classic **polling model,** but professionally organized to serve as a foundation for real-world or educational projects.

---

## Main Features

- Question creation and management.
- Response option registration.
- Functional voting system.
- Results visualization.
- Administrative panel for managing surveys.

---

## Technologies Used

- **Python 3**
- **Django 5**
- HTML / CSS
- SQLite por defecto

---

## Installation and execution

Follow these steps to install and run the project in your local environment:

### 1. Clone the repository

In a folder you have already created, run the following command in the terminal:
```
git clone git@github.com:CamiloPosadaAnturi/polls-django-project.git
```
### 2. Create and activate a virtual environment
```
python3 -m venv venv
source venv/bin/activate
```
On Windows:
```
python -m venv venv
venv\Scripts\activate
```
### Install Dependencies
```
pip install -r requirements.txt
```
### Apply migrations
```
python manage.py migrate
```
### Create SuperUser
```
python manage.py createsuperuser
```
### Run the server
```
python manage.py runserver
```

### Usage

- `http://127.0.0.1:8000/` — Main survey page
- `http://127.0.0.1:8000/admin/` — Manage questions and options

---

### Tests

```bash
python manage.py test
```