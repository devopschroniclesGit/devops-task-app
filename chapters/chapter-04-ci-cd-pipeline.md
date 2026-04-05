# Chapter 4: CI/CD Pipeline – Automating Build and Delivery

This chapter focuses on introducing **Continuous Integration (CI)** to automate the build and delivery process of the containerized application.

After standardizing the environment with Docker in Chapter 3, the next challenge was eliminating the manual process of building and pushing images.

## Objective
Automate the Docker image build and push process for every code change.

## Tools Used
- GitHub Actions
- Docker
- Docker Hub

## Pipeline Flow
git push → GitHub Actions → Build Docker Image → Push to Docker Hub

## Key Improvements
- Automatic image builds on every push
- Secure Docker Hub authentication using GitHub Secrets
- Consistent artifact generation
- Reduced manual deployment errors

## Key Lessons Learned
- Exact secret naming is critical
- Authentication and authorization are different
- Token permissions must allow push access
- CI automation improves reliability and speed

## Outcome
The application now automatically produces a deployable Docker image whenever changes are pushed to the repository.

This marks the transition from manual workflows to automated DevOps practices.
