# Chapter 3: Containerization – Standardizing the Application

## Overview
After successfully deploying the application to AWS EC2 in Chapter 2, the next major challenge was environment inconsistency.

Although the application was functional, deployments required repeated manual setup steps, including dependency installation, database configuration, and environment-specific fixes.

This made the system difficult to reproduce and unreliable across different machines.

At this stage, the primary issue was no longer the application code itself, but the environment in which it was running.

---

## Core Challenge
The application behaved differently depending on the execution environment:

- Local machine vs EC2 instance
- Missing dependencies on fresh environments
- Database configuration inconsistencies
- Repetitive manual setup steps

This created a fragile deployment process that could not scale reliably.

---

## Objective
The objective of this phase was to eliminate environment-related inconsistencies.

The system needed to run the same way regardless of where it was deployed.

**Goal:**  
Standardize the application environment and ensure consistent execution across any machine.

---

## Introducing Containerization
To solve these challenges, Docker was introduced.

Instead of relying on host machine configuration, the application and all required dependencies were packaged into containers.

This allowed the application to run consistently across:

- Local development environments
- Virtual machines
- Cloud infrastructure
- Fresh EC2 instances

The environment became part of the application itself.

---

## System Architecture
The system was restructured into a multi-container architecture:

- **API Service** – Flask application
- **Database Service** – PostgreSQL
- **Internal Docker Network** – service-to-service communication

The database connection was updated from `localhost` to the service name `db`.

This enabled reliable inter-container communication.

---

## Implementation Overview
The implementation included:

- Creating a `Dockerfile`
- Using `docker-compose.yml`
- Defining environment variables
- Mapping ports for external access
- Standardizing runtime dependencies

The full application stack could now be started with a single command:

```bash
docker compose up --build
