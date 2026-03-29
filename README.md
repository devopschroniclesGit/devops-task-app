## DevOps Task Management API

This project demonstrates the evolution of a simple application into a production-ready system using DevOps principles.

It showcases the journey from local development to automated build pipelines, solving real-world engineering challenges along the way.

## Project Journey
### Chapter 1 — Local Development
Flask API running on localhost
PostgreSQL database running locally
Manual setup and configuration
Limited accessibility and scalability
### Chapter 2 — Cloud Deployment (AWS EC2)

Application deployed to Amazon EC2

PostgreSQL installed and configured manually
Security groups configured for external access
# Real-world issues encountered:
Missing dependencies on fresh environments
Database authentication and permission errors
Network access restrictions
### Chapter 3 — Containerisation (Docker)

Application containerised using Docker

PostgreSQL runs in a separate container
Docker Compose used for orchestration
Environment standardised across systems
# Key improvements:
No manual setup required
Consistent execution across environments
Single command to run the entire system
### Chapter 4 — CI Pipeline (GitHub Actions)

A Continuous Integration pipeline was implemented using GitHub Actions

# Objective

Automate Docker image build and push on every code change

## Pipeline Workflow
git push → GitHub Actions → Build Docker Image → Push to Docker Hub
## Technologies Used
GitHub Actions
Docker
Docker Hub
# Secrets Configuration
Secret Name	Description
DOCKER_USERNAME	Docker Hub username
DOCKER_PASSWORD	Docker Hub access token
# Output Artifact

Docker image:

devopschroniclesdocker/task-app:latest
## Challenges & Lessons Learned
Secret misconfiguration (incorrect naming)
Docker authentication vs authorization issues
Token permission (Read vs Write) problems
Incorrect image tagging format
Credential caching in CI pipelines
## Key Insight

“Automation removes manual dependency from repetitive processes.”

## Architecture (Current)
Flask API (container)
PostgreSQL database (container)
Docker Compose orchestration
Internal container networking
CI pipeline for automated image builds
# Run Locally (Docker)

Clone the repository:

git clone https://github.com/devopschroniclesGit/devops-task-app.git
cd devops-task-app

Run the application:

docker compose up --build
# Access
http://localhost:5000/health
# Run on AWS EC2

Launch EC2 instance via Amazon EC2

Install Docker:

sudo apt update
sudo apt install docker.io -y
sudo systemctl start docker
sudo systemctl enable docker

Clone repository:

git clone https://github.com/devopschroniclesGit/devops-task-app.git
cd devops-task-app

Run:

docker compose up --build

Open port 5000 in Security Group.

## API Endpoints
Method	Endpoint	Description
GET	/health	Returns service status
GET	/tasks	Retrieves all tasks
POST	/tasks	Creates a new task
## Tech Stack
Python (Flask)
PostgreSQL
Docker
Docker Compose
Amazon EC2
GitHub Actions
## Challenges & Lessons Learned

During the project, several real-world issues were encountered:

Git submodule issues affecting repository structure
Container networking (localhost vs service name)
Port conflicts with local services
Docker Compose compatibility issues
OS-specific package installation challenges
Service readiness vs startup order
CI/CD secret misconfiguration
Docker registry authentication issues
## Key Takeaways
Environment consistency is critical
Containers eliminate “works on my machine” problems
Automation improves reliability and speed
CI pipelines reduce human error
Authentication and authorization are different concepts
## Key Principle

Build once, run anywhere.
