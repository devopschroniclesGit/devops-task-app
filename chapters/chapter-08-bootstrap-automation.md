# Chapter 8 — EC2 Provisioning + Elastic IP + Bootstrap Automation

## *Provision compute infrastructure automatically*

This chapter builds directly on the Terraform foundation established in Chapter 7.

Previously, the focus was on:

- Terraform installation
- provider configuration
- security group creation
- region troubleshooting
- VM time synchronization

In this chapter, the infrastructure evolves into a fully usable compute environment.

The main objective was to provision an AWS EC2 instance automatically using Terraform and ensure that the server is immediately ready to host the application.

---

# Chapter Objective

The goal of this chapter was:

> **provision a production-ready EC2 instance with stable public access and automated bootstrap configuration**

This includes:

- EC2 instance provisioning
- Elastic IP allocation
- automatic Docker installation
- server startup automation
- reusable infrastructure workflow

This is a critical DevOps milestone because infrastructure now becomes:

> **repeatable + recoverable + scalable**

---

# Why this chapter comes next

After establishing Infrastructure as Code in Chapter 7, the next logical step was to provision actual compute resources.

The key engineering problem solved in this chapter was:

> **how do we create a server automatically and ensure it is deployment-ready from first boot?**

Manual server setup does not scale.

Bootstrap automation solves this problem.

---

# Project Structure

```text
devops-task-app/
├── app/
├── Dockerfile
├── .github/
│   └── workflows/
├── terraform/
│   ├── provider.tf
│   ├── main.tf
│   ├── outputs.tf
│   └── userdata.sh
