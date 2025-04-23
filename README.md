
---

### Assignment 2: Ticket Booking Management System 

```markdown
#  Ticket Booking Management System

A Django web application for booking event/show tickets with seat selection, booking history, and a custom admin dashboard. Built entirely using CBVs, and manual form handling.

---

## 🔧 Tech Stack

- Backend: Django (Python)
- Frontend: HTML, CSS, JavaScript
- DevOps: Docker, Docker Compose, Jenkins
- Database: SQLite (default)

---

## 🚀 Features

### 🔐 Authentication
- Register, Login, Logout

### 🧑‍💻 User Experience
- View shows/events
- Book tickets with seat selection
- View booking history

### 🛠️ Admin Features
- Manage shows: Add/Edit/Delete
- View all bookings
- Custom interface (not Django Admin)

---

## 🐳 DevOps

- Fully Dockerized
- CI/CD via Jenkins (`Jenkinsfile` included)


---
## ▶️ Setup Instructions

```bash
git clone https://github.com/nilam-10/booking-ticket-app

docker-compose up --build
open at http://localhost:8090/

#Project Structure
BOOKING-TICKET-APP/
├── ticket_booking/             # Project settings
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── core/                       # Main app with views, templates, logic
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   ├── static/
│   ├── templates/
│   └── tests/
│
├── docker-compose.yml
├── Dockerfile
├── Jenkinsfile
├── manage.py
├── requirements.txt
├── demo.gif                    # UI demo
└── README.md
