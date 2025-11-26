system_design = [

    # ---------------------- Difficulty 1 ----------------------
    {
        "category": "system_design",
        "term": "What is a system?",
        "difficulty": 1,
        "formal_definition": "A system is a collection of components or services that work together to provide functionality to users.",
        "simple_definition": "A group of parts working together to do something.",
        "example": "A login service + database + frontend UI.",
        "why_it_matters": "Forms the basis for all design discussions."
    },

    # ---------------------- Difficulty 2 ----------------------
    {
        "category": "system_design",
        "term": "Microservices",
        "difficulty": 2,
        "formal_definition": "An architectural style where applications are built as independent, loosely coupled services.",
        "simple_definition": "Building apps from many small, independent services.",
        "example": "Amazon uses microservices for different business domains.",
        "why_it_matters": "Improves scalability, agility, and independent deployments."
    },
    {
        "category": "system_design",
        "term": "Monolith",
        "difficulty": 2,
        "formal_definition": "A software architecture where all functionality is contained in a single, unified codebase.",
        "simple_definition": "One big application handling everything.",
        "example": "Legacy ERP systems.",
        "why_it_matters": "Simple to build but hard to scale or update."
    },
    {
        "category": "system_design",
        "term": "Scalability",
        "difficulty": 2,
        "formal_definition": "The ability of a system to handle increasing load by adding resources.",
        "simple_definition": "How well a system can handle growth.",
        "example": "Adding more API servers to handle surge traffic.",
        "why_it_matters": "A core requirement for high-traffic systems."
    },
    {
        "category": "system_design",
        "term": "Load Balancing",
        "difficulty": 2,
        "formal_definition": "The practice of distributing incoming requests across multiple backend servers.",
        "simple_definition": "Spreading incoming traffic across servers.",
        "example": "AWS Elastic Load Balancer.",
        "why_it_matters": "Prevents overload and improves reliability."
    },
    {
        "category": "system_design",
        "term": "Caching",
        "difficulty": 2,
        "formal_definition": "A technique of storing frequently accessed data in fast storage to reduce latency and load.",
        "simple_definition": "Saving data so you don’t recompute it.",
        "example": "Redis caching popular queries.",
        "why_it_matters": "Biggest lever for performance improvement."
    },
    {
        "category": "system_design",
        "term": "Database Sharding",
        "difficulty": 2,
        "formal_definition": "A database partitioning technique that splits data across multiple servers.",
        "simple_definition": "Breaking a big database into smaller pieces.",
        "example": "Sharding users by region.",
        "why_it_matters": "Enables horizontal scaling."
    },
    {
        "category": "system_design",
        "term": "Message Queue",
        "difficulty": 2,
        "formal_definition": "A distributed messaging system that enables asynchronous communication between services.",
        "simple_definition": "A buffer system for sending messages between services.",
        "example": "RabbitMQ, SQS.",
        "why_it_matters": "Decouples services and handles spikes."
    },
    {
        "category": "system_design",
        "term": "CDN",
        "difficulty": 2,
        "formal_definition": "A distributed server network that caches and delivers static content close to users.",
        "simple_definition": "Servers around the world that speed up content delivery.",
        "example": "Cloudflare serving images quickly.",
        "why_it_matters": "Reduces latency and offloads origin servers."
    },
    {
        "category": "system_design",
        "term": "Event-Driven Architecture",
        "difficulty": 2,
        "formal_definition": "A design where services communicate by emitting and consuming events asynchronously.",
        "simple_definition": "Services reacting to events instead of direct calls.",
        "example": "Payment service emits 'payment_successful'.",
        "why_it_matters": "Makes systems decoupled and scalable."
    },
    {
        "category": "system_design",
        "term": "Redundancy",
        "difficulty": 2,
        "formal_definition": "The duplication of critical components to improve system availability and fault tolerance.",
        "simple_definition": "Having backups so nothing breaks.",
        "example": "Two load balancers in active-passive mode.",
        "why_it_matters": "Prevents single points of failure."
    },
    {
        "category": "system_design",
        "term": "API Gateway",
        "difficulty": 2,
        "formal_definition": "A centralized entry point that routes, transforms, and authenticates client API requests.",
        "simple_definition": "A front door for APIs.",
        "example": "AWS API Gateway or Kong.",
        "why_it_matters": "Adds security, observability, and request handling."
    },

    # ---------------------- Difficulty 3 ----------------------
    {
        "category": "system_design",
        "term": "Horizontal vs Vertical Scaling",
        "difficulty": 3,
        "formal_definition": "Horizontal scaling adds more machines; vertical scaling adds more power to existing machines.",
        "simple_definition": "Scaling out vs scaling up.",
        "example": "Adding more EC2s vs upgrading to bigger EC2s.",
        "why_it_matters": "Core to capacity planning."
    },
    {
        "category": "system_design",
        "term": "Read Replicas",
        "difficulty": 3,
        "formal_definition": "Database replicas used to distribute read-heavy workloads and reduce latency.",
        "simple_definition": "Copies of DB for read-only traffic.",
        "example": "Postgres read replicas in AWS RDS.",
        "why_it_matters": "Improves performance under load."
    },
    {
        "category": "system_design",
        "term": "Write Path vs Read Path",
        "difficulty": 3,
        "formal_definition": "The write path refers to how data is created/updated; the read path defines how data is retrieved with minimal latency.",
        "simple_definition": "How data gets written vs how it gets read.",
        "example": "Writes → primary DB; reads → replicas.",
        "why_it_matters": "Essential for designing scalable architectures."
    },
    {
        "category": "system_design",
        "term": "Strong vs Eventual Consistency",
        "difficulty": 3,
        "formal_definition": "Consistency models determine how soon all nodes in a distributed system reflect the same data.",
        "simple_definition": "Instant accuracy vs slight delay.",
        "example": "DynamoDB is eventually consistent.",
        "why_it_matters": "Affects user experience and performance."
    },

    # ---------------------- Difficulty 4 ----------------------
    {
        "category": "system_design",
        "term": "Rate Limiting",
        "difficulty": 4,
        "formal_definition": "A technique for controlling the number of requests a client can make within a time window.",
        "simple_definition": "Protecting APIs from too many requests.",
        "example": "100 requests per minute per IP.",
        "why_it_matters": "Prevents abuse and protects infrastructure."
    },
    {
        "category": "system_design",
        "term": "Circuit Breaker Pattern",
        "difficulty": 4,
        "formal_definition": "A resilience pattern that stops requests to a failing service to prevent cascading failures.",
        "simple_definition": "Stop calling a failing service to avoid bringing everything down.",
        "example": "If DB is down, API immediately returns fallback.",
        "why_it_matters": "Critical for stability in microservices."
    },
    {
        "category": "system_design",
        "term": "Throttling",
        "difficulty": 4,
        "formal_definition": "A technique for slowing down or delaying requests when systems become overloaded.",
        "simple_definition": "Intentionally slowing requests to protect systems.",
        "example": "Queueing or delaying non-critical tasks.",
        "why_it_matters": "Prevents overload and downtime."
    },
    {
        "category": "system_design",
        "term": "Failover",
        "difficulty": 4,
        "formal_definition": "Automatic switching to a backup system when the primary system fails.",
        "simple_definition": "Switch to backup when main system dies.",
        "example": "RDS Multi-AZ failover.",
        "why_it_matters": "Ensures high availability."
    },

    # ---------------------- Difficulty 5 ----------------------
    {
        "category": "system_design",
        "term": "CAP Theorem",
        "difficulty": 5,
        "formal_definition": "A distributed system can provide only two of the following three: Consistency, Availability, Partition Tolerance.",
        "simple_definition": "You can’t have all three—must choose two.",
        "example": "AP systems like DynamoDB choose availability.",
        "why_it_matters": "Guides architecture trade-offs in distributed systems."
    },
    {
        "category": "system_design",
        "term": "Distributed Consensus (Raft/Paxos)",
        "difficulty": 5,
        "formal_definition": "Protocols that ensure multiple nodes in a distributed system agree on shared state.",
        "simple_definition": "How servers agree on what's true.",
        "example": "Etcd uses Raft.",
        "why_it_matters": "Critical for leaders, clusters, and strong consistency."
    }
]
