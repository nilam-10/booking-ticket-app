# Ticket Booking Management System

A Django-based web application for booking tickets to shows/events, featuring seat selection, booking history, and a custom admin dashboard. Built entirely with Class-Based Views (CBVs) and manual form handling.

---

## 🛠️ Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite (default)
- **DevOps**: Docker, Docker Compose, Jenkins

---

## 🚀 Features

### 🔐 Authentication
- User Registration
- Secure Login & Logout

### 🎫 User Interface
- Browse upcoming shows and events
- Select and book seats
- Access personal booking history

### 🛠️ Admin Panel (Custom Interface)
- Add, edit, and delete shows
- View all user bookings
- Completely custom interface (no Django admin)

---

## 🐳 DevOps

- Fully containerized using Docker & Docker Compose
- Continuous Integration/Deployment enabled via Jenkins (`Jenkinsfile` included)

---

## ▶️ Setup Instructions

```bash
# Clone the repository
git clone https://github.com/nilam-10/booking-ticket-app

# Build and run the project
docker-compose up --build

# Visit the app at
http://localhost:8090/

#Project Structure
BOOKING-TICKET-APP/
├── ticket_booking/             # Project configuration
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── core/                       # Main application
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
├── demo.gif                    # UI walkthrough
└── README.md
