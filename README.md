
---

###  Assignment 2: Ticket Booking Management System 

```markdown
# ticket Booking Management System

A Django web application for booking event/show tickets. Includes seat selection, booking history, and custom admin panel. This project strictly follows Class-Based Views (CBV), uses manual HTML forms, and is deployed using Docker and Jenkins.

---

## 🔧 Tech Stack

- Backend: Django (Python)
- Frontend: HTML, CSS, JavaScript

- DevOps: Docker, Docker Compose, Jenkins (CI/CD)

---

## 🚀 Features

### 🔐 Authentication
- User Registration
- User Login/Logout

### 🎫 User Functionality
- View upcoming events/shows
- Book tickets with seat selection
- View booking history

### 🛠️ Admin Panel
- Custom admin interface (no Django admin)
- Add/Edit/Delete events
- View all user bookings

---

## 🐳 Docker & Jenkins

### Docker
- `Dockerfile` included for containerization
- `docker-compose.yml` for quick setup

### Jenkins
- `Jenkinsfile` for CI/CD pipeline — build, test, deploy automation

---

## 🛠️ Setup Instructions

```bash
# Clone the repository
git clone https://github.com/nilam-10/booking-ticket-app


# Run using Docker
docker-compose up --build
view at http://localhost:8090/

#Project struture
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

