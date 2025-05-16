# MCAT Content Outline Tracker

An interactive web app to help students review the AAMC MCAT content outline. Built with a Flask backend and Vue.js frontend.

---

## ✨ Features

- ✅ Track progress with "I know this / I don't know this" toggles
- 🎨 Color-coded mastery status per topic
- 📹 Linked resources (videos, articles) for each concept
- 🔍 Searchable and filterable content outline
- 🧪 REST API for flexibility and extensibility

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
neurotrack/
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
└── README.md
