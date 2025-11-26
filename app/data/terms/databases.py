databases = [
    # ---------------------- Difficulty 1 ----------------------
    {
        "category": "databases",
        "term": "What is a database?",
        "difficulty": 1,
        "formal_definition": "A database is an organized collection of structured information stored electronically and accessed via queries.",
        "simple_definition": "A place to store and retrieve data.",
        "example": "A PostgreSQL database holding user accounts.",
        "why_it_matters": "Every backend system relies on a database to store persistent data."
    },
    {
        "category": "databases",
        "term": "What is a DBMS?",
        "difficulty": 1,
        "formal_definition": "A Database Management System (DBMS) is software that manages databases, enabling storage, retrieval, and manipulation of data.",
        "simple_definition": "Software that controls and manages databases.",
        "example": "MySQL, PostgreSQL, MongoDB.",
        "why_it_matters": "Understanding DBMS systems is essential for building data-backed applications."
    },
    {
        "category": "databases",
        "term": "What is a database schema?",
        "difficulty": 1,
        "formal_definition": "A schema defines the structure of a database, including tables, fields, constraints, and relationships.",
        "simple_definition": "The blueprint or layout of the database.",
        "example": "A 'users' table with columns: id, email, password_hash.",
        "why_it_matters": "Schemas help maintain organized and predictable data structures."
    },

    # ---------------------- Difficulty 2 ----------------------
    {
        "category": "databases",
        "term": "Types of databases",
        "difficulty": 2,
        "formal_definition": "Databases are commonly categorized into relational, document, key-value, graph, time-series, and columnar databases.",
        "simple_definition": "Different databases store data in different ways based on use cases.",
        "example": "Relational (PostgreSQL), Document (MongoDB), Graph (Neo4j).",
        "why_it_matters": "Choosing the right type impacts scalability and performance."
    },
    {
        "category": "databases",
        "term": "Advantages and disadvantages of relational databases",
        "difficulty": 2,
        "formal_definition": "Relational databases enforce structured schemas, support ACID transactions, and use SQL, but may struggle with horizontal scaling.",
        "simple_definition": "They are reliable and structured, but don’t scale horizontally easily.",
        "example": "Banking systems use relational databases for strict consistency.",
        "why_it_matters": "Understanding tradeoffs helps pick the right database for your system."
    },
    {
        "category": "databases",
        "term": "Advantages and disadvantages of NoSQL databases",
        "difficulty": 2,
        "formal_definition": "NoSQL databases provide flexible schemas, horizontal scaling, and high performance, but may sacrifice consistency guarantees.",
        "simple_definition": "They scale well and are flexible, but consistency can be weaker.",
        "example": "MongoDB used for flexible JSON-like storage.",
        "why_it_matters": "NoSQL is essential for large-scale distributed applications."
    },
    {
        "category": "databases",
        "term": "What is a key-value database?",
        "difficulty": 2,
        "formal_definition": "A key-value store organizes data as key → value pairs with fast lookups.",
        "simple_definition": "A simple database storing key and value pairs.",
        "example": "Redis, DynamoDB.",
        "why_it_matters": "Extremely performant for caching, sessions, and high-speed reads."
    },
    {
        "category": "databases",
        "term": "What is a graph database?",
        "difficulty": 2,
        "formal_definition": "A graph database models data as nodes, edges, and properties to represent complex relationships.",
        "simple_definition": "A database designed for connected data.",
        "example": "Neo4j for social networks (friends, followers).",
        "why_it_matters": "Useful when relationships between entities matter more than the entities themselves."
    },

    # ---------------------- Difficulty 3 ----------------------
    {
        "category": "databases",
        "term": "What is database replication?",
        "difficulty": 3,
        "formal_definition": "Replication copies data across multiple database servers for redundancy and availability.",
        "simple_definition": "Copying data to multiple servers.",
        "example": "PostgreSQL primary → read replicas.",
        "why_it_matters": "Improves availability, failover, and read performance."
    },
    {
        "category": "databases",
        "term": "Master–slave vs master–master replication",
        "difficulty": 3,
        "formal_definition": "Master–slave has a single write node, while master–master allows multiple nodes to accept writes.",
        "simple_definition": "One-writer vs multiple-writers.",
        "example": "MySQL master with multiple read slaves.",
        "why_it_matters": "Affects scaling, failover, and consistency strategies."
    },
    {
        "category": "databases",
        "term": "Synchronous vs asynchronous replication",
        "difficulty": 3,
        "formal_definition": "Synchronous waits for replicas before confirming writes; asynchronous does not.",
        "simple_definition": "Wait for replicas (sync) vs don’t wait (async).",
        "example": "AWS RDS uses async read replicas for scalable reads.",
        "why_it_matters": "Determines trade-offs between consistency and performance."
    },
    {
        "category": "databases",
        "term": "What are database indexes?",
        "difficulty": 3,
        "formal_definition": "Indexes are data structures that speed up read queries by mapping keys to rows.",
        "simple_definition": "A shortcut for finding rows faster.",
        "example": "B-tree index on email column.",
        "why_it_matters": "Proper indexing can improve query speed by orders of magnitude."
    },
    {
        "category": "databases",
        "term": "What is database partitioning?",
        "difficulty": 3,
        "formal_definition": "Partitioning splits a large table into smaller, more manageable pieces.",
        "simple_definition": "Breaking a table into smaller chunks.",
        "example": "Splitting logs by month into separate partitions.",
        "why_it_matters": "Improves performance and reduces maintenance overhead."
    },
    {
        "category": "databases",
        "term": "What is database sharding?",
        "difficulty": 3,
        "formal_definition": "Sharding distributes data across multiple independent database servers based on a shard key.",
        "simple_definition": "Splitting data across many servers.",
        "example": "Users with IDs 0–10M in shard A, 10M–20M in shard B.",
        "why_it_matters": "Essential for horizontal scaling at massive scale."
    },

    # ---------------------- Difficulty 4 ----------------------
    {
        "category": "databases",
        "term": "What are message queues vs message brokers?",
        "difficulty": 4,
        "formal_definition": "Message queues temporarily store messages for async processing; message brokers route, transform, and distribute messages across systems.",
        "simple_definition": "Queues hold messages; brokers handle routing.",
        "example": "RabbitMQ (broker), SQS (queue).",
        "why_it_matters": "Critical for distributed and event-driven architectures."
    },
    {
        "category": "databases",
        "term": "How does a publish–subscribe model work?",
        "difficulty": 4,
        "formal_definition": "In pub/sub, publishers send messages to topics, and subscribers receive messages from topics without knowing each other.",
        "simple_definition": "Producers publish to topics; consumers subscribe to them.",
        "example": "Kafka topics broadcasting events.",
        "why_it_matters": "Decouples services and scales event-driven systems."
    },
    {
        "category": "databases",
        "term": "What is an event-driven architecture?",
        "difficulty": 4,
        "formal_definition": "An architecture where components communicate by producing and consuming events instead of direct service calls.",
        "simple_definition": "Systems talk by sending events rather than calling each other.",
        "example": "Order service emits 'OrderCreated' → Inventory service consumes it.",
        "why_it_matters": "Boosts scalability, reliability, and loose coupling."
    }
]
