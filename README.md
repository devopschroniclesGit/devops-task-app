## DevOps Task Management API

This project demonstrates the evolution of a simple application into a production-ready system using DevOps principles.

It showcases the journey from local development to cloud deployment and containerisation, while solving real-world engineering challenges along the way.

---

## Project Journey

### Chapter 1 — Local Development

* Flask API running on localhost
* PostgreSQL database running locally
* Manual setup and configuration
* Limited accessibility and scalability

---

### Chapter 2 — Cloud Deployment (AWS EC2)

* Application deployed to AWS EC2
* PostgreSQL installed and configured manually
* Security groups configured for external access
* Real-world issues encountered:

  * Missing dependencies on fresh environments
  * Database authentication and permission errors
  * Network access restrictions

---

### Chapter 3 — Containerisation (Docker)

* Application containerised using Docker
* PostgreSQL runs in a separate container
* Docker Compose used for orchestration
* Environment standardised across systems

Key improvements:

* No manual setup required
* Consistent execution across environments
* Single command to run the entire system

---

## Architecture (Current)

* Flask API (container)
* PostgreSQL database (container)
* Docker Compose orchestration
* Internal container networking

---

## Run Locally (Docker)

Clone the repository:

git clone https://github.com/devopschroniclesGit/devops-task-app.git

cd devops-task-app

Run the application:

docker compose up --build

---

## Access

http://localhost:5000/health

---

## Run on AWS EC2

1. Launch EC2 instance
2. Install Docker
3. Clone repository

git clone https://github.com/devopschroniclesGit/devops-task-app.git

cd devops-task-app

docker compose up --build

4. Open port **5000** in the Security Group

---

## API Endpoints

GET /health
Returns service status

GET /tasks
Retrieves all tasks

POST /tasks
Creates a new task

---

## Tech Stack

* Python (Flask)
* PostgreSQL
* Docker
* Docker Compose
* AWS EC2

---

## Challenges & Lessons Learned

During the project, several real-world issues were encountered:

* Git submodule issues affecting repository structure
* Container networking (`localhost` vs service name)
* Port conflicts with local services
* Docker Compose version incompatibility
* OS-specific package installation challenges
* Service startup timing (database readiness vs API startup)

---

## Key Takeaways

* Environment consistency is critical
* Containers eliminate "works on my machine" problems
* Infrastructure differs across operating systems
* Service readiness is not the same as startup order

---

## Key Principle

Build once, run anywhere.

---

## Next Steps

* Implement CI/CD pipeline (GitHub Actions)
* Automate builds and deployments
* Integrate container registry (Docker Hub / ECR)

---

## Summary

This project demonstrates practical DevOps skills by:

* Building a working API
* Deploying to the cloud
* Containerising the system
* Solving real-world infrastructure and deployment issues

It reflects an understanding of how applications evolve from development to production-ready systems.

