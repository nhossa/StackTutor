raw_question_block = """
What is Linux and difference between UNIX and Linux?
What is the Linux kernel?
What are inodes in Linux?
Explain the Linux boot process
What is a zombie process?
Difference between soft links and hardlinks?
What are namespaces and c-groups?
What are symbolic links?
What are the different types of permissions in Linux?
What is swap space?
What is chmod, chown and chgrp in Linux?
What are cronjobs?
Commands (basic & advanced):
What does chmod +x FILENAME do?
Which command will show you free/used memory?
Which command will show me the current directory I am in?
How can I terminate an on going process?
Write the command that will display all .yaml files including permissions of each file? ()
How can I found the status of a process?
What is the command to show all open ports?
How do you find the process ID of a running process in Linux?
How do you find the dependencies of a package in Linux?
Advanced:
Does free memory exist on Linux?
How can I check if a server is down?
What is inside /proc?
A process on the system can no longer log files, what can I do?
What is LILO?
What are syscalls in Linux and how do they work?
What is no route to host?
What is the difference between a hard link and a symbolic link in Linux? (WITH hands-on example)
Linux Internals & Advanced (Scenario based questions):
Explain the linux boot process (detailed)
A process on the system can no longer log files, how would you debug?
How can I check if a Linux system is healthy?
What happens when you type "ls" or "cd" into a terminal? (go deep and talk about what happens behind the scenes - kernel level)
How can I check if a server is down?
How are Linux processes killed on a lower level?
I have accidentally entered `cd/bin` and done `chmod 644 chmod` - how can I fix this?
How would you troubleshoot a network connectivity issue in Linux?
How do you troubleshoot a connectivity issue with a remote server in Linux?
How do you view and edit the system logs in Linux?
Which command do you use to copy one file from one server to another?
Which command do you use to copy directories from one server to another?
🔹 Networking
What is HTTP?
Difference between HTTP and HTTPS?
How does a typical HTTP request look like?
What is an HTTP method?
What are HTTP request headers?
What is in an HTTP request body?
What is in an HTTP response?
What’s an HTTP status code?
What are HTTP response headers?
What is in an HTTP response body?
TCP vs UDP
What is DNS?
How does DNS work?
What is TLS?
What are CIDR ranges?
What is ingress and egress traffic?
What is a switch vs a hub?
What is a switch vs a router?
What is HTTPS vs Websockets?
Explain how a 3 way handshake works?
Stateless vs Stateful firewalls?
What are VPCs?
What is subnetting?
What is DHCP?
Advanced + Scenario based questions:
When I type google.com into the browser, what actually happens? (basic version)
I can't reach a website, how can I troubleshoot? (use deep Linux + networking knowledge)
Can you break down the OSI model and what does it signify?
How does mTLS work and compare it to TLS?
Describe the TCP/IP connection process?
When and why would one use a TCP over UDP?
Data transfer between 2 hosts is extremely slow. How can you troubleshoot?
🔹 Git
What is Git?
Difference between Git and SVN?
What is the basic Git workflow?
Difference between git pull and Git fetch
What is git cherry-pick?
What is the HEAD in Git?
When do I use Git stash?
What does git reset do?
What is Git fork? What is difference between git fork, clone and branch?
What is difference between `git stash pop` and `git stash apply`?
Advanced:
I need to update my local repos, what commands do I use?
I need to rollback to a previous commit and I don't need my recent changes, what do I use?
How can I amend an older commit?
What is the command to check the difference between two commits?
When do you use `git rebase` instead of `git merge`?
Do you know how to undo a git rebase?
How do you bring down updates from main branch if your local branch becomes stale?
🔹 AWS
-----General--------
What is AWS?
What are two services of AWS where you could store secrets?
What is the relation between the Availability Zone and Region in AWS?
What is auto-scaling?
What services can help minimise a DDoS attack?
What is an AMI?
What are different types of load balancers?
-----Networking-----
What is a VPC?
How do Subnets work?
What network object do you need to allow a server ingress from the internet?
How can your resources in the VPC get access to the internet?
-----Scenario-based-----
I want to create a 3 Tier Architecture. Can you explain step by step of how I can go about this?
In VPC with private and public subnets, database servers should ideally be launched into which subnet?
What are some security best practices for EC2s?
I created a web application with autoscaling. I observed that the traffic on my application is the highest on Wednesdays and Fridays between 9 AM and 7 PM. What would be the best solution for me to handle the scaling?
You have an application running on your Amazon EC2 instance. You want to reduce the load on your instance as soon as the CPU utilization reaches 100 percent. How will you do that?
-----Others-----
Name some managed runtimes for Lambda
🔹 Azure
What is Azure?
What are ARM templates in Azure?
What is Azure CDN?
How is Azure App Service different from Azure Functions?
How to define an Environment Variable on Azure using Azure CLI?
How would you choose between Azure Blob Storage vs. Azure File Service?
What is difference between Keys and Secrets in Azure Key Vault?
What’s the difference between Azure SQL Database and Azure SQL Managed Instance?
When should we use Azure Table Storage over Azure SQL?
Explain what is the difference between Block Blobs, Append Blobs and Page Blobs in Azure?
Advanced:
What to use: many small Azure Storage Blob containers vs one really large container with tons of blobs?
🔹 Terraform
What is IaC? What is Terraform?
What is Terraform state?
What are most common Terraform commands?
What is Terraform backend?
What are modules in Terraform?
What is Terragrunt?
Explain the workflow of the core Terraform?
Difference between Terraform, AWS CloudFormation and Azure ARM?
What is the difference between Terraform and Ansible?
What are provisioners in Terraform?
How can two people using the Terraform cloud can create two different sets of infrastructure using the same working directory?
What is a null resource in Terraform?
Which command is used to perform syntax validation on terraform configuration files?
How can I format my current directory of Terraform config files in the HCP format?
Advanced:
I have 3 people in my team who want to work on the same AWS Infrastructure on Terraform as well as same state. What can I do to ensure there are no clashes?
In a pipeline, where would you store the Terraform state?
Can I test my terraform modules? If so, how can I test them? Is there a common framework used to Terraform modules?
How does state file locking work?
What is Checkov?
How can I use Terraform in a pipeline?
How can one export data from one module to another?
How can you import existing resources under Terraform management?
Which command can be used to reconcile the Terraform state with the actual real-world infrastructure?
What are some best practices when using Terraform modules?
How do you handle secrets and sensitive data in Terraform?
What are some best practices when writing Terraform code?
How do you export data from one module to another?
🔹 Docker & K8s
Container (Docker):
What is a container and what are its fundamentals?
What are c-groups and namespaces in Linux?
What is Docker and how does it work?
What is a container and what are its fundamentals?
What are c-groups and namespaces in Linux?
What is Docker and how does it work?
When do I use Docker Compose vs Docker Swarm and K8s?
What is a Dockerfile used for?
Can you explain the basic components of a Dockerfile?
What is a FROM in a Dockerfile used for?
What is a COPY in a Dockerfile used for?
What is a ADD in a Dockerfile used for?
What is a CMD & ENTRTPOINT in a Dockerfile used for?
How is a container different from a virtual machine?
How can I run a container?
How can I stop and remove a container?
How can I attach a shell to a terminal of a running container?
What is a dangling image?
What is Docker compose and when is it used?
Advanced:
What is the difference between COPY and ADD commands in a Dockerfile?
What is the difference between CMD and RUN commands in a Dockerfile?
What are some best practices to follow when running containers in production?
Name some limitations of containers vs VMs
Is it good practice to run stateful applications in containers?
Is it possible to generate a Dockerfile from an image
$ docker history --no-trunc <IMAGE_ID>
How does virtualisation work at a lower level?
What is an orphant volume? And how can you remove it?
When you limit the memory for a container, does it reserve that memory for the container?
What is the difference between Docker RUN, CMD and ENTRYPOINT?
What is the difference between "expose" and "publish" in Docker?
How do containers work at a lower level?
Container Orchestration (Kubernetes = K8s):
What is Kubernetes?
What problems does Kubernetes solve?
What is the difference between Docker and K8s?
What are the core components of the control plane and data plane? What are the components used for?
What is a Pod and what does it do?
How can containers within a pod communicate with each other?
What is a K8s cluster ?
What are deployments?
What are stateful sets?
How do you restrict pod-to-pod communication in a cluster?
How can I rollback a deployment?
What are namespaces?
What is the role of the kube-apiserver?
Advanced:
Take me through a full cycle of an app deployment from code to an app running on a pod/deployment.
Can you mention some good practices to follow when creating containers?
Can you explain a simple K8s cluster architecture and the components within it?
What happens when a master node fails?
What happens when a worker node fails?
What is an Ingress controller?
How can one build a highly availabe (HA) cluster in K8s?
What is the role of ETCD in K8s?
Explain what are Taints and Tolerations in K8s?
🔹 Ansible
What is Ansible?
How does Ansible work?
What is Ansible Galaxy?
What are Ansible handlers?
What is Ansible Vault?
What aer Ansible collections?
How do you get a list of Ansible predefined variables?
How is Ansible playbook different from ad-hoc commands?
What is the recommended for securing secret information used within Ansible playbooks?
What templating language is directly supported within Ansible for creating dynamic playbooks?
What protocol does Ansible use for communicating with client systems?
What is an inventory file?
Advanced:
Can you name some Ansible best practices?
How do you handle errors in Ansible?
How do you test your Ansible roles and tasks?
What is Molecule and how does it works?
🔹 CI/CD
What is meant by Continuous Integration?
Explain blue-green deployment
What is a CI/CD pipeline?
What is a canary deployment?
What is a rolling deployment?
🔹 DevOps methodology, practices, & Agile
What is meant by continuous integratons?
What are the advantages of DevOps?
Can you describe some branching strategies you have used?
What is the blue/green deployment pattern?
System Design
🔹 CDN & Caching
What is a CDN and why would I use one?
What are CDN edge servers?
How does CDN caching work?
What is cache invalidation?
What are some cache invalidation methods?
What is a cache Hit?
What is a cache Miss?
Can you explain a caching workflow?
Explain why CDN availability may be a problem for using WebSockets?
What are some best practices for caching?
What is the CAP Theorem?
What is a Partition in CAP theorem?
What are A and P in CAP theorem and the difference between them?
Explain when CA is used and when CP is used?
Explain the difference between horizontal scaling and vertical scaling?
Difference between forward proxy and reverse proxy?
What is Load Balancing and how does it work? How does it relate to reverse proxies?
Name me some common load balancers
What is a microservice architecture and when would I consider using one?
🔹 API Design
What is an API?
What is REST?
What is a RESTful API?
What is a RESTful Web Service?
What is a RESTful Web API?
What is a RESTful Web Application?
What is API design?
What is API documentation?
What are the core components of a HTTP request?
What are the core components of a HTTP response?
What is a cached response?
What is the difference between a HTTP GET and POST request?
What is the difference between a HTTP PUT and PATCH request?
What is the difference between a HTTP 301 and 302 response?
What is the difference between a HTTP 401 and 403 response?
What is the difference between a HTTP 404 and 410 response?
What is the difference between a HTTP 500 and 503 response?
What is the difference between a HTTP 200 and 201 response?
What is payload?
What is a HTTP header?
What is a HTTP body?
Explain cache-control header?
Name some best practices for better RESTful API design?
🔹 Databases
What is a database?
What is DBMS (Database Management System)?
What is the schema referred to in a Database?
What are different types of databases?
Advantages & Disadvantages of using relational databases?
Advantages & Disadvantages of using NoSQL relational databases?
What is a key-value database? What are some examples of this?
What are graph databases? Name some examples?
What is database replication?
What is master-slave replication? And what is master-master replication?
What is Synchronous vs Asynchronous replication?
What are indexes in databases?
How can one improve query performance by using index hunting?
What do you understand by ‘Atomicity’ and ‘Aggregation’?
What is database partitioning?
What is database sharding?
Advanced:
What are message queues? And what are message brokers?
How does the publish-subscribe model work?
Can you explain how an event-driven architecture works?
What is an API Gateway? How is this different from load balancers?
Explain why CDN (in)availability may be a problem for using WebSockets?
Software Engineering
🔹 General
What are some ways that you can version an API?
What does it mean for an API to be idempotent?
How can you implement idempotency in APIs?
What are some ways you could authenticate an API?
What are benefits of working with circuit breakers?
Define cascading failures and how to deal with those?
How can you deploy an API without disrupting traffic?
Explain what a Race condition is to a 5 year old?
🔹 Golang
What is Go?
Why was the Go langauge created?
What is a pointer?
What is the difference between the = and := operator?
What are goroutines?
Does Go have exceptions?
Can you return multiple values from a function?
What is a channel?
What is a struct?
What is a slice?
What is a map?
What is a method?
What is a package?
What is a module?
What is a pointer?
What is a pointer receiver?
How to check if a Map contains a key in Go?
When is the init() function run?
Advanced:
Implement a function that reverses a slice of integers?
What are generics and how do they work?
🔹 Python
🔹 Java
What is JVM?
What is JRE?
What is JDK?
What is the difference between JDK and JRE?
What is the difference between JVM and JRE?
How does a HashMap work in Java?
What is the difference between an Interface and an Abstract class?
How does Garbage Collection work in Java?
How does Garbage Collection prevent a Java application from going out of memory?
What is the difference between a stack and a heap?
What's a deadlock?
What is the difference between an ArrayList and a LinkedList?
Does Java support multiple inheritance?
What is the difference between == and .equals()?
Explain marshalling and unmarshalling?
🔹 JavaScript
What is TypeScript?
What are the differences between TypeScript and JavaScript?
Why use TypeScript?
What are the advantages of TypeScript?
What are Types in TypeScript?
What are Type Assertions in TypeScript?
What are the Primitive data types?
What are the special data types in TypeScript?
What are interfaces in TypeScript?
Interfaces Vs Types?
Data
Data Modelling and Schemas:
Define data modelling and the benefits of implementing a data model?
What are some of the design schemas used when performing data modelling?
What are the three types of data models?
What is a table (entity) and column (attribute)?
What is normalisation/denormalisation and what is its purpose?
What are the main relationships which can be found in a data model? (name 3)
Explain the two different types of design schemas (snowflake and star)?
What is a data mart?
How would you describe granularity?
How does data sparcity impact aggregation of data sets/sources?
In the context of data modelling, what is the importance of metadata? How would you describe the role of metadata in data modelling?
What is a DDL script?
What is a fact and dimension?
What is an ERD? Entity relationship diagram?
What are the differences between foreign and surrogate keys?
Desribe cardinality
Data Architect
Please state an example of designing, creating, deploying and managing an end to end data architecture project?
What are the fundamental skills required for a data architect?
What is a data block and a data file?
What is data warehousing?
What are the main differences between 'a view' and 'a materialised view'?
What is a junk dimension?
Please explain in detail data warehousing architecture
What are the different types of integrity constraints?
Why do data architects enforce and monitor data compliance standards in data systems?
Differentiate between OTLP and OLAP
How do you design and implement a data warehouse?
How do you handle data quality issues?
How do you optimise data models for performance?
Describe your familiarity with big data technologies such as Hadoop and Spark
How do you go about gathering requirements for a new data project?
How do you hamdle conflicting priorities when working on multiple projects?
Which software and design patterns are you familiar with?
Data Engineering
What made you choose data engineering and what does it mean to you?
How would you define data engineering?
What is the difference between a data architect and a data engineer?
What are data engineers responsible for?
What is the difference between structured ,semi structured and unstructured data?
Describe differences between a data warehouse and an operational database
How would you increase the revenue of a business using data analytics and big data?
What are the advantages of using skewed tables in Hive?
Explain the hive data model and its components
Why is using a distributed system important in hadoop?
Name the core features of hadoop
Define hadoop streaming
What is data locality?
What does Context object do in Hadoop and why is it important?
Name the three reducer phases in hadoop
What do args and kwargs commands do?
List the differences between tuples and lists
What are the advantages of working with big data on the cloud?
Can you describe what happens when a data block is corrupted?
How would you explain file permissions in hadoop?
Which process would you follow to add a node to a cluster?
Can you list python libraries which can facilitate efficient data processing?
What challenges came up during your recent project, and how did you overcome these challenges?
Have you ever transformed unstructured data into structured data? and how did you do it?
Can you tell me about NameNode? What happens if NameNode crashes or comes to an end?
How to achieve security in Hadoop?
What is FIFO Scheduling?
SQL
How can you deal with duplicate data points in an SQL query?
List objects that are created via the CREATE statement in SQL
How would you see the database structure in SQL?
How would you search for a specific string in a column?
What are the differences between DDL, DML and DCL?
Difference between SQL and MySQL?
How is a RDBMS different to a DBMS?
What is a self join? name other join commands
What is the SELECT statement?
What are the CRUD commands?
What are UNION, MINUS and INTERSECT commands?
How would you load data into tables using SQL?
What is PostgreSQL?
Explain the character manipulation functions in SQL
What is the difference between RANK and DENSE_RANK() functions?
What are tables and fields?r
What is a schema in a SQL server?
How would you create a table with 4 columns
What is a CASE statment?
Summarise differences between SQL and NoSQL
Difference between NOW() and CURRENT_DATE()
What is a BLOB and TEXT in MySQL?
How do you remove duplicate rows in SQL?
How do you create a stored in procedure in SQL?
What is the difference between CHAR, VARCHAR datatypes in SQL?
What are constraints in SQL?
Differences in DELETE and TRUNCATE statements?
What is data integrity?
What do you understand by query optimisation?
What are entities and relationships?
Name some aggregate functions which are commonly used in SQL
What are the syntax and use of the COALESCE function?
What is the ACID property in a database?
What is a “Trigger” in SQL?
What is a subquery in SQL?
What is a CLAUSE in SQL?
What is the need for a MERGE statement?
How can you fetch common records from two tables?
What are aggregate and scalar functions?
What are Views used for?
What are Local and Global variables?
ETL & Data Pipelines & more
How would I go about troubleshooting pipelines?
Machine Learning
Cyber Security & Info Security
What is a firewall, and how does it work?
What is a vulnerability assessment, and how is it different from a penetration test?
What is encryption, and how is it used in cybersecurity?
What is a Denial of Service (DoS) attack, and how does it work?
What is phishing, and how can you identify and prevent it?
What is a DDoS attack and how does it work?
What is the CIA triad and why is it important in cyber security?
What is the difference between a virus and a worm?
What is multi-factor authentication and why is it important?
What is social engineering, and how can it be prevented?
What is the difference between symmetric and asymmetric encryption?
What is an intrusion detection system (IDS), and how does it work?
What is a security information and event management (SIEM) system, and how does it work?
What is a honeypot and how is it used in cybersecurity?
What is a man-in-the-middle attack and how can it be prevented?
What is the difference between IDS and IPS?
How is Encryption different from Hashing?
What is a three-way handshake?
CWhat are the response codes that can be received from a Web Application?
Explain SSL Encryption?
Explain Data Leakage?
What are some of the common Cyberattacks?
What are salted hashes?
What is Port Scanning?
Encryption and Authentication
What is a three-way handshake?
How do cookies work?
How do sessions work?
Explain how OAuth works.
What is a public key infrastructure flow and how would I diagram it?
Describe the difference between synchronous and asynchronous encryption.
Describe SSL handshake.
How does HMAC work?
Why HMAC is designed in that way?
What is the difference between authentication vs authorization name spaces?
What’s the difference between Diffie-Hellman and RSA?
How does Kerberos work?
If you're going to compress and encrypt a file, which do you do first and why?
How do I authenticate you and know you sent the message?
Should you encrypt all data at rest?
What is Perfect Forward Secrecy?
OWASP Top 10, Pentesting and/or Web Applications
Differentiate XSS from CSRF.
What do you do if a user brings you a pc that is acting 'weird'? You suspect malware.
What is the difference between tcp dump and FWmonitor?
Do you know what XXE is?
Explain man-in-the-middle attacks.
What is a Server Side Request Forgery attack?
Describe what are egghunters and their use in exploit development.
How is pad lock icon in browser generated?
What is Same Origin Policy and CORS?
Compliance
Can you explain SOC 2?
What are the five trust criteria?
How is ISO27001 different?
Can you list examples of controls these frameworks require?
What is the difference between Governance, Risk and Compliance?
What does Zero Trust mean?
What is role-based access control (RBAC) and why is it covered by compliance frameworks?
What is the NIST framework and why is it influential?
What is the OSI model?
"""
