networking = [

    # ------------------ CORE NETWORK MODELS ------------------
    {
        "category": "networking",
        "term": "OSI Model",
        "formal_definition": "A conceptual seven-layer framework describing how network systems communicate from physical transmission to application-level interactions.",
        "simple_definition": "A 7-layer model explaining how data moves through a network.",
        "example": "HTTP operates at Layer 7; TCP at Layer 4.",
        "difficulty": 2,
        "why_it_matters": "Critical for diagnosing and designing network systems."
    },
    {
        "category": "networking",
        "term": "TCP/IP Model",
        "formal_definition": "A four-layer practical networking model used by real internet communication systems.",
        "simple_definition": "The real-world networking model used by the internet.",
        "example": "DNS, HTTP, TLS all sit on top of TCP/IP.",
        "difficulty": 2,
        "why_it_matters": "Foundation of the modern internet."
    },

    # ------------------ IP, ROUTING, ADDRESSES ------------------
    {
        "category": "networking",
        "term": "Subnetting",
        "formal_definition": "The practice of dividing a network into smaller logical segments, each with its own address space.",
        "simple_definition": "Splitting a network into smaller networks.",
        "example": "10.0.0.0/24 split into four /26 subnets.",
        "difficulty": 3,
        "why_it_matters": "Improves security, routing, and network performance."
    },
    {
        "category": "networking",
        "term": "CIDR",
        "formal_definition": "Classless Inter-Domain Routing expresses IP ranges using a prefix length to improve flexibility and efficiency.",
        "simple_definition": "A compact way of describing IP ranges.",
        "example": "192.168.1.0/24",
        "difficulty": 3,
        "why_it_matters": "Used everywhere in cloud networking (VPCs, routing)."
    },
    {
        "category": "networking",
        "term": "NAT",
        "formal_definition": "Network Address Translation modifies IP headers so many private hosts can share a single public IP.",
        "simple_definition": "Allows many devices to share one public IP.",
        "example": "Home routers use NAT.",
        "difficulty": 2,
        "why_it_matters": "Essential for IPv4 scarcity and security."
    },

    # ------------------ CORE DEVICES ------------------
    {
        "category": "networking",
        "term": "Switch",
        "formal_definition": "A device that forwards traffic within a LAN using MAC address tables.",
        "simple_definition": "Connects devices on the same network.",
        "example": "Office ethernet switch connecting all PCs.",
        "difficulty": 2,
        "why_it_matters": "Fundamental for LAN design."
    },
    {
        "category": "networking",
        "term": "Router",
        "formal_definition": "A device that forwards packets between different networks using IP routing.",
        "simple_definition": "Connects different networks together.",
        "example": "Home WiFi router connects LAN → internet.",
        "difficulty": 2,
        "why_it_matters": "Core of all modern networking."
    },
    {
        "category": "networking",
        "term": "VLAN",
        "formal_definition": "A Virtual LAN creates separate logical networks on the same physical switch.",
        "simple_definition": "Virtual separation inside a single network.",
        "example": "Guest WiFi in a separate VLAN from staff devices.",
        "difficulty": 2,
        "why_it_matters": "Improves segmentation and security."
    },

    # ------------------ DNS ------------------
    {
        "category": "networking",
        "term": "DNS",
        "formal_definition": "The Domain Name System resolves human-readable domain names into IP addresses.",
        "simple_definition": "Turns website names into IP addresses.",
        "example": "www.google.com → 142.250.72.206",
        "difficulty": 2,
        "why_it_matters": "Without DNS, the internet breaks."
    },
    {
        "category": "networking",
        "term": "How DNS Works",
        "formal_definition": "DNS queries progress from local cache → resolver → root → TLD → authoritative server to retrieve an IP address.",
        "simple_definition": "The step-by-step lookup process to resolve a domain.",
        "example": "Recursive query to resolve facebook.com.",
        "difficulty": 3,
        "why_it_matters": "Understanding DNS is essential for debugging failures."
    },

    # ------------------ DHCP ------------------
    {
        "category": "networking",
        "term": "DHCP",
        "formal_definition": "Dynamic Host Configuration Protocol automatically assigns IP addresses and network parameters to devices.",
        "simple_definition": "Automatically gives devices IP addresses.",
        "example": "Laptop joins WiFi and receives an IP automatically.",
        "difficulty": 2,
        "why_it_matters": "Used everywhere in modern networking."
    },

    # ------------------ INTERNET SECURITY ------------------
    {
        "category": "networking",
        "term": "Firewall",
        "formal_definition": "A device or software that filters network packets based on security rules.",
        "simple_definition": "Blocks or allows network traffic.",
        "example": "AWS Security Groups filter inbound/outbound traffic.",
        "difficulty": 2,
        "why_it_matters": "First line of network defense."
    },
    {
        "category": "networking",
        "term": "Stateful vs Stateless Firewall",
        "formal_definition": "Stateful firewalls track connection state; stateless firewalls inspect packets individually.",
        "simple_definition": "Stateful remembers connections; stateless treats every packet alone.",
        "example": "AWS NACL = stateless; Security Groups = stateful.",
        "difficulty": 3,
        "why_it_matters": "Critical for cloud security design."
    },

    # ------------------ PROTOCOLS ------------------
    {
        "category": "networking",
        "term": "HTTP",
        "formal_definition": "Hypertext Transfer Protocol enabling communication between browsers and servers.",
        "simple_definition": "How browsers request websites.",
        "example": "GET /home HTTP/1.1",
        "difficulty": 2,
        "why_it_matters": "Backbone of web communication."
    },
    {
        "category": "networking",
        "term": "HTTPS",
        "formal_definition": "Secure HTTP using TLS to encrypt communication.",
        "simple_definition": "Encrypted version of HTTP.",
        "example": "https://google.com",
        "difficulty": 2,
        "why_it_matters": "Protects user data and prevents MITM attacks."
    },
    {
        "category": "networking",
        "term": "TLS",
        "formal_definition": "Transport Layer Security encrypts network data to ensure privacy and integrity.",
        "simple_definition": "Encryption protocol used by HTTPS.",
        "example": "TLS handshake before HTTPS browsing.",
        "difficulty": 3,
        "why_it_matters": "Essential for secure internet communication."
    },
    {
        "category": "networking",
        "term": "mTLS",
        "formal_definition": "Mutual TLS authenticates both client and server using certificates.",
        "simple_definition": "TLS but both sides prove who they are.",
        "example": "Service-to-service authentication in microservices.",
        "difficulty": 4,
        "why_it_matters": "Used in zero-trust architectures."
    },

    # ------------------ TCP / UDP ------------------
    {
        "category": "networking",
        "term": "TCP vs UDP",
        "formal_definition": "TCP provides reliable, ordered delivery; UDP provides fast, connectionless, best-effort delivery.",
        "simple_definition": "TCP = reliable. UDP = fast.",
        "example": "TCP: web browsing. UDP: video streaming.",
        "difficulty": 3,
        "why_it_matters": "Core networking interview topic."
    },
    {
        "category": "networking",
        "term": "TCP 3-Way Handshake",
        "formal_definition": "TCP establishes connections via SYN → SYN-ACK → ACK, allowing reliable communication.",
        "simple_definition": "How TCP creates a connection.",
        "example": "Client opens TCP connection to server.",
        "difficulty": 3,
        "why_it_matters": "Must-know for backend and DevOps roles."
    },

    # ------------------ LOAD BALANCING ------------------
    {
        "category": "networking",
        "term": "Load Balancer",
        "formal_definition": "Distributes incoming traffic across multiple servers to increase reliability and reduce latency.",
        "simple_definition": "Spreads traffic across servers.",
        "example": "AWS ELB balancing traffic to EC2s.",
        "difficulty": 2,
        "why_it_matters": "Prevents overload; enables scaling."
    },
    {
        "category": "networking",
        "term": "Ingress vs Egress Traffic",
        "formal_definition": "Ingress refers to inbound traffic; egress refers to outbound traffic.",
        "simple_definition": "Ingress = incoming. Egress = outgoing.",
        "example": "Ingress rules allow inbound HTTPS.",
        "difficulty": 2,
        "why_it_matters": "Used heavily in cloud networking rules."
    },

    # ------------------ WEB SOCKETS ------------------
    {
        "category": "networking",
        "term": "HTTPS vs WebSockets",
        "formal_definition": "HTTPS uses request/response; WebSockets allow full-duplex real-time communication.",
        "simple_definition": "HTTPS = one-way request/response. WebSockets = real-time two-way.",
        "example": "Chat apps use WebSockets.",
        "difficulty": 3,
        "why_it_matters": "Critical for real-time applications."
    },

    # ------------------ CLOUD NETWORKING ------------------
    {
        "category": "networking",
        "term": "VPC",
        "formal_definition": "Virtual Private Cloud is an isolated virtual network within cloud providers.",
        "simple_definition": "Your own private network in the cloud.",
        "example": "AWS VPC with public and private subnets.",
        "difficulty": 3,
        "why_it_matters": "Foundational cloud concept."
    },

    # ------------------ TROUBLESHOOTING ------------------
    {
        "category": "networking",
        "term": "No Route to Host",
        "formal_definition": "An error indicating that the system has no valid network path to the target host.",
        "simple_definition": "Your machine doesn’t know how to reach the server.",
        "example": "Firewall blocking outbound traffic.",
        "difficulty": 3,
        "why_it_matters": "Common real-world failure."
    },
    {
        "category": "networking",
        "term": "I can't reach a website — troubleshooting steps",
        "formal_definition": "Troubleshooting includes checking DNS, routing, firewall rules, ports, and server health.",
        "simple_definition": "Step-by-step debugging when a site won’t load.",
        "example": "ping → dig → traceroute → curl",
        "difficulty": 4,
        "why_it_matters": "Real-world DevOps problem-solving skill."
    },
    {
        "category": "networking",
        "term": "Slow data transfer troubleshooting",
        "formal_definition": "Diagnosing slowness involves checking bandwidth, latency, congestion, packet loss, and server load.",
        "simple_definition": "Find why data is moving slowly.",
        "example": "iperf tests between hosts.",
        "difficulty": 4,
        "why_it_matters": "Performance engineers must know this."
    },

    # ------------------ FULL NETWORK LIFECYCLE ------------------
    {
        "category": "networking",
        "term": "What happens when you type google.com?",
        "formal_definition": "Full lifecycle: DNS lookup → TCP handshake → TLS handshake → HTTP request → server response → rendering.",
        "simple_definition": "Step-by-step explanation of how a webpage loads.",
        "example": "Browser resolves DNS before sending HTTP.",
        "difficulty": 4,
        "why_it_matters": "A famous system design interview question."
    }

]
