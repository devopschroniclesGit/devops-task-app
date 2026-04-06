# Chapter 6: Automated Deployment – CI/CD Integration with EC2

This chapter focuses on extending the existing CI pipeline into a full CI/CD workflow by automating deployment to the live EC2 environment.

After validating runtime deployment in Chapter 5, the next challenge was eliminating the manual steps required to update production after every code change.

## Objective
Automate deployment to EC2 after every successful build and image push.

## Tools Used
- GitHub Actions
- Docker
- Docker Hub
- Amazon EC2
- SSH deployment automation

## Pipeline Flow
git push → GitHub Actions → Build Docker Image → Push to Docker Hub → SSH to EC2 → Pull Latest Image → Restart Containers

## Key Improvements
- Automatic deployment after every push
- Secure EC2 access using GitHub Secrets
- Automatic container refresh
- Reduced manual operational steps
- Faster production updates

## Challenges Encountered
- SSH connectivity issues
- Incorrect secret values
- Container name conflicts
- Missing environment variables during redeployment
- Network dependency preservation

## Key Lesson Learned
Continuous Integration becomes Continuous Delivery when deployment is automated.

Automation must preserve both application artifacts and runtime configuration.

## Outcome
The system now automatically builds and deploys the latest version of the application to EC2 after every successful code change.

This chapter marks the transition from CI to a full CI/CD workflow.
