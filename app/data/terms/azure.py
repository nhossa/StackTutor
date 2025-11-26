azure = [
    # ---------------------- Difficulty 1 ----------------------
    {
        "category": "azure",
        "term": "What is Azure?",
        "difficulty": 1,
        "formal_definition": "Azure is Microsoft's cloud computing platform offering services such as compute, storage, networking, databases, AI, and DevOps tools.",
        "simple_definition": "Microsoft’s cloud where you can run servers, databases, and apps.",
        "example": "Deploying a Node.js API to Azure App Service.",
        "why_it_matters": "Azure is the second-largest cloud provider; most enterprises rely on it."
    },
    {
        "category": "azure",
        "term": "What is Azure Blob Storage?",
        "difficulty": 1,
        "formal_definition": "Azure Blob Storage is a massively scalable object storage service for storing unstructured data like images, logs, videos, and backups.",
        "simple_definition": "Azure’s place to store files in the cloud.",
        "example": "Storing user-uploaded images in a blob container.",
        "why_it_matters": "Blob Storage is central to most Azure architectures and applications."
    },
    {
        "category": "azure",
        "term": "What is Azure App Service?",
        "difficulty": 1,
        "formal_definition": "Azure App Service is a fully managed platform for hosting web apps, REST APIs, and backend services in multiple languages.",
        "simple_definition": "A place to host websites or APIs without managing servers.",
        "example": "Running a Flask API on App Service.",
        "why_it_matters": "One of the most common hosting options for Azure developers."
    },

    # ---------------------- Difficulty 2 ----------------------
    {
        "category": "azure",
        "term": "What is Azure Function?",
        "difficulty": 2,
        "formal_definition": "Azure Functions is a serverless compute service that runs code in response to events without managing infrastructure.",
        "simple_definition": "Run code without servers — pay only when it executes.",
        "example": "Triggering a function when a file is uploaded to Blob Storage.",
        "why_it_matters": "Key Azure serverless technology used in modern cloud apps."
    },
    {
        "category": "azure",
        "term": "How to set an environment variable using Azure CLI?",
        "difficulty": 2,
        "formal_definition": "Environment variables can be set using the CLI command 'az webapp config appsettings set' for Azure App Service.",
        "simple_definition": "Use Azure CLI to add environment variables to your app.",
        "example": "az webapp config appsettings set --settings DB_PASSWORD=secret123",
        "why_it_matters": "Environment variables are critical for secure configuration."
    },
    {
        "category": "azure",
        "term": "Azure Blob Storage vs Azure File Service",
        "difficulty": 2,
        "formal_definition": "Blob Storage stores unstructured objects, while File Service provides SMB-based file shares suitable for legacy applications.",
        "simple_definition": "Blobs = object storage; Files = network file shares.",
        "example": "Blob for images; File Service for shared folders used by VMs.",
        "why_it_matters": "Choosing the correct storage type impacts cost and performance."
    },
    {
        "category": "azure",
        "term": "Azure Keys vs Secrets in Key Vault",
        "difficulty": 2,
        "formal_definition": "Keys are used for cryptographic operations; secrets store sensitive values such as tokens, passwords, and connection strings.",
        "simple_definition": "Keys = crypto operations; Secrets = passwords/strings.",
        "example": "Storing JWT signing keys vs storing DB passwords.",
        "why_it_matters": "Understanding this is essential for secure application design."
    },

    # ---------------------- Difficulty 3 ----------------------
    {
        "category": "azure",
        "term": "What are ARM templates?",
        "difficulty": 3,
        "formal_definition": "ARM (Azure Resource Manager) templates are JSON files that define Azure resources declaratively for automated deployment.",
        "simple_definition": "JSON templates used to deploy Azure resources automatically.",
        "example": "Deploying a VNet + VM using a single ARM template.",
        "why_it_matters": "Infrastructure-as-Code is a core cloud engineering skill."
    },
    {
        "category": "azure",
        "term": "What is Azure CDN?",
        "difficulty": 3,
        "formal_definition": "Azure CDN provides a globally distributed network of servers to deliver content with low latency by caching data close to users.",
        "simple_definition": "A network that speeds up delivery of static content.",
        "example": "Serving images through Azure CDN for faster global performance.",
        "why_it_matters": "Critical for performance at scale in global applications."
    },
    {
        "category": "azure",
        "term": "Azure App Service vs Azure Functions",
        "difficulty": 3,
        "formal_definition": "App Service runs full web apps with persistent hosting, while Functions execute event-driven serverless code without managing servers.",
        "simple_definition": "App Service = full web apps; Functions = event-driven serverless code.",
        "example": "App Service hosting a FastAPI app; Function triggered on queue message.",
        "why_it_matters": "Choosing the right compute model affects cost, performance, and maintenance."
    },
    {
        "category": "azure",
        "term": "Azure SQL Database vs SQL Managed Instance",
        "difficulty": 3,
        "formal_definition": "Azure SQL Database is a fully managed single database; Managed Instance offers near full SQL Server compatibility with instance-level features.",
        "simple_definition": "SQL DB = single database; Managed Instance = full SQL Server features.",
        "example": "Using Managed Instance to lift-and-shift a legacy SQL Server app.",
        "why_it_matters": "Choosing correctly avoids compatibility issues and overpaying."
    },
    {
        "category": "azure",
        "term": "When to use Azure Table Storage over Azure SQL?",
        "difficulty": 3,
        "formal_definition": "Azure Table Storage is ideal for non-relational, large-scale key-value or NoSQL scenarios. SQL is better for relational data requiring joins.",
        "simple_definition": "Use Table Storage for NoSQL key-value data; SQL for relational.",
        "example": "Storing millions of logs in Table Storage for cheap scalability.",
        "why_it_matters": "Choosing the right data model can dramatically improve cost/performance."
    },
    {
        "category": "azure",
        "term": "Difference between Block, Append, and Page Blobs",
        "difficulty": 3,
        "formal_definition": "Block blobs store files; Append blobs optimize append-only operations; Page blobs support random read/write, used for virtual disks.",
        "simple_definition": "Block = files, Append = logs, Page = VM disks.",
        "example": "Using Page Blobs for Azure VM OS disks.",
        "why_it_matters": "Proper blob type selection affects cost, performance, and correctness."
    },

    # ---------------------- Difficulty 4 ----------------------
    {
        "category": "azure",
        "term": "Many small blob containers vs one large container",
        "difficulty": 4,
        "formal_definition": "Multiple containers help with organization, access control, and lifecycle policies. One large container simplifies access but limits granularity of permissions.",
        "simple_definition": "More containers = better organization/security; one container = simplicity.",
        "example": "Separating production and staging data into different containers.",
        "why_it_matters": "Poor container organization can break permission models and cost management."
    },
    {
        "category": "azure",
        "term": "What is Azure Virtual Network (VNet)?",
        "difficulty": 4,
        "formal_definition": "Azure VNet is the fundamental building block for private networking in Azure, enabling IP ranges, subnets, routing, and security.",
        "simple_definition": "Azure's private network system.",
        "example": "Deploying VMs in a VNet with separate public and private subnets.",
        "why_it_matters": "All secure Azure architectures depend on VNets."
    },
    {
        "category": "azure",
        "term": "What is Azure Kubernetes Service (AKS)?",
        "difficulty": 4,
        "formal_definition": "AKS is a fully managed Kubernetes service that automates cluster creation, scaling, updates, and monitoring.",
        "simple_definition": "Managed Kubernetes for container orchestration.",
        "example": "Running a microservices app on AKS.",
        "why_it_matters": "AKS is the core service for large-scale containerized workloads."
    },
    {
        "category": "azure",
        "term": "What is Azure Service Bus?",
        "difficulty": 4,
        "formal_definition": "Azure Service Bus is a fully managed enterprise message broker supporting queues, topics, and pub/sub communication.",
        "simple_definition": "A messaging system for connecting distributed systems.",
        "example": "Publishing events from an API to a worker service via topics.",
        "why_it_matters": "Critical for event-driven architecture and decoupled systems."
    }
]
