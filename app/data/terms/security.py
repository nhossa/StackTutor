security = [

    # ---------------------- Difficulty 1 ----------------------
    {
        "category": "security",
        "term": "What is cybersecurity?",
        "difficulty": 1,
        "formal_definition": "Cybersecurity is the practice of protecting systems, networks, and data from digital attacks.",
        "simple_definition": "Keeping computers and data safe from attacks.",
        "example": "Using antivirus, firewalls, and secure passwords.",
        "why_it_matters": "All modern systems require protection from threats."
    },

    # ---------------------- Difficulty 2 ----------------------
    {
        "category": "security",
        "term": "IAM",
        "difficulty": 2,
        "formal_definition": "Identity and Access Management is the framework that defines and enforces who can access which resources.",
        "simple_definition": "Controls who can access what.",
        "example": "AWS IAM roles and policies.",
        "why_it_matters": "Prevents unauthorized access to sensitive systems."
    },
    {
        "category": "security",
        "term": "Encryption",
        "difficulty": 2,
        "formal_definition": "Encryption transforms data into unreadable ciphertext using algorithms and keys.",
        "simple_definition": "Scrambles data so only the right person can read it.",
        "example": "PGP-encrypted emails.",
        "why_it_matters": "Protects sensitive data at rest and in transit."
    },
    {
        "category": "security",
        "term": "Firewall",
        "difficulty": 2,
        "formal_definition": "A firewall monitors and filters network traffic based on predefined security rules.",
        "simple_definition": "A barrier that blocks unwanted traffic.",
        "example": "Blocking port 22 from the public internet.",
        "why_it_matters": "Prevents many common network attacks."
    },
    {
        "category": "security",
        "term": "2FA",
        "difficulty": 2,
        "formal_definition": "Two-Factor Authentication requires two separate identity verification methods.",
        "simple_definition": "Requires two proofs to log in.",
        "example": "Password + SMS code.",
        "why_it_matters": "Significantly reduces account takeover attacks."
    },
    {
        "category": "security",
        "term": "Zero Trust",
        "difficulty": 2,
        "formal_definition": "Zero Trust is a security model where no user or device is trusted by default.",
        "simple_definition": "Always verify, trust nothing.",
        "example": "Requiring authentication even for internal services.",
        "why_it_matters": "Minimizes lateral movement in breaches."
    },
    {
        "category": "security",
        "term": "Penetration Testing",
        "difficulty": 2,
        "formal_definition": "A controlled simulation of cyberattacks to identify weaknesses.",
        "simple_definition": "Ethically hacking your own systems.",
        "example": "Hiring white-hat testers to attack an app.",
        "why_it_matters": "Reveals vulnerabilities before attackers find them."
    },
    {
        "category": "security",
        "term": "Malware",
        "difficulty": 2,
        "formal_definition": "Malware is software intentionally designed to disrupt, damage, or gain unauthorized access to systems.",
        "simple_definition": "Harmful software.",
        "example": "Ransomware encrypting your files.",
        "why_it_matters": "One of the most common sources of data breaches."
    },
    {
        "category": "security",
        "term": "Phishing",
        "difficulty": 2,
        "formal_definition": "Phishing is a social engineering attack that manipulates users into revealing sensitive information.",
        "simple_definition": "Tricking people into giving login info.",
        "example": "Fake email from 'Apple Support' asking for a password.",
        "why_it_matters": "Most breaches start with phishing."
    },
    {
        "category": "security",
        "term": "DDoS Attack",
        "difficulty": 2,
        "formal_definition": "A Distributed Denial of Service attack overwhelms a target with traffic from multiple compromised systems.",
        "simple_definition": "Flooding a system until it crashes.",
        "example": "Botnets sending millions of fake requests.",
        "why_it_matters": "Can take down sites and services."
    },
    {
        "category": "security",
        "term": "SSL/TLS",
        "difficulty": 2,
        "formal_definition": "SSL/TLS are cryptographic protocols used to secure communication over networks.",
        "simple_definition": "Encrypts traffic on the web.",
        "example": "HTTPS connections.",
        "why_it_matters": "Protects online privacy and integrity."
    },

    # ---------------------- Difficulty 3 ----------------------
    {
        "category": "security",
        "term": "Least Privilege",
        "difficulty": 3,
        "formal_definition": "The principle of granting users and applications only the minimum access required to perform their tasks.",
        "simple_definition": "Give only the access needed, nothing more.",
        "example": "A Lambda function only allowed S3:GetObject.",
        "why_it_matters": "Limits damage in case of compromise."
    },
    {
        "category": "security",
        "term": "Hashing",
        "difficulty": 3,
        "formal_definition": "Hashing converts data into a fixed-length value that cannot be feasibly reversed.",
        "simple_definition": "One-way scrambling of data.",
        "example": "Storing passwords as bcrypt hashes.",
        "why_it_matters": "Essential for secure credential storage."
    },
    {
        "category": "security",
        "term": "SQL Injection",
        "difficulty": 3,
        "formal_definition": "An attack that injects malicious SQL statements into input fields to manipulate the database.",
        "simple_definition": "Attacking a database using unsafe input.",
        "example": "' OR 1=1 --",
        "why_it_matters": "One of the most common critical vulnerabilities."
    },
    {
        "category": "security",
        "term": "XSS (Cross-Site Scripting)",
        "difficulty": 3,
        "formal_definition": "A vulnerability where attackers inject malicious scripts into websites viewed by others.",
        "simple_definition": "Injecting JavaScript into a web page.",
        "example": "<script>alert('hacked')</script>",
        "why_it_matters": "Allows credential theft and session hijacking."
    },
    {
        "category": "security",
        "term": "CSRF (Cross-Site Request Forgery)",
        "difficulty": 3,
        "formal_definition": "An attack that forces a user to perform unwanted actions on a web application where they are authenticated.",
        "simple_definition": "Tricking a user into making a request they didn’t intend.",
        "example": "A hidden form that triggers money transfers.",
        "why_it_matters": "Can perform unauthorized actions on behalf of users."
    },
    {
        "category": "security",
        "term": "Access Tokens",
        "difficulty": 3,
        "formal_definition": "Tokens represent user authentication and authorization, typically short-lived and digitally signed.",
        "simple_definition": "Temporary proof of login.",
        "example": "JWTs in API authentication.",
        "why_it_matters": "Critical for modern stateless authentication."
    },

    # ---------------------- Difficulty 4 ----------------------
    {
        "category": "security",
        "term": "mTLS",
        "difficulty": 4,
        "formal_definition": "Mutual TLS is a protocol where both the client and server authenticate each other's certificates.",
        "simple_definition": "Both sides verify identity using certificates.",
        "example": "Service-to-service authentication in microservices.",
        "why_it_matters": "Prevents impersonation inside distributed systems."
    },
    {
        "category": "security",
        "term": "Secret Management",
        "difficulty": 4,
        "formal_definition": "The practice of securely storing, rotating, and accessing sensitive values like API keys and passwords.",
        "simple_definition": "Safely storing things like API keys.",
        "example": "AWS Secrets Manager or HashiCorp Vault.",
        "why_it_matters": "Improper secret storage causes massive breaches."
    },
    {
        "category": "security",
        "term": "Network Segmentation",
        "difficulty": 4,
        "formal_definition": "Dividing networks into isolated segments to limit the spread of attacks.",
        "simple_definition": "Breaking a network into smaller secure pieces.",
        "example": "Production network separate from development.",
        "why_it_matters": "Greatly reduces blast radius of attacks."
    },
    {
        "category": "security",
        "term": "Incident Response",
        "difficulty": 4,
        "formal_definition": "The structured approach for handling and mitigating security breaches or attacks.",
        "simple_definition": "How teams respond to security incidents.",
        "example": "Detection → Containment → Eradication → Recovery.",
        "why_it_matters": "Determines how quickly damage is controlled."
    },

    # ---------------------- Difficulty 5 ----------------------
    {
        "category": "security",
        "term": "Threat Modeling",
        "difficulty": 5,
        "formal_definition": "Threat modeling identifies potential threats, vulnerabilities, and attack paths in a system.",
        "simple_definition": "Planning for what could go wrong.",
        "example": "STRIDE model in system design.",
        "why_it_matters": "Used by senior engineers to design secure systems."
    },
    {
        "category": "security",
        "term": "Zero-Day Exploits",
        "difficulty": 5,
        "formal_definition": "Zero-day exploits take advantage of vulnerabilities unknown to the vendor.",
        "simple_definition": "Attacks that exploit bugs no one knows about yet.",
        "example": "Chrome or Windows zero-day attacks.",
        "why_it_matters": "These attacks are extremely dangerous and hard to defend against."
    }
]
