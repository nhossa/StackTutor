devops = [
    # ---------------------- Core DevOps Concepts ----------------------
    {
        "category": "devops",
        "term": "What is DevOps?",
        "difficulty": 1,
        "formal_definition": "DevOps is a set of cultural philosophies, practices, and automation techniques that unify software development and operations to deliver high-quality software quickly and reliably.",
        "simple_definition": "Developers and ops working together with automation to ship faster.",
        "example": "Developers push code, CI tests it, CD deploys it automatically.",
        "why_it_matters": "Modern engineering teams depend on DevOps to move fast safely."
    },
    {
        "category": "devops",
        "term": "Continuous Integration",
        "difficulty": 1,
        "formal_definition": "Continuous Integration is the practice of automatically building and testing code every time a developer commits changes.",
        "simple_definition": "Automatically test new code on every commit.",
        "example": "GitHub Actions running tests on each pull request.",
        "why_it_matters": "Prevents broken builds and keeps code stable."
    },
    {
        "category": "devops",
        "term": "Continuous Delivery",
        "difficulty": 2,
        "formal_definition": "Continuous Delivery ensures every code change is automatically tested and ready to deploy to production.",
        "simple_definition": "Every commit is production-ready.",
        "example": "CI pipeline builds Docker images and stores them in ECR.",
        "why_it_matters": "Eliminates risky deployments."
    },
    {
        "category": "devops",
        "term": "Continuous Deployment",
        "difficulty": 2,
        "formal_definition": "Continuous Deployment is the practice of automatically deploying code to production after it passes automated tests.",
        "simple_definition": "New code goes live automatically.",
        "example": "A commit to main autodeploys to ECS.",
        "why_it_matters": "Maximizes delivery speed."
    },

    # ---------------------- Tools ----------------------
    {
        "category": "devops",
        "term": "Docker",
        "difficulty": 2,
        "formal_definition": "A platform for packaging applications into portable, isolated containers.",
        "simple_definition": "A tool to package apps into containers.",
        "example": "Containerizing a FastAPI app.",
        "why_it_matters": "Ensures consistent environments everywhere."
    },
    {
        "category": "devops",
        "term": "Kubernetes",
        "difficulty": 3,
        "formal_definition": "An open-source system for automating deployment, scaling, and management of containerized applications.",
        "simple_definition": "A tool to run and manage containers across servers.",
        "example": "Running microservices on EKS.",
        "why_it_matters": "Industry standard for large-scale container orchestration."
    },
    {
        "category": "devops",
        "term": "Jenkins",
        "difficulty": 2,
        "formal_definition": "An open-source automation server used to build, test, and deploy software.",
        "simple_definition": "A tool to automate builds and releases.",
        "example": "Jenkins pipeline triggered by Git commits.",
        "why_it_matters": "Widely used for CI/CD in enterprises."
    },
    {
        "category": "devops",
        "term": "Terraform",
        "difficulty": 3,
        "formal_definition": "An Infrastructure as Code tool for provisioning and managing cloud resources.",
        "simple_definition": "Write code to create cloud resources.",
        "example": "Terraform scripts provisioning RDS and VPC.",
        "why_it_matters": "Makes infrastructure reproducible and version-controlled."
    },
    {
        "category": "devops",
        "term": "Ansible",
        "difficulty": 2,
        "formal_definition": "An automation tool for configuration management and application deployment.",
        "simple_definition": "Automates server setup and configuration.",
        "example": "Installing NGINX on servers using playbooks.",
        "why_it_matters": "Eliminates repetitive manual configuration."
    },
    {
        "category": "devops",
        "term": "Prometheus",
        "difficulty": 2,
        "formal_definition": "An open-source monitoring and alerting toolkit built for reliability.",
        "simple_definition": "A tool to monitor systems and send alerts.",
        "example": "Tracking CPU and memory usage.",
        "why_it_matters": "Helps catch issues early."
    },
    {
        "category": "devops",
        "term": "Grafana",
        "difficulty": 2,
        "formal_definition": "A visualization platform for graphing and analyzing time-series metrics.",
        "simple_definition": "Makes monitoring dashboards.",
        "example": "Visualizing Prometheus metrics.",
        "why_it_matters": "Critical for debugging and performance analysis."
    },
    {
        "category": "devops",
        "term": "Helm",
        "difficulty": 3,
        "formal_definition": "A package manager for Kubernetes applications.",
        "simple_definition": "Manages Kubernetes app deployments.",
        "example": "Deploying apps with Helm charts.",
        "why_it_matters": "Simplifies managing complex Kubernetes resources."
    },
    {
        "category": "devops",
        "term": "GitOps",
        "difficulty": 3,
        "formal_definition": "A practice where Git is the single source of truth for infrastructure and application deployment.",
        "simple_definition": "Manage infrastructure using Git workflows.",
        "example": "ArgoCD syncing Kubernetes manifests from Git.",
        "why_it_matters": "Brings reliability and history to infrastructure."
    },

    # ---------------------- Deployment Patterns ----------------------
    {
        "category": "devops",
        "term": "Blue-Green Deployment",
        "difficulty": 3,
        "formal_definition": "A deployment strategy with two identical environments where traffic switches only when the new version is validated.",
        "simple_definition": "Swap between two environments with no downtime.",
        "example": "Switch ALB traffic from Blue to Green.",
        "why_it_matters": "Provides instant rollback and zero downtime."
    },
    {
        "category": "devops",
        "term": "Canary Deployment",
        "difficulty": 3,
        "formal_definition": "A deployment strategy where a new version is rolled out to a small portion of users before full release.",
        "simple_definition": "Send the new version to a small test group first.",
        "example": "Routing 1% of traffic to the new release.",
        "why_it_matters": "Catches production issues early."
    },
    {
        "category": "devops",
        "term": "Rolling Deployment",
        "difficulty": 2,
        "formal_definition": "A deployment strategy that gradually updates instances with the new version.",
        "simple_definition": "Update servers one by one.",
        "example": "Updating EC2 instances via ASG rolling update.",
        "why_it_matters": "Avoids downtime and spreads risk."
    },

    # ---------------------- Advanced DevOps ----------------------
    {
        "category": "devops",
        "term": "Infrastructure as Code",
        "difficulty": 3,
        "formal_definition": "The practice of managing infrastructure using machine-readable configuration files.",
        "simple_definition": "Write code to control cloud resources.",
        "example": "Terraform provisioning VPC, subnets, and RDS.",
        "why_it_matters": "Automates and standardizes infrastructure."
    },
    {
        "category": "devops",
        "term": "Securing CI/CD Pipelines",
        "difficulty": 4,
        "formal_definition": "Includes secret management, dependency scanning, isolation, least-privilege IAM roles, and artifact signing.",
        "simple_definition": "Protect secrets, restrict access, scan dependencies.",
        "example": "Using GitHub OIDC with AWS IAM instead of long-lived keys.",
        "why_it_matters": "CI/CD pipelines are major security targets."
    }
]
