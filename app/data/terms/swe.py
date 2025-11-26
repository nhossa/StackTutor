swe = [

    # ---------------------- Difficulty 1 ----------------------
    {
        "category": "swe",
        "term": "What is software engineering?",
        "difficulty": 1,
        "formal_definition": "Software engineering is the discipline of designing, developing, testing, and maintaining software systems in a systematic and efficient manner.",
        "simple_definition": "Building software the right way—from planning to coding to maintenance.",
        "example": "Designing and building a FastAPI backend for an app.",
        "why_it_matters": "Forms the foundation of all professional development work."
    },

    # ---------------------- Difficulty 2 ----------------------
    {
        "category": "swe",
        "term": "Agile",
        "difficulty": 2,
        "formal_definition": "Agile is an iterative software development methodology focused on delivering small increments of value with continuous feedback.",
        "simple_definition": "Building software in small steps with constant feedback.",
        "example": "Scrum sprints every two weeks.",
        "why_it_matters": "Industry standard for modern development teams."
    },
    {
        "category": "swe",
        "term": "REST API",
        "difficulty": 2,
        "formal_definition": "A REST API follows the Representational State Transfer architecture using stateless communication and resource-based URIs.",
        "simple_definition": "API that follows consistent HTTP rules.",
        "example": "GET /users/123",
        "why_it_matters": "Most backend systems use REST."
    },
    {
        "category": "swe",
        "term": "Unit Test",
        "difficulty": 2,
        "formal_definition": "A unit test verifies the correctness of a small, isolated piece of code such as a function or class method.",
        "simple_definition": "Test for a single function.",
        "example": "Test add(2,3) == 5",
        "why_it_matters": "Prevents bugs early."
    },
    {
        "category": "swe",
        "term": "Version Control",
        "difficulty": 2,
        "formal_definition": "Version control systems track and manage changes to code over time.",
        "simple_definition": "Tracks history of code changes.",
        "example": "Git commits and branches.",
        "why_it_matters": "Enables collaboration and rollback."
    },
    {
        "category": "swe",
        "term": "OOP",
        "difficulty": 2,
        "formal_definition": "Object-Oriented Programming is a paradigm organized around objects containing data and behavior.",
        "simple_definition": "Programming using classes and objects.",
        "example": "A Car class with attributes and methods.",
        "why_it_matters": "Common approach for organizing complex systems."
    },
    {
        "category": "swe",
        "term": "Refactoring",
        "difficulty": 2,
        "formal_definition": "Refactoring improves internal code structure without changing its observable behavior.",
        "simple_definition": "Cleaning up code.",
        "example": "Renaming variables or simplifying logic.",
        "why_it_matters": "Improves maintainability."
    },
    {
        "category": "swe",
        "term": "Design Pattern",
        "difficulty": 2,
        "formal_definition": "Design patterns are reusable solutions to common software architecture problems.",
        "simple_definition": "Reusable coding solutions.",
        "example": "Singleton, Observer, Factory.",
        "why_it_matters": "Standardized solutions reduce errors."
    },
    {
        "category": "swe",
        "term": "API Endpoint",
        "difficulty": 2,
        "formal_definition": "An endpoint is a specific URL route where an API exposes functionality.",
        "simple_definition": "A specific API URL.",
        "example": "POST /login",
        "why_it_matters": "Defines how clients interact with servers."
    },
    {
        "category": "swe",
        "term": "Continuous Integration",
        "difficulty": 2,
        "formal_definition": "Continuous Integration automatically builds and tests source code whenever changes are committed.",
        "simple_definition": "Automatically test code on every change.",
        "example": "GitHub Actions running tests on every PR.",
        "why_it_matters": "Reduces integration failures."
    },
    {
        "category": "swe",
        "term": "Code Review",
        "difficulty": 2,
        "formal_definition": "Code review is the peer review process of inspecting code for correctness, style, and security.",
        "simple_definition": "Checking each other’s code.",
        "example": "Reviewing a PR on GitHub.",
        "why_it_matters": "Improves quality and consistency."
    },

    # ---------------------- Difficulty 3 ----------------------
    {
        "category": "swe",
        "term": "SOLID Principles",
        "difficulty": 3,
        "formal_definition": "SOLID is a set of five object-oriented design principles that promote maintainability, scalability, and clean architecture.",
        "simple_definition": "Five rules for writing clean OOP code.",
        "example": "Single Responsibility: each class should do one thing.",
        "why_it_matters": "A core interview and coding best practice topic."
    },
    {
        "category": "swe",
        "term": "Technical Debt",
        "difficulty": 3,
        "formal_definition": "Technical debt is the cost of rework caused by choosing short-term, fast solutions instead of long-term maintainable ones.",
        "simple_definition": "Shortcuts that cause future problems.",
        "example": "Hard-coded logic instead of configs.",
        "why_it_matters": "Affects long-term productivity and stability."
    },
    {
        "category": "swe",
        "term": "System Design Basics",
        "difficulty": 3,
        "formal_definition": "System design is the process of defining architecture, components, interactions, and data flows in a scalable system.",
        "simple_definition": "Designing how a big system works.",
        "example": "Designing a scalable quiz API.",
        "why_it_matters": "Required for backend and full-stack interviews."
    },
    {
        "category": "swe",
        "term": "Concurrency",
        "difficulty": 3,
        "formal_definition": "Concurrency is the ability of a system to run multiple tasks overlapping in time.",
        "simple_definition": "Handling multiple things at once.",
        "example": "Async requests in FastAPI.",
        "why_it_matters": "Critical for high-performance apps."
    },

    # ---------------------- Difficulty 4 ----------------------
    {
        "category": "swe",
        "term": "Scalability",
        "difficulty": 4,
        "formal_definition": "Scalability is a system's ability to handle increased workload by adding resources horizontally or vertically.",
        "simple_definition": "Can your system handle more users?",
        "example": "Auto-scaling API servers in AWS.",
        "why_it_matters": "Core requirement for production systems."
    },
    {
        "category": "swe",
        "term": "Idempotency",
        "difficulty": 4,
        "formal_definition": "Idempotency ensures that repeated requests produce the same result without additional side effects.",
        "simple_definition": "Doing something once or many times gives the same outcome.",
        "example": "PUT /user/123 should not create duplicates.",
        "why_it_matters": "Critical for reliable APIs."
    },
    {
        "category": "swe",
        "term": "CQRS",
        "difficulty": 4,
        "formal_definition": "CQRS (Command Query Responsibility Segregation) separates read and write operations into different models.",
        "simple_definition": "Separate models for reading and writing data.",
        "example": "Read replicas for queries, master node for writes.",
        "why_it_matters": "Improves performance and maintainability."
    },
    {
        "category": "swe",
        "term": "Load Balancing",
        "difficulty": 4,
        "formal_definition": "Load balancing distributes incoming traffic across multiple servers to ensure reliability and performance.",
        "simple_definition": "Spreads traffic across servers.",
        "example": "AWS ALB distributing traffic to API servers.",
        "why_it_matters": "Prevents overload and downtime."
    },

    # ---------------------- Difficulty 5 ----------------------
    {
        "category": "swe",
        "term": "Distributed Systems",
        "difficulty": 5,
        "formal_definition": "Distributed systems are systems with multiple components running on different machines that work together as one.",
        "simple_definition": "One system spread across many machines.",
        "example": "Microservices communicating over gRPC.",
        "why_it_matters": "Senior-level interview essential."
    },
    {
        "category": "swe",
        "term": "CAP Theorem",
        "difficulty": 5,
        "formal_definition": "CAP Theorem states that in a distributed system you can only guarantee two of three: Consistency, Availability, Partition Tolerance.",
        "simple_definition": "You can't have all three: consistency, uptime, and partition safety.",
        "example": "AP systems like DynamoDB prioritize availability.",
        "why_it_matters": "Guides architecture decisions for large-scale systems."
    }
]
