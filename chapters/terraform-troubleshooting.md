# Terraform Pipeline Troubleshooting Notes

## Issue
Terraform workflow failed due to duplicate security group and missing remote state.

## Root Cause
- Security group already existed in AWS
- No persistent backend state configured
- Workflow attempted to recreate resources

## Planned Fix
- configure S3 backend
- import existing resources
- restore automated Terraform deployment
