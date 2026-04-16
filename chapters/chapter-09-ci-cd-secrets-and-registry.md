# Chapter 9: CI/CD Secrets and Container Registry

This chapter focused on securing the CI/CD pipeline by integrating Docker Hub authentication using GitHub Actions secrets.

## Objectives
- Secure Docker login credentials
- Build container images in pipeline
- Push images to Docker Hub
- Prevent credential exposure

## Implementation
- Added `DOCKER_USERNAME`
- Added `DOCKER_PASSWORD`
- Configured GitHub repository secrets
- Updated workflow for secure login

## Key Commands
```bash
docker login
docker build -t task-app .
docker push devopschroniclesdocker/task-app:latest
