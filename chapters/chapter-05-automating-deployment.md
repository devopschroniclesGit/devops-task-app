# Chapter 5: Continuous Deployment – Automating Runtime Deployment

This chapter focuses on deploying the containerized application to a live cloud environment using Amazon EC2.

After introducing CI in Chapter 4, Docker images were automatically built and pushed to Docker Hub. However, deployment to a running environment was still manual.

## Objective
Standardize and validate how the application runs in a real cloud environment.

## Deployment Environment
- Amazon EC2
- Docker containers
- PostgreSQL database container
- Internal Docker networking

## Architecture
EC2 Instance
├── task-app (Flask API)
└── postgres-db (PostgreSQL)

Both containers communicate through an internal Docker network.

## Key Implementation Steps
- Provision EC2 instance
- Install Docker
- Pull latest image from Docker Hub
- Create Docker network
- Start PostgreSQL container
- Start Flask API container
- Configure environment variables
- Validate API connectivity

## Challenges Encountered
- Application failed without database dependency
- `localhost` inside containers caused connection failures
- Container name conflicts
- Missing service dependencies
- Manual environment preparation

## Key Lesson Learned
Applications do not run in isolation.

A successful deployment requires all dependent services, networking, and environment configuration to be provisioned correctly.

## Outcome
The system evolved from single-container execution to a reliable multi-container deployment running on EC2.

This chapter reinforces an important DevOps principle:

**You do not deploy applications, you deploy systems.**

## Next Phase
The application now runs successfully in the cloud, but deployment is still manual.

The next challenge is to fully automate deployment after every code change.
