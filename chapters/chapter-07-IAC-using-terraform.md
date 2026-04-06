# Chapter 7 — Infrastructure as Code with Terraform
## Provision infrastructure automatically

Chapter 7 marked a major shift in the project:

> from **manual cloud operations**
>
> to
>
> **Infrastructure as Code (IaC)**

Instead of creating resources manually in the AWS Console, infrastructure is now defined using **Terraform code**.

This chapter introduced the foundation for:

- repeatable deployments
- disaster recovery
- scaling
- infrastructure version control
- cloud automation

---

## Chapter Objective

The primary goal of this chapter was:

> **provision AWS infrastructure automatically using Terraform**

This means resources such as:

- EC2 instances
- Security groups
- Elastic IPs
- future load balancers

can now be created from code.

This is the foundation of modern DevOps and Platform Engineering.

---

## Why This Chapter Came Next

After successfully building:

- application deployment
- Dockerization
- CI/CD pipelines
- cloud deployment troubleshooting

the next logical step was:

> **automate the infrastructure layer**

Previously, infrastructure depended on:

- manually created EC2 instances
- manually tracked public IP addresses
- manually updated GitHub secrets

This approach does not scale.

Terraform solves this.

---

## Repository Structure

Infrastructure code was added directly into the Git repository.

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
