cdn_caching = [
    # ---------------------- Difficulty 1 ----------------------
    {
        "category": "cdn-caching",
        "term": "What is a CDN?",
        "difficulty": 1,
        "formal_definition": "A CDN (Content Delivery Network) is a geographically distributed network of servers that deliver content faster by caching it closer to end users.",
        "simple_definition": "A network of servers that makes websites load faster.",
        "example": "Serving images through Cloudflare CDN instead of your origin server.",
        "why_it_matters": "Almost every high-traffic website uses a CDN for speed, cost reduction, and reliability."
    },
    {
        "category": "cdn-caching",
        "term": "What is caching?",
        "difficulty": 1,
        "formal_definition": "Caching stores copies of frequently accessed data to reduce latency and load on the origin system.",
        "simple_definition": "Saving data temporarily so future requests are faster.",
        "example": "Returning a cached API response instead of recomputing it.",
        "why_it_matters": "Caching is one of the most powerful performance techniques in system design."
    },
    {
        "category": "cdn-caching",
        "term": "What is a cache hit?",
        "difficulty": 1,
        "formal_definition": "A cache hit occurs when the requested data is found in the cache instead of being fetched from the origin.",
        "simple_definition": "When the data you want is already cached.",
        "example": "Cloudflare serving an image directly without contacting your server.",
        "why_it_matters": "High cache hit ratios drastically reduce server load."
    },

    # ---------------------- Difficulty 2 ----------------------
    {
        "category": "cdn-caching",
        "term": "What is a cache miss?",
        "difficulty": 2,
        "formal_definition": "A cache miss occurs when the requested data is not found in the cache and must be retrieved from the origin.",
        "simple_definition": "When the cache doesn’t have the data, so the server must fetch it.",
        "example": "The first request after deployment results in a cache miss.",
        "why_it_matters": "Cache misses increase latency and backend load."
    },
    {
        "category": "cdn-caching",
        "term": "How does CDN caching work?",
        "difficulty": 2,
        "formal_definition": "A CDN caches static or cacheable content on edge servers. When a user requests content, the CDN serves it from the nearest edge if available, or fetches from the origin if not.",
        "simple_definition": "The CDN saves content on servers around the world and serves it without hitting your backend.",
        "example": "CloudFront caching /static/logo.png globally.",
        "why_it_matters": "CDN caching is critical for performance, scalability, and cost reduction."
    },
    {
        "category": "cdn-caching",
        "term": "What are CDN edge servers?",
        "difficulty": 2,
        "formal_definition": "Edge servers are distributed nodes within a CDN that store cached content geographically closer to users.",
        "simple_definition": "Servers close to users that deliver cached content.",
        "example": "A user in Japan receives assets from a Tokyo CDN edge node.",
        "why_it_matters": "Edge servers are the foundation of modern, low-latency content delivery."
    },
    {
        "category": "cdn-caching",
        "term": "What is cache invalidation?",
        "difficulty": 2,
        "formal_definition": "Cache invalidation is the process of removing or updating cached content so users receive fresh, correct data.",
        "simple_definition": "Refreshing or deleting outdated cached data.",
        "example": "Purging the CDN cache when a new website version is deployed.",
        "why_it_matters": "Incorrect invalidation causes stale data bugs and user confusion."
    },

    # ---------------------- Difficulty 3 ----------------------
    {
        "category": "cdn-caching",
        "term": "What are cache invalidation methods?",
        "difficulty": 3,
        "formal_definition": "Common cache invalidation methods include time-based expiration (TTL), manual purge, cache-busting via versioned URLs, and conditional validation with ETags or Last-Modified headers.",
        "simple_definition": "Different ways to update or clear cached content.",
        "example": "Using logo-v2.png to force the CDN to fetch a new file.",
        "why_it_matters": "Good invalidation strategy prevents stale data without overloading servers."
    },
    {
        "category": "cdn-caching",
        "term": "Explain a caching workflow",
        "difficulty": 3,
        "formal_definition": "A standard caching workflow is: request → CDN checks edge cache → if hit, respond → if miss, fetch from origin → CDN stores response → return to user.",
        "simple_definition": "CDN tries cache first, then the server, then caches the result.",
        "example": "Cloudflare fetching an uncached HTML file and storing it for future users.",
        "why_it_matters": "Understanding this is essential for debugging cache behavior."
    },
    {
        "category": "cdn-caching",
        "term": "Why CDN availability can affect WebSockets",
        "difficulty": 3,
        "formal_definition": "Many CDNs do not fully support WebSockets at edge nodes due to the persistent connection requirement, causing issues when routing through CDN layers.",
        "simple_definition": "CDNs may not support or may interfere with long-lived WebSocket connections.",
        "example": "CloudFront historically didn't support WebSockets at all.",
        "why_it_matters": "Choosing the wrong CDN setup breaks real-time applications."
    },
    {
        "category": "cdn-caching",
        "term": "Best practices for caching",
        "difficulty": 3,
        "formal_definition": "Best practices include using appropriate TTLs, versioned assets, avoiding cache for dynamic content, using ETags, compressing content, and monitoring cache hit ratios.",
        "simple_definition": "Use TTL, versioning, and proper headers to avoid stale or un-cached data.",
        "example": "Setting Cache-Control: max-age=3600, immutable.",
        "why_it_matters": "Correct caching massively improves performance and lowers cost."
    },

    # ---------------------- Difficulty 4 ----------------------
    {
        "category": "cdn-caching",
        "term": "What is the CAP Theorem?",
        "difficulty": 4,
        "formal_definition": "CAP Theorem states that a distributed system cannot simultaneously provide Consistency, Availability, and Partition Tolerance. It can only guarantee two of the three.",
        "simple_definition": "Distributed systems must choose two: Consistency, Availability, or Partition Tolerance.",
        "example": "AP systems (like DNS) prioritize availability over strict consistency.",
        "why_it_matters": "System design heavily depends on which trade-offs you choose."
    },
    {
        "category": "cdn-caching",
        "term": "What is a Partition in CAP?",
        "difficulty": 4,
        "formal_definition": "A network partition occurs when communication between distributed nodes breaks, causing the system to split into isolated segments.",
        "simple_definition": "When parts of a distributed system can't reach each other.",
        "example": "A failed network link between two data centers.",
        "why_it_matters": "Partitions are inevitable; systems must be designed to handle them."
    },
    {
        "category": "cdn-caching",
        "term": "Difference between A and P in CAP",
        "difficulty": 4,
        "formal_definition": "Availability means every request gets a response, even if stale. Partition Tolerance means the system continues functioning despite network failures.",
        "simple_definition": "A = always respond; P = keep working even if the network breaks.",
        "example": "AP systems return stale cached data instead of failing.",
        "why_it_matters": "Choosing A or C under partitions is the core system design decision."
    },
    {
        "category": "cdn-caching",
        "term": "Explain when CA vs CP is used",
        "difficulty": 4,
        "formal_definition": "CA systems prioritize consistency and availability but break under partitions. CP systems maintain consistency under partitions but may sacrifice availability.",
        "simple_definition": "CA = no partitions allowed; CP = choose consistency during failures.",
        "example": "CA: single-node SQL. CP: MongoDB configured for consistency.",
        "why_it_matters": "Picking the wrong model leads to outages or bad data."
    },
    {
        "category": "cdn-caching",
        "term": "Horizontal vs vertical scaling",
        "difficulty": 4,
        "formal_definition": "Vertical scaling adds more power (CPU/RAM) to a single machine; horizontal scaling adds more machines to distribute load.",
        "simple_definition": "Vertical = bigger machine; Horizontal = more machines.",
        "example": "Adding 8 more servers behind a CDN is horizontal scaling.",
        "why_it_matters": "Scaling strategy defines system cost, reliability, and performance."
    },
    {
        "category": "cdn-caching",
        "term": "Forward proxy vs reverse proxy",
        "difficulty": 4,
        "formal_definition": "A forward proxy sits in front of clients and controls outbound traffic; a reverse proxy sits in front of servers and controls inbound traffic.",
        "simple_definition": "Forward = protects client; Reverse = protects server.",
        "example": "Nginx as a reverse proxy for your backend API.",
        "why_it_matters": "Reverse proxies are fundamental to load balancers, CDNs, and caching."
    },
    {
        "category": "cdn-caching",
        "term": "Load balancing and relation to reverse proxies",
        "difficulty": 4,
        "formal_definition": "Load balancers distribute traffic across multiple servers and often act as reverse proxies to manage routing, health checks, and failover.",
        "simple_definition": "Load balancers spread traffic; many are reverse proxies too.",
        "example": "An ALB routing requests to a fleet of EC2 instances.",
        "why_it_matters": "Scalable systems fundamentally require load balancers."
    },
    {
        "category": "cdn-caching",
        "term": "Common load balancers",
        "difficulty": 4,
        "formal_definition": "Examples include Nginx, HAProxy, AWS ALB, AWS NLB, Azure Load Balancer, Cloudflare Load Balancer, and Traefik.",
        "simple_definition": "Popular load balancers used in industry.",
        "example": "Using HAProxy for round-robin traffic distribution.",
        "why_it_matters": "Load balancing is foundational for system reliability and scaling."
    },
    {
        "category": "cdn-caching",
        "term": "What is microservice architecture?",
        "difficulty": 4,
        "formal_definition": "Microservices break applications into small, independent services that communicate over APIs, improving scalability and independent deployment.",
        "simple_definition": "Building an app as many small services instead of one big one.",
        "example": "Auth, billing, and notifications as separate services behind an API gateway.",
        "why_it_matters": "Most modern distributed systems use microservices, CDNs, and caching together."
    }
]
