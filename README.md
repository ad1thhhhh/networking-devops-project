# ☕ Barista Task List App – Full Cloud Automation on Azure

## 🚀 Enterprise-Grade DevOps Automation Project

This project demonstrates a **production-style DevOps architecture** for deploying the **Barista Task List App** to **Microsoft Azure** using:

- Infrastructure as Code (**Terraform**)
- Containerization (**Docker**)
- CI/CD Automation (**GitHub Actions**)
- Configuration Management (**Ansible**)
- Immutable Infrastructure Principles

The system uses **two independent CI/CD pipelines**:

1. **Infrastructure Pipeline** – Provisions and manages Azure infrastructure  
2. **Application Deployment Pipeline** – Builds and deploys the containerized application  

This separation ensures production-level release safety, lifecycle control, and reduced operational risk.

---

# 🏗 High-Level Architecture

The architecture follows **immutable infrastructure principles**:

- Infrastructure is defined declaratively
- No manual server configuration
- Containers are replaced, not modified
- Infrastructure and application lifecycles are decoupled

---

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

During provisioning, the VM:

- Installs Docker Engine automatically
- Configures required dependencies
- Prepares runtime environment
- Runs containerized application on port:

```
80 → 5000
```

Infrastructure is fully manageable using:

```bash
terraform apply
terraform destroy
```

---

# 🔁 CI/CD Pipeline Architecture

The system is designed with **clear separation of concerns**:

| Pipeline | Responsibility |
|-----------|----------------|
| Infrastructure Pipeline | Provision & manage Azure resources |
| Application Pipeline | Build & deploy containerized app |

---

# 1️⃣ Infrastructure Pipeline

## 🔁 Trigger

- Triggered on changes in `/terraform` directory
- Push to `main` branch

## ⚙️ Workflow Responsibilities

- Checkout repository
- Authenticate to Azure using Service Principal
- Setup Terraform dynamically
- Run `terraform init`
- Run `terraform plan`
- Run `terraform apply -auto-approve`
- Extract VM public IP using `terraform output`
- Update GitHub repository secret (`VM_IP`) dynamically
- Enable cross-pipeline communication securely

## 🔄 Infrastructure Workflow Diagram

```
        Developer Push (Terraform Code)
                     │
                     ▼
           GitHub Actions Triggered
                     │
                     ▼
              Azure Login
                     │
                     ▼
              Setup Terraform
                     │
                     ▼
              terraform init
                     │
                     ▼
              terraform plan
                     │
                     ▼
              terraform apply
                     │
                     ▼
         Extract VM Public IP Output
                     │
                     ▼
        Update GitHub Secret (VM_IP)
                     │
                     ▼
           Infrastructure Ready
```

## 💡 Key Engineering Capabilities

- Idempotent infrastructure provisioning
- Secure Azure authentication via `azure/login@v2`
- Dynamic Terraform environment setup
- Runtime extraction of infrastructure outputs
- Automated secret propagation using GitHub CLI
- Zero manual cloud configuration

---

# 2️⃣ Application Deployment Pipeline

## 🔁 Trigger

- Push to:
  - `/app/**`
  - `/ansible/**`
- Manual trigger via `workflow_dispatch`

## ⚙️ Workflow Responsibilities

- Checkout application code
- Authenticate to DockerHub
- Build Docker image from `/app`
- Tag image using commit SHA
- Push image to DockerHub
- SSH into Azure VM
- Pull latest container image
- Stop existing container (if running)
- Remove old container instance
- Deploy new container
- Expose application on port `80 → 5000`

## 🔄 Application Workflow Diagram

```
        Developer Push (App Code)
                     │
                     ▼
           GitHub Actions Triggered
                     │
                     ▼
              DockerHub Login
                     │
                     ▼
              Build Docker Image
           (Tagged with Commit SHA)
                     │
                     ▼
              Push to DockerHub
                     │
                     ▼
              SSH into Azure VM
                     │
                     ▼
              Pull Latest Image
                     │
                     ▼
        Stop & Remove Old Container
                     │
                     ▼
              Run New Container
                     │
                     ▼
             Application Live
```

## 📦 Deployment Strategy

- Immutable container replacement
- Version-controlled image tagging
- Stateless deployments
- Secure SSH-based remote execution
- Fully automated release process

---

# ⚙️ Technology Stack

- **Cloud Provider:** Microsoft Azure  
- **Infrastructure as Code:** Terraform  
- **CI/CD Platform:** GitHub Actions  
- **Containerization:** Docker  
- **Configuration Management:** Ansible  
- **Authentication:** Azure Service Principal  
- **Secret Management:** GitHub Encrypted Secrets  

---

# 🔐 Security & Best Practices

- No credentials stored in source code
- Azure authentication via Service Principal
- SSH key-based VM authentication
- DockerHub credentials encrypted
- Network Security Groups defined via Terraform
- Cross-pipeline secret propagation
- Idempotent infrastructure updates

---

# 📊 Engineering Highlights

- Designed modular Terraform-based Azure infrastructure
- Implemented dual-pipeline CI/CD architecture
- Integrated Docker image lifecycle into automated workflow
- Automated VM bootstrapping using cloud-init
- Enabled full environment lifecycle management
- Achieved zero manual deployment effort
- Ensured deterministic and reproducible infrastructure provisioning
- Implemented secure secret handling across pipelines

---

# 🎯 Objective

This project demonstrates practical DevOps engineering capabilities by integrating:

- Infrastructure as Code
- Cloud networking design
- CI/CD automation
- Containerized application deployment
- Secure authentication practices
- Immutable infrastructure strategy

It reflects a real-world production deployment model rather than an academic implementation.

---

# 🧠 DevOps Principles Demonstrated

- Infrastructure as Code (IaC)
- Continuous Integration
- Continuous Deployment
- Immutable Infrastructure
- Separation of Concerns in CI/CD
- Secure Secret Management
- Automation-First Engineering
- Environment Reproducibility
- Declarative Infrastructure Design

---

# 📂 Repository Structure

```
├── terraform/                 # Infrastructure configuration
├── ansible/                   # Configuration management
├── app/                       # Application source code
├── .github/workflows/
│     ├── infrastructure.yml   # Infrastructure pipeline
│     └── application.yml      # Application pipeline
├── Dockerfile
└── README.md
```

---

# 🚀 Deployment Commands

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
