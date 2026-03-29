# DevOps Task Management API

## Overview
This project demonstrates the evolution of a local application into a production-ready DevOps system.

Chapter 1 focuses on building a local API with a PostgreSQL database.

---

## Architecture (Chapter 1)

- Flask API
- PostgreSQL database
- Local environment

---

## Setup Instructions

### 1. Clone repo
git clone https://github.com/YOUR_USERNAME/devops-task-app.git

cd devops-task-app/app

### 2. Create virtual environment
python3 -m venv venv
source venv/bin/activate

### 3. Install dependencies
pip install -r requirements.txt

---

## Database Setup

Install PostgreSQL and create:

- Database: taskdb
- User: devuser
- Password: devpass

---

## Run Application

python app.py

---

## Access

http://localhost:5000/health

---

## Limitations (Chapter 1)

- Local only
- Manual setup
- No CI/CD
- No containerisation
- No scalability

---

## Next Steps

- Dockerisation
- CI/CD pipelines
- AWS deployment
