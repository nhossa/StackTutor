aws = [
    # ---------------------- Difficulty 1 ----------------------
    {
        "category": "aws",
        "term": "What is AWS?",
        "difficulty": 1,
        "formal_definition": "AWS (Amazon Web Services) is a cloud computing platform offering infrastructure and platform services such as compute, storage, networking, databases, and machine learning.",
        "simple_definition": "A cloud platform where you can run servers, databases, apps, and more.",
        "example": "Running a FastAPI app on AWS EC2.",
        "why_it_matters": "AWS is the most widely used cloud provider globally; fundamentals are mandatory for cloud roles."
    },
    {
        "category": "aws",
        "term": "What is EC2?",
        "difficulty": 1,
        "formal_definition": "EC2 is a compute service that provides resizable virtual machines in the cloud.",
        "simple_definition": "AWS virtual machines you can run apps on.",
        "example": "Launching an Ubuntu EC2 instance to host a backend API.",
        "why_it_matters": "It’s the core compute service used in most AWS architectures."
    },
    {
        "category": "aws",
        "term": "What is S3?",
        "difficulty": 1,
        "formal_definition": "Amazon S3 is an object storage service for storing files, backups, logs, and static assets.",
        "simple_definition": "A place to store files in the cloud.",
        "example": "Storing uploaded images or backups in an S3 bucket.",
        "why_it_matters": "One of the most used services in all of AWS; nearly every architecture uses S3."
    },

    # ---------------------- Difficulty 2 ----------------------
    {
        "category": "aws",
        "term": "Where can you store secrets in AWS?",
        "difficulty": 2,
        "formal_definition": "AWS Secrets Manager and AWS Systems Manager Parameter Store are the primary managed services for securely storing secrets and configuration values.",
        "simple_definition": "Use Secrets Manager or Parameter Store to securely store secrets.",
        "example": "Storing database passwords in Secrets Manager.",
        "why_it_matters": "Hardcoding secrets is insecure; secure storage is required for production."
    },
    {
        "category": "aws",
        "term": "What is an AMI?",
        "difficulty": 2,
        "formal_definition": "An AMI (Amazon Machine Image) contains the OS, configuration, and software needed to launch an EC2 instance.",
        "simple_definition": "A template used to create EC2 instances.",
        "example": "Creating a custom AMI after configuring Nginx and Docker.",
        "why_it_matters": "Used for auto-scaling, consistent deployments, and quick server creation."
    },
    {
        "category": "aws",
        "term": "What is auto-scaling?",
        "difficulty": 2,
        "formal_definition": "Autoscaling automatically adjusts the number of compute resources in response to traffic or performance metrics.",
        "simple_definition": "Automatically adds/removes servers based on traffic.",
        "example": "Scale out when CPU > 60%, scale in when CPU < 25%.",
        "why_it_matters": "Enables cost savings and handles variable traffic loads."
    },
    {
        "category": "aws",
        "term": "What are AWS load balancers?",
        "difficulty": 2,
        "formal_definition": "Elastic Load Balancing offers ALB (Application Load Balancer), NLB (Network Load Balancer), and GLB (Gateway Load Balancer) for distributing traffic.",
        "simple_definition": "Services that distribute traffic across your servers.",
        "example": "Using an ALB to route HTTP requests to EC2 instances.",
        "why_it_matters": "Load balancers are essential for high availability and scaling."
    },
    {
        "category": "aws",
        "term": "Which AWS services help minimize DDoS attacks?",
        "difficulty": 2,
        "formal_definition": "AWS Shield, AWS WAF, CloudFront, and Route 53 provide protection against DDoS attacks.",
        "simple_definition": "Shield, WAF, CloudFront, and Route53 help protect against attacks.",
        "example": "Using WAF rules to block suspicious IP ranges.",
        "why_it_matters": "Security is a core requirement for production workloads."
    },

    # ---------------------- Difficulty 3 ----------------------
    {
        "category": "aws",
        "term": "What is a VPC?",
        "difficulty": 3,
        "formal_definition": "A Virtual Private Cloud (VPC) is a logically isolated network in AWS where you define IP ranges, subnets, routing, and security.",
        "simple_definition": "Your own private network inside AWS.",
        "example": "Creating a VPC with public and private subnets.",
        "why_it_matters": "All modern AWS architectures rely on VPC networking."
    },
    {
        "category": "aws",
        "term": "How do subnets work?",
        "difficulty": 3,
        "formal_definition": "Subnets divide a VPC’s IP range into smaller networks, either public (internet-facing) or private (internal-only).",
        "simple_definition": "Smaller networks inside a VPC, either public or private.",
        "example": "Putting EC2 web servers in a public subnet; DB in a private subnet.",
        "why_it_matters": "Subnet organization impacts security, design, and scaling."
    },
    {
        "category": "aws",
        "term": "How do resources access the internet in a VPC?",
        "difficulty": 3,
        "formal_definition": "Public subnets require an Internet Gateway; private subnets require a NAT Gateway for outbound traffic.",
        "simple_definition": "Public uses IGW; private uses NAT.",
        "example": "Private EC2 instances using NAT Gateway to download updates.",
        "why_it_matters": "Understanding this prevents misconfigured apps unable to reach the internet."
    },
    {
        "category": "aws",
        "term": "Which object allows server ingress from the internet?",
        "difficulty": 3,
        "formal_definition": "A Security Group controls inbound and outbound traffic at the instance level.",
        "simple_definition": "Security Groups let you open ports for traffic.",
        "example": "Allowing inbound 443 to a load balancer.",
        "why_it_matters": "Security Groups are essential for controlling access and security."
    },
    {
        "category": "aws",
        "term": "What are Lambda managed runtimes?",
        "difficulty": 3,
        "formal_definition": "AWS Lambda supports managed runtimes such as Python, Node.js, Java, Go, Ruby, and .NET Core.",
        "simple_definition": "The languages Lambda natively supports.",
        "example": "Running a Python 3.12 Lambda function.",
        "why_it_matters": "Important when choosing how to run serverless workloads."
    },

    # ---------------------- Difficulty 4 ----------------------
    {
        "category": "aws",
        "term": "Where should databases be placed in a VPC?",
        "difficulty": 4,
        "formal_definition": "Databases should be placed in private subnets to prevent direct internet exposure.",
        "simple_definition": "Database servers belong in private subnets.",
        "example": "Hosting RDS MySQL in a private subnet with no public IP.",
        "why_it_matters": "Critical for security and architecture correctness."
    },
    {
        "category": "aws",
        "term": "Security best practices for EC2 instances",
        "difficulty": 4,
        "formal_definition": "Best practices include using IAM roles instead of keys, disabling root login, restricting SSH access, using SG least privilege, patching OS, encrypting EBS, and logging via CloudWatch.",
        "simple_definition": "Use IAM roles, restrict SSH, patch machines, and encrypt everything.",
        "example": "Assigning an IAM role to EC2 instead of storing AWS keys.",
        "why_it_matters": "Misconfigured EC2 security is a top cause of breaches."
    },
    {
        "category": "aws",
        "term": "How to handle peak traffic in autoscaling?",
        "difficulty": 4,
        "formal_definition": "Use scheduled scaling for predictable traffic patterns to pre-scale capacity before load arrives.",
        "simple_definition": "Use scheduled scaling before heavy traffic hits.",
        "example": "Scale to 10 instances every Wednesday and Friday at 8:50 AM.",
        "why_it_matters": "Avoids slow scale-out delays and keeps applications responsive."
    },
    {
        "category": "aws",
        "term": "How to reduce EC2 load when CPU hits 100%?",
        "difficulty": 4,
        "formal_definition": "Configure CloudWatch alarms to trigger autoscaling scale-out policies or move heavy workloads to SQS/Lambda asynchronous processing.",
        "simple_definition": "Use autoscaling or offload work to serverless queues.",
        "example": "Scale from 2 → 6 instances when CPU > 85% for 2 minutes.",
        "why_it_matters": "High CPU on a single node can lead to service outages."
    },
    {
        "category": "aws",
        "term": "Explain how to build a 3-tier AWS architecture",
        "difficulty": 4,
        "formal_definition": "A 3-tier architecture consists of a public presentation tier (ALB + EC2/ECS), a private application tier (EC2/ECS), and a private data tier (RDS/NoSQL), all inside a VPC with separate subnets and routing.",
        "simple_definition": "Frontend tier → App tier → Database tier in separate subnets.",
        "example": "ALB → EC2 app servers → RDS MySQL in private subnets.",
        "why_it_matters": "This is the classic architecture pattern for scalable, secure cloud apps."
    }
]
