# Chapter 1: The Beginning – Local Development

## Overview
The journey started with a practical challenge: managing development tasks in a lightweight and programmatic way.

Traditional task management tools often require manual interaction and do not integrate naturally into development workflows or automation pipelines. To solve this, the objective was to build a simple HTTP-based task management API that could later serve as a foundation for CI/CD and DevOps automation.

At this stage, the focus was on proving the application concept and establishing a working backend service.

---

## Objective
The initial goal was to build a simple API capable of:

- Creating tasks
- Retrieving tasks
- Tracking task status (for example: `pending`, `completed`)
- Verifying service health through a `/health` endpoint

This transformed the project from a simple script into a stateful backend service with persistent storage.

---

## Initial Architecture
The entire system was developed and run locally.

### Components
- **Application Layer**: HTTP API service
- **Database Layer**: Local PostgreSQL instance
- **Communication**: `localhost`

All components were tightly coupled within a single local environment.

```text
Client Request
     |
     v
 Local API Service
     |
     v
PostgreSQL (localhost)
