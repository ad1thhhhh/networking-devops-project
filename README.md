# ☕ Barista Task List App – Full Cloud Automation on Azure

## Overview

This project demonstrates a **fully automated cloud framework** for deploying the Barsita Task List App to **Microsoft Azure** using:

- Infrastructure as Code (**Terraform**)
- Containerization (**Docker**)
- CI/CD Automation (**GitHub Actions**)
- Configuration Management (**Ansible**)

The system uses **two independent CI/CD pipelines**:
1. **Infrastructure Pipeline** – Provisions and manages Azure infrastructure  
2. **Application Deployment Pipeline** – Builds and deploys the containerized application  
This separation ensures safer releases, better lifecycle control, and production-style deployment architecture.

---

## 🏗 Architecture Overview

### Infrastructure Workflow

1. Triggered on push to main and when changes are detected in ./terraform directory
2. Uses actions/checkout@v3 to pull the latest code
3. Uses azure/login@v2 to authenticate Azure credentials
4. Installs Terraform dynamically in GitHub runner
5. Initializes backend & downloads provider plugins
6. Provisions or updates Azure infrastructure
7. Captures dynamic infrastructure output (VM public IP)
8. Github secrets are updated with VM public IP for Application Deployment pipeline


### Application Workflow

1. Triggered manually or when changes detected in .app/** .ansible/** directory
2. Uses actions/checkout@v3 to pull latest application code into GitHub runner
3. Logs into DockerHub using credentials in GitHub secrets
4. Builds container image from /app directory
5. Pushes versioned image to DockerHub
6. Stops and Removes Old Container
7. Runs new container (Port 80 -> 5000)
8. Application Live

This architecture enforces **immutable infrastructure** — infrastructure changes are applied declaratively, and application updates are delivered via container replacement rather than manual server modificatio


# ☁️ Cloud Infrastructure – Microsoft Azure

All infrastructure is provisioned using Terraform.

## Provisioned Resources

- Azure Resource Group
- Virtual Network (VNet)
- Subnet
- Network Security Group
- Public IP Address
- Linux Virtual Machine
- Cloud-init bootstrap configuration

## VM Bootstrapping

During provisioning:

- Docker Engine is installed automatically
- Required dependencies are configured
- VM is prepared to run containerized workloads
- Application container runs on port `80 → 5000`

---

# 🔁 CI/CD Pipeline Architecture

## 1️⃣ Infrastructure Pipeline

Triggered when:
- Changes occur in `/terraform` directory

Performs:

```yaml
1. Checkout repository
2. Authenticate to Azure (Service Principal)
3. Terraform init
4. Terraform validate
5. Terraform plan
6. Terraform apply
```

### Purpose

- Fully automated Azure resource provisioning
- Idempotent infrastructure updates
- Version-controlled infrastructure lifecycle
- Controlled environment creation & destruction

Infrastructure can also be destroyed using:

```bash
terraform destroy
```

---

## 2️⃣ Application Deployment Pipeline

Triggered when:
- Changes occur in `/app` directory
- Code is pushed to `main`

Performs:

```yaml
1. Checkout repository
2. Build Docker image
3. Tag image with commit SHA
4. Push image to Docker Hub
5. SSH into VM (or use automation)
6. Pull latest image
7. Restart container
```

### Purpose

- Isolated application release cycle
- Zero manual server updates
- Stateless container replacement
- Safe and repeatable deployments

---

# ⚙️ Technology Stack

- **Cloud Provider:** Microsoft Azure  
- **Infrastructure as Code:** Terraform  
- **CI/CD Platform:** GitHub Actions  
- **Containerization:** Docker  
- **Configuration Management:** Ansible  
- **Authentication:** Azure Service Principal  
- **Secrets Management:** GitHub Encrypted Secrets  

---

# 📦 Immutable Infrastructure Strategy

This project follows immutable deployment principles:

- No manual SSH configuration
- No in-place infrastructure mutation
- Infrastructure defined declaratively
- Containers replaced instead of modified
- Infrastructure lifecycle fully automated

### Benefits

- Eliminates configuration drift
- Predictable deployments
- Safer rollback strategy
- Reduced operational risk
- Complete auditability

---

# 🔐 Security & Best Practices

- Azure authentication via Service Principal
- No credentials stored in source code
- Encrypted GitHub secrets
- Network Security Group rules defined via Terraform
- Separation of infrastructure and application workflows
- Idempotent infrastructure provisioning

---

# 📊 Engineering Highlights

- Designed modular Terraform infrastructure
- Implemented dual-pipeline CI/CD architecture
- Integrated Docker build lifecycle into application workflow
- Automated VM provisioning using cloud-init
- Achieved full environment lifecycle automation
- Applied Infrastructure as Code best practices
- Enabled stateless, container-based deployments
- Reduced manual operational effort to zero

---

# 🎯 Objective

The goal of this project is to demonstrate practical DevOps engineering skills by combining:

- Infrastructure automation
- Cloud networking design
- CI/CD best practices
- Containerized application deployment
- Secure cloud authentication
- Immutable infrastructure strategy

This reflects a real-world production deployment model.

---

# 🧠 DevOps Principles Demonstrated

- Infrastructure as Code (IaC)
- Continuous Integration
- Continuous Deployment
- Cloud Resource Lifecycle Management
- Immutable Infrastructure
- Separation of Concerns in CI/CD
- Automation-First Engineering
- Environment Reproducibility

---

# 📂 Repository Structure

```
├── terraform/                 # Infrastructure configuration
├── ansible/                   # Configuration management
├── app/                       # Application source code
├── .github/workflows/
│     ├── infrastructure.yml   # Infra pipeline
│     └── application.yml      # App deployment pipeline
├── Dockerfile
└── README.md
```

---

# 🚀 How to Deploy

## Infrastructure

```bash
terraform init
terraform apply
```

## Destroy Infrastructure

```bash
terraform destroy
```

---

# 👤 Author

**Adithya**  
DevOps & Cloud Automation Engineer  

GitHub: https://github.com/ad1thhhhh
