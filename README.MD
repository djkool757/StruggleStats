# StruggleStats

Concept Confusion Tracker is a web app that helps MCAT students log and visualize the concepts they struggle with most, revealing patterns in their learning over time. Built with a Flask backend and Vue.js frontend.

---

## ✨ Features

Tag wrong questions by Subtopic

User can add notes, like "aha" moments, after reviewing to any given topic 

Smart reminders(notification) within the site to review those concepts

---

## 🧱 Tech Stack

| Layer      | Tech           |
|------------|----------------|
| Backend    | Flask, SQLAlchemy, Flask-CORS |
| Frontend   | Vue.js (Vite), Axios, Tailwind CSS |
| Database   | SQLite (default, can be swapped for PostgreSQL/MySQL) |
| Communication | REST API via JSON |

---

## 📁 Project Structure
StruggleStats/
├── backend/ # Flask API
│ ├── app/ # Application package
│ │ ├── models.py
│ │ ├── routes.py
│ │ └── init.py
│ ├── run.py
│ └── requirements.txt
│
├── frontend/ # Vue.js frontend (Vite)
│ ├── src/
│ │ ├── components/
│ │ ├── App.vue
│ │ └── main.js
│ ├── vite.config.js
│ └── package.json
├──docker-compose.yml
├──Dockerfile.backend
├──Dockerfile.frontend
└── README.md

