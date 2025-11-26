terraform = [

    # ---------------------- Difficulty 1 ----------------------
    {
        "category": "terraform",
        "term": "What is Infrastructure as Code (IaC)?",
        "difficulty": 1,
        "formal_definition": "Infrastructure as Code is the practice of managing infrastructure through machine-readable configuration files instead of manual processes.",
        "simple_definition": "Managing cloud resources using code instead of clicking in the console.",
        "example": "Terraform file that declares an AWS EC2 instance.",
        "why_it_matters": "IaC ensures repeatability, automation, and version-controlled infrastructure."
    },
    {
        "category": "terraform",
        "term": "What is Terraform?",
        "difficulty": 1,
        "formal_definition": "Terraform is an open-source IaC tool by HashiCorp that provisions and manages infrastructure across multiple cloud providers using declarative configuration.",
        "simple_definition": "A tool to build and manage cloud resources with code.",
        "example": "terraform apply creating S3 buckets and EC2s.",
        "why_it_matters": "Terraform is the industry standard for cloud automation."
    },

    # ---------------------- Difficulty 2 ----------------------
    {
        "category": "terraform",
        "term": "Terraform State",
        "difficulty": 2,
        "formal_definition": "Terraform state is a file that stores information about managed infrastructure, mapping real resources to configuration.",
        "simple_definition": "A file Terraform uses to remember what it built.",
        "example": "terraform.tfstate stored in S3 for team usage.",
        "why_it_matters": "State enables Terraform to detect drift and update infrastructure safely."
    },
    {
        "category": "terraform",
        "term": "Common Terraform Commands",
        "difficulty": 2,
        "formal_definition": "Terraform provides commands like init, plan, apply, destroy, fmt, validate that drive the IaC workflow.",
        "simple_definition": "Core commands to set up, preview, build, and clean infrastructure.",
        "example": "terraform plan → terraform apply.",
        "why_it_matters": "These commands make up the entire Terraform lifecycle."
    },
    {
        "category": "terraform",
        "term": "Terraform Backend",
        "difficulty": 2,
        "formal_definition": "A backend determines how Terraform stores state — locally or remotely (S3, GCS, Terraform Cloud).",
        "simple_definition": "Where Terraform keeps its state file.",
        "example": "S3 backend with DynamoDB locking.",
        "why_it_matters": "Remote backends enable safe team collaboration."
    },
    {
        "category": "terraform",
        "term": "Terraform Modules",
        "difficulty": 2,
        "formal_definition": "Modules are reusable groups of Terraform resources that provide encapsulation and standardization.",
        "simple_definition": "Reusable Terraform code blocks.",
        "example": "A VPC module reused across environments.",
        "why_it_matters": "Promotes best practices and reduces code duplication."
    },
    {
        "category": "terraform",
        "term": "Terraform Workflow",
        "difficulty": 2,
        "formal_definition": "The core workflow includes writing configuration, initializing providers, planning, and applying changes.",
        "simple_definition": "Write → Init → Plan → Apply.",
        "example": "Change a variable → run terraform plan.",
        "why_it_matters": "Understanding the workflow prevents destructive mistakes."
    },
    {
        "category": "terraform",
        "term": "Terraform vs CloudFormation vs ARM",
        "difficulty": 2,
        "formal_definition": "Terraform is cloud-agnostic; CloudFormation is AWS-specific; ARM is Azure-specific.",
        "simple_definition": "Terraform works everywhere; others are tied to their cloud.",
        "example": "Using Terraform to manage AWS + GCP in one codebase.",
        "why_it_matters": "Terraform's portability is a huge industry advantage."
    },
    {
        "category": "terraform",
        "term": "Terraform vs Ansible",
        "difficulty": 2,
        "formal_definition": "Terraform is declarative IaC for provisioning; Ansible is procedural configuration management.",
        "simple_definition": "Terraform builds infrastructure; Ansible configures it.",
        "example": "Terraform creates EC2 → Ansible installs packages on it.",
        "why_it_matters": "They solve different problems and are often used together."
    },
    {
        "category": "terraform",
        "term": "Terraform Provisioners",
        "difficulty": 2,
        "formal_definition": "Provisioners execute scripts on local or remote machines during resource creation or destruction.",
        "simple_definition": "Commands Terraform can run while creating resources.",
        "example": "running a shell script after creating EC2.",
        "why_it_matters": "Useful for bootstrapping but discouraged for major automation."
    },

    # ---------------------- Difficulty 3 ----------------------
    {
        "category": "terraform",
        "term": "Terragrunt",
        "difficulty": 3,
        "formal_definition": "Terragrunt is a wrapper tool that provides extra features like DRY modules, locking, and environment management.",
        "simple_definition": "A helper tool that makes Terraform cleaner and easier.",
        "example": "Centralizing remote backend settings in Terragrunt.",
        "why_it_matters": "Used heavily in large-scale enterprises."
    },
    {
        "category": "terraform",
        "term": "Null Resource",
        "difficulty": 3,
        "formal_definition": "A Terraform resource used to run arbitrary scripts or triggers without provisioning cloud infrastructure.",
        "simple_definition": "A resource that does nothing except run scripts.",
        "example": "local-exec to run a bash script.",
        "why_it_matters": "Useful for glue logic and orchestration."
    },
    {
        "category": "terraform",
        "term": "Terraform Validate & Format",
        "difficulty": 3,
        "formal_definition": "`terraform validate` checks for logical/syntax errors; `terraform fmt` formats code in standard style.",
        "simple_definition": "Commands to check and clean code.",
        "example": "terraform validate before committing.",
        "why_it_matters": "Ensures code quality and prevents misconfigurations."
    },
    {
        "category": "terraform",
        "term": "How Two People Use Same Directory",
        "difficulty": 3,
        "formal_definition": "Teams use workspaces or remote state with locking to ensure isolated or safe concurrent Terraform usage.",
        "simple_definition": "Use workspaces + remote state to avoid conflicts.",
        "example": "dev vs prod workspaces.",
        "why_it_matters": "Prevents two engineers from overwriting each other’s resources."
    },
    {
        "category": "terraform",
        "term": "Exporting Data Between Modules",
        "difficulty": 3,
        "formal_definition": "Modules expose values using outputs which can be passed to other modules as input variables.",
        "simple_definition": "Use outputs to pass data between modules.",
        "example": "vpc_id output passed into EC2 module.",
        "why_it_matters": "Critical for multi-module architectures."
    },

    # ---------------------- Difficulty 4 ----------------------
    {
        "category": "terraform",
        "term": "State File Locking",
        "difficulty": 4,
        "formal_definition": "A mechanism preventing simultaneous Terraform operations on the same state, usually using DynamoDB or Terraform Cloud.",
        "simple_definition": "Locks the state so two people can't run apply at the same time.",
        "example": "DynamoDB table prevents state corruption.",
        "why_it_matters": "Avoids race conditions and catastrophic resource overwrites."
    },
    {
        "category": "terraform",
        "term": "Where To Store Terraform State in CI/CD",
        "difficulty": 4,
        "formal_definition": "State should be stored in a remote backend such as S3 + DynamoDB or Terraform Cloud when used in pipelines.",
        "simple_definition": "Store state in S3/Terraform Cloud, never in the repo.",
        "example": "GitHub Actions pipeline referencing remote backend.",
        "why_it_matters": "Pipelines require safe, locked, centralized state."
    },
    {
        "category": "terraform",
        "term": "Testing Terraform Modules",
        "difficulty": 4,
        "formal_definition": "Terraform modules can be tested with Terratest, which provisions infrastructure in test environments to verify behavior.",
        "simple_definition": "Use Terratest to test Terraform code.",
        "example": "Testing a VPC module with Go tests.",
        "why_it_matters": "Prevents infrastructure bugs from reaching production."
    },
    {
        "category": "terraform",
        "term": "Terraform in CI/CD Pipelines",
        "difficulty": 4,
        "formal_definition": "Integrating Terraform with pipelines involves automated linting, planning, policy checks, and the approval workflow.",
        "simple_definition": "Running terraform plan/apply inside CI safely.",
        "example": "GitHub Actions running plan on pull request.",
        "why_it_matters": "Enables safe automated infra deployments."
    },
    {
        "category": "terraform",
        "term": "Importing Existing Resources",
        "difficulty": 4,
        "formal_definition": "terraform import maps existing real-world cloud resources into Terraform state without recreation.",
        "simple_definition": "Bring existing AWS resources under Terraform control.",
        "example": "terraform import aws_s3_bucket.example my-bucket",
        "why_it_matters": "Allows gradual migration to Terraform."
    },
    {
        "category": "terraform",
        "term": "Reconciling State With Real Infrastructure",
        "difficulty": 4,
        "formal_definition": "`terraform refresh` or `terraform plan` detect and reconcile drift between state and actual resources.",
        "simple_definition": "Making Terraform state match real cloud resources.",
        "example": "Detect drift when someone edits a resource in the AWS console.",
        "why_it_matters": "State drift is one of the biggest infra risks."
    },
    {
        "category": "terraform",
        "term": "Handling Secrets in Terraform",
        "difficulty": 4,
        "formal_definition": "Terraform integrates with secret managers (AWS Secrets Manager, Vault) and uses sensitive variables to avoid plaintext leakage.",
        "simple_definition": "Use secret managers, never commit secrets.",
        "example": "variable db_password { sensitive = true }",
        "why_it_matters": "Mismanaged secrets cause catastrophic breaches."
    },
    {
        "category": "terraform",
        "term": "Terraform Best Practices",
        "difficulty": 4,
        "formal_definition": "Best practices include modular design, remote state, locking, environment separation, tagging, version pinning, and avoiding provisioners.",
        "simple_definition": "Use modules, remote state, tags, and pinned versions.",
        "example": "Pin AWS provider to 5.30.0.",
        "why_it_matters": "Prevents disaster and ensures maintainable IaC."
    },
    {
        "category": "terraform",
        "term": "Checkov",
        "difficulty": 4,
        "formal_definition": "Checkov is a static analysis tool that scans Terraform for security and compliance misconfigurations.",
        "simple_definition": "A tool to detect Terraform security mistakes.",
        "example": "Checkov warns if an S3 bucket is public.",
        "why_it_matters": "Critical for DevSecOps pipelines."
    }
]
