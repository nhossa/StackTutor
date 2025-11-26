api_design = [

    # ---------------------- Difficulty 1 ----------------------
    {
        "category": "api_design",
        "term": "What is an API?",
        "difficulty": 1,
        "formal_definition": "An API is a defined interface that allows software systems to interact by exposing functions, operations, or data.",
        "simple_definition": "A way for different apps or services to talk to each other.",
        "example": "Your weather app calling an API to get today's temperature.",
        "why_it_matters": "APIs power communication between all modern systems."
    },
    {
        "category": "api_design",
        "term": "What is a HTTP request?",
        "difficulty": 1,
        "formal_definition": "A HTTP request is a structured message sent from a client to a server requesting an action or data.",
        "simple_definition": "A message your browser or app sends to a server.",
        "example": "GET /users/123",
        "why_it_matters": "Understanding requests is essential for all backend work."
    },
    {
        "category": "api_design",
        "term": "What is a HTTP response?",
        "difficulty": 1,
        "formal_definition": "A HTTP response is a server message that includes a status code, headers, and optional payload.",
        "simple_definition": "What the server sends back after your request.",
        "example": "200 OK with JSON user data.",
        "why_it_matters": "Every API interaction returns a response."
    },

    # ---------------------- Difficulty 2 ----------------------
    {
        "category": "api_design",
        "term": "What is REST?",
        "difficulty": 2,
        "formal_definition": "REST is an architectural style emphasizing statelessness, uniform interfaces, and resource-based modeling.",
        "simple_definition": "Rules for designing predictable, clean APIs.",
        "example": "GET /books to retrieve a list of books.",
        "why_it_matters": "Most modern APIs follow REST principles."
    },
    {
        "category": "api_design",
        "term": "What is a RESTful API?",
        "difficulty": 2,
        "formal_definition": "A RESTful API conforms to REST by using HTTP semantics, URIs for resources, and stateless interactions.",
        "simple_definition": "An API built using REST rules.",
        "example": "GET /orders, POST /orders",
        "why_it_matters": "RESTful design is expected in backend interviews."
    },
    {
        "category": "api_design",
        "term": "What is a payload?",
        "difficulty": 2,
        "formal_definition": "The payload is the body content of a HTTP request or response that carries actual application data.",
        "simple_definition": "The data you're sending or receiving.",
        "example": "{\"email\": \"naim@example.com\"}",
        "why_it_matters": "APIs revolve around payload structure and validation."
    },
    {
        "category": "api_design",
        "term": "What is a HTTP header?",
        "difficulty": 2,
        "formal_definition": "Headers are metadata fields that describe the request or response context, such as content type, auth, and caching.",
        "simple_definition": "Extra information sent with requests and responses.",
        "example": "Authorization: Bearer <token>",
        "why_it_matters": "Headers control auth, caching, formats, and security."
    },

    # ---------------------- Difficulty 3 ----------------------
    {
        "category": "api_design",
        "term": "What is API design?",
        "difficulty": 3,
        "formal_definition": "API design is defining endpoints, data models, behavior, validations, error formats, and versioning to ensure a consistent interface.",
        "simple_definition": "Planning how your API works and behaves.",
        "example": "Designing POST /orders and GET /orders/{id}.",
        "why_it_matters": "Good design avoids breaking users and scales long-term."
    },
    {
        "category": "api_design",
        "term": "Components of a HTTP request",
        "difficulty": 3,
        "formal_definition": "A HTTP request has a method, URL, headers, query params, and optional body.",
        "simple_definition": "Method, URL, headers, params, body.",
        "example": "POST /login with JSON body.",
        "why_it_matters": "Used for building and debugging APIs."
    },
    {
        "category": "api_design",
        "term": "Components of a HTTP response",
        "difficulty": 3,
        "formal_definition": "A HTTP response contains a status code, response headers, and an optional payload.",
        "simple_definition": "Status code, headers, returned data.",
        "example": "201 Created with new user JSON.",
        "why_it_matters": "Defines the contract for API consumers."
    },
    {
        "category": "api_design",
        "term": "Cache-Control header",
        "difficulty": 3,
        "formal_definition": "Cache-Control specifies how long and where responses can be cached using directives like max-age, no-store, private, and public.",
        "simple_definition": "Controls how long and where responses are cached.",
        "example": "Cache-Control: max-age=3600",
        "why_it_matters": "Caching reduces latency and server load."
    },
    {
        "category": "api_design",
        "term": "Difference between GET and POST",
        "difficulty": 3,
        "formal_definition": "GET retrieves resources and is idempotent, while POST submits data and may create or modify state.",
        "simple_definition": "GET = fetch. POST = create or send data.",
        "example": "GET /users vs POST /users",
        "why_it_matters": "Essential for building proper RESTful APIs."
    },
    {
        "category": "api_design",
        "term": "Difference between PUT and PATCH",
        "difficulty": 3,
        "formal_definition": "PUT fully replaces a resource; PATCH applies partial updates.",
        "simple_definition": "PUT = replace all. PATCH = update part.",
        "example": "PATCH /users/1 {\"email\": \"new@x.com\"}",
        "why_it_matters": "Common interview question about REST semantics."
    },

    # ---------------------- Difficulty 4 ----------------------
    {
        "category": "api_design",
        "term": "Idempotency",
        "difficulty": 4,
        "formal_definition": "Idempotency ensures that making the same request multiple times has the same effect as making it once.",
        "simple_definition": "Doing something once or many times gives the same result.",
        "example": "DELETE /users/1 is idempotent.",
        "why_it_matters": "Critical for reliability, especially in payment systems."
    },
    {
        "category": "api_design",
        "term": "Idempotency keys",
        "difficulty": 4,
        "formal_definition": "Clients send a unique idempotency key to prevent duplicate processing of non-idempotent operations like POST.",
        "simple_definition": "A token to ensure a POST request isn’t run twice.",
        "example": "Stripe uses Idempotency-Key for charges.",
        "why_it_matters": "Prevents duplicate orders, payments, or writes."
    },
    {
        "category": "api_design",
        "term": "Pagination",
        "difficulty": 4,
        "formal_definition": "Pagination divides large datasets into smaller chunks using limit/offset or cursor-based systems.",
        "simple_definition": "Returning big lists in smaller pages.",
        "example": "/users?limit=20&page=2",
        "why_it_matters": "Prevents performance issues and massive payload sizes."
    },
    {
        "category": "api_design",
        "term": "Rate limiting",
        "difficulty": 4,
        "formal_definition": "Rate limiting restricts how many requests a client may make in a given time window.",
        "simple_definition": "Limits how fast clients can call your API.",
        "example": "100 requests/min",
        "why_it_matters": "Prevents abuse and protects backend services."
    },
    {
        "category": "api_design",
        "term": "Throttling",
        "difficulty": 4,
        "formal_definition": "Throttling slows down or spaces out requests from a client to control load.",
        "simple_definition": "Slows down high traffic instead of blocking it completely.",
        "example": "Streaming APIs use throttling.",
        "why_it_matters": "Important for fair use and system protection."
    },
    {
        "category": "api_design",
        "term": "Difference between 401 and 403",
        "difficulty": 4,
        "formal_definition": "401 means authentication required or failed; 403 means authenticated but lacking permissions.",
        "simple_definition": "401 = login required. 403 = not allowed.",
        "example": "403 for admin-only pages.",
        "why_it_matters": "Fundamental to API security and debugging."
    },
    {
        "category": "api_design",
        "term": "Difference between 500 and 503",
        "difficulty": 4,
        "formal_definition": "500 is an unexpected server error; 503 indicates temporary unavailability or overload.",
        "simple_definition": "500 = server broke. 503 = server busy/unavailable.",
        "example": "503 during deployment.",
        "why_it_matters": "Common real-world outage root causes."
    },
    {
        "category": "api_design",
        "term": "Circuit breaker pattern",
        "difficulty": 4,
        "formal_definition": "A resilience pattern where failing services are temporarily blocked to prevent cascading failures.",
        "simple_definition": "Stop calling a failing service until it's healthy again.",
        "example": "Netflix Hystrix breaking calls to unhealthy microservices.",
        "why_it_matters": "Prevents total system collapse."
    },
    {
        "category": "api_design",
        "term": "Retries and exponential backoff",
        "difficulty": 4,
        "formal_definition": "Retries resubmit failed requests; exponential backoff increases wait time between retries to avoid overload.",
        "simple_definition": "Retrying with increasing delays.",
        "example": "AWS SDK retry strategy.",
        "why_it_matters": "Essential for distributed systems reliability."
    },
    {
        "category": "api_design",
        "term": "Stateless vs Stateful APIs",
        "difficulty": 4,
        "formal_definition": "Stateless APIs don’t store client session data; stateful APIs maintain session information server-side.",
        "simple_definition": "Stateless = no memory of previous requests.",
        "example": "REST = stateless; traditional sessions = stateful.",
        "why_it_matters": "Scalability depends on statelessness."
    },
    {
        "category": "api_design",
        "term": "Best practices for RESTful API design",
        "difficulty": 4,
        "formal_definition": "Includes resource modeling, correct HTTP verbs, versioning, pagination, consistent errors, security, and caching.",
        "simple_definition": "Use clean URLs, correct methods, versioning, pagination.",
        "example": "/v1/orders?page=1",
        "why_it_matters": "Defines production-quality APIs."
    },
    {
        "category": "api_design",
        "term": "API versioning",
        "difficulty": 4,
        "formal_definition": "Supporting multiple API versions to prevent breaking changes and ensure backward compatibility.",
        "simple_definition": "Keeping old and new API versions running safely.",
        "example": "/v1/orders vs /v2/orders",
        "why_it_matters": "Prevents breaking millions of clients."
    },

    # ---------------------- Difficulty 5 (Advanced) ----------------------
    {
        "category": "api_design",
        "term": "OAuth2",
        "difficulty": 5,
        "formal_definition": "OAuth2 is an authorization framework enabling third-party apps to access user resources without sharing passwords.",
        "simple_definition": "A secure way to let apps access your data.",
        "example": "Login with Google.",
        "why_it_matters": "Required knowledge for secure API design."
    },
    {
        "category": "api_design",
        "term": "JWT",
        "difficulty": 5,
        "formal_definition": "JSON Web Tokens are signed, encoded tokens used to represent claims for authentication and authorization.",
        "simple_definition": "A token that proves who you are.",
        "example": "Authorization: Bearer <jwt>",
        "why_it_matters": "Standard method for stateless auth."
    },
    {
        "category": "api_design",
        "term": "API Gateway",
        "difficulty": 5,
        "formal_definition": "An API gateway acts as a single entry point for clients, providing routing, auth, throttling, caching, monitoring, and transformations.",
        "simple_definition": "A front door for all your APIs.",
        "example": "AWS API Gateway.",
        "why_it_matters": "Essential for microservices architecture."
    },
    {
        "category": "api_design",
        "term": "OpenAPI / Swagger",
        "difficulty": 5,
        "formal_definition": "OpenAPI is a specification for describing REST APIs, and Swagger provides tooling for documentation, validation, and testing.",
        "simple_definition": "A standard for documenting APIs.",
        "example": "FastAPI auto-generates OpenAPI docs.",
        "why_it_matters": "Clear documentation accelerates development."
    },
    {
        "category": "api_design",
        "term": "Webhooks",
        "difficulty": 5,
        "formal_definition": "Webhooks push real-time events from a service to a client-defined URL when certain conditions occur.",
        "simple_definition": "Your server gets notified automatically when something happens.",
        "example": "Stripe webhook on payment success.",
        "why_it_matters": "Used for real-time event-driven integrations."
    },
    {
        "category": "api_design",
        "term": "Contract Testing",
        "difficulty": 5,
        "formal_definition": "Contract testing ensures that API providers and consumers agree on request/response formats and behavior.",
        "simple_definition": "Ensures both sides agree on the API format.",
        "example": "Pact testing between microservices.",
        "why_it_matters": "Avoids breaking downstream clients."
    },
    {
        "category": "api_design",
        "term": "GraphQL vs REST",
        "difficulty": 5,
        "formal_definition": "GraphQL allows flexible queries for exactly the needed data, unlike REST's predefined endpoints.",
        "simple_definition": "GraphQL lets clients ask for exactly what they want.",
        "example": "query { user(id:1) { name email } }",
        "why_it_matters": "Increasingly used in modern APIs."
    },
    {
        "category": "api_design",
        "term": "gRPC",
        "difficulty": 5,
        "formal_definition": "gRPC is a high-performance RPC framework using HTTP/2 and Protocol Buffers.",
        "simple_definition": "A very fast way services call each other.",
        "example": "Internal microservice communication at Google.",
        "why_it_matters": "Crucial for microservice architectures."
    },
    {
        "category": "api_design",
        "term": "API deprecation strategy",
        "difficulty": 5,
        "formal_definition": "Defines how old API versions are phased out using sunset headers, migration guides, and timed removal.",
        "simple_definition": "The process of retiring old versions safely.",
        "example": "GitHub announces v3 deprecation 1 year in advance.",
        "why_it_matters": "Critical for long-term API evolution."
    }
]
