# Azure Cloud Devops Automation

## Overview

This project demonstrates an automated cloud deployment workflow on Microsoft Azure using **Terraform** for Infrastructure as Code and **GitHub Actions** for CI/CD automation.

The pipeline is responsible for:

- Provisioning Azure infrastructure using Terraform  
- Building and pushing a Docker container image  
- Deploying the containerized application to Azure  
- Ensuring consistent and repeatable deployments  

The architecture follows **immutable infrastructure principles**, meaning infrastructure components are replaced rather than modified during updates. This approach improves reliability, reduces configuration drift, and makes rollbacks safer and more predictable.

---

## Tech Stack

- Microsoft Azure  
- Terraform  
- GitHub Actions  
- Docker  

---

## Key Features

- Fully automated infrastructure provisioning  
- Containerized application deployment  
- CI/CD pipeline triggered on code push  
- Reproducible and stateless deployments  
- Infrastructure managed as code  

---

## Deployment Flow

1. Code is pushed to the `main` branch  
2. GitHub Actions workflow is triggered  
3. Docker image is built and pushed to Docker Hub  
4. Terraform provisions or updates Azure resources  
5. Application is deployed using immutable deployment practices  

---

## Architecture Diagram

```
┌───────────────────────────────┐
│          Developer            │
└───────────────┬───────────────┘
                │  Git Push
                ▼
┌───────────────────────────────┐
│     GitHub Repository         │
│        (main branch)          │
└───────────────┬───────────────┘
                │  Triggers
                ▼
┌──────────────────────────────────────────┐
│        GitHub Actions CI/CD             │
│------------------------------------------│
│  • Build Docker Image                   │
│  • Push Image to DockerHub              │
│  • Terraform Init / Plan / Apply        │
└───────────────┬──────────────────────────┘
                │
                ▼
┌──────────────────────────────────────────┐
│          Microsoft Azure Cloud          │
│------------------------------------------│
│  • Resource Group                       │
│  • Virtual Network                      │
│  • Subnet                               │
│  • Network Security Group               │
│  • Public IP                            │
│  • Linux Virtual Machine                │
└───────────────┬──────────────────────────┘
                │  cloud-init
                ▼
┌───────────────────────────────┐
│     Docker Engine on VM      │
│  • Pull latest image         │
│  • Run container             │
└───────────────┬───────────────┘
                │
                ▼
┌───────────────────────────────┐
│   Publicly Accessible App    │
│     http://<public-ip>       │
└───────────────────────────────┘
```
## Objective

The goal of this project is to demonstrate practical DevOps skills by combining cloud infrastructure automation, containerization, and CI/CD into a single streamlined pipeline.
