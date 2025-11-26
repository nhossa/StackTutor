docker_kubernetes = [
    {
        "category": "docker-kubernetes",
        "term": "What is a container and what are its fundamentals?",
        "difficulty": 3,
        "formal_definition": "A container is a lightweight, isolated environment that packages an application with all its dependencies using Linux primitives such as namespaces and cgroups.",
        "simple_definition": "A lightweight isolated environment to run apps.",
        "example": "Running a FastAPI app inside a container.",
        "why_it_matters": "Containers are the foundation of modern DevOps and cloud deployments."
    },
    {
        "category": "docker-kubernetes",
        "term": "What are cgroups and namespaces?",
        "difficulty": 4,
        "formal_definition": "Namespaces isolate process views (PIDs, mounts, networking), and cgroups limit resource usage (CPU, memory, IO) in Linux.",
        "simple_definition": "Namespaces isolate; cgroups control resource limits.",
        "example": "Docker isolates containers via namespaces and limits memory via cgroups.",
        "why_it_matters": "They power container isolation and efficiency."
    },
    {
        "category": "docker-kubernetes",
        "term": "What is Docker and how does it work?",
        "difficulty": 3,
        "formal_definition": "Docker is a container platform that builds, ships, and runs applications using layered file systems and Linux isolation mechanisms.",
        "simple_definition": "A tool to build and run containers.",
        "example": "Building an image with a Dockerfile and running it with docker run.",
        "why_it_matters": "Docker is the standard for packaging applications."
    },
    {
        "category": "docker-kubernetes",
        "term": "When to use Docker Compose vs Docker Swarm vs Kubernetes?",
        "difficulty": 4,
        "formal_definition": "Compose is for local multi-container apps; Swarm manages small clusters; Kubernetes orchestrates production-scale clusters.",
        "simple_definition": "Compose = local; Swarm = small clusters; K8s = large production clusters.",
        "example": "Compose for dev, Kubernetes for cloud-scale apps.",
        "why_it_matters": "Choosing the right tool prevents over-engineering."
    },
    {
        "category": "docker-kubernetes",
        "term": "What is a Dockerfile and what is it used for?",
        "difficulty": 2,
        "formal_definition": "A Dockerfile is a declarative file specifying how to build a Docker image.",
        "simple_definition": "A file that defines how to build an image.",
        "example": "FROM python:3.10-slim",
        "why_it_matters": "Every containerized app starts with a Dockerfile."
    },
    {
        "category": "docker-kubernetes",
        "term": "Basic components of a Dockerfile",
        "difficulty": 2,
        "formal_definition": "Dockerfile instructions include FROM, COPY, RUN, CMD, ENTRYPOINT, EXPOSE, and more.",
        "simple_definition": "The building blocks of an image.",
        "example": "RUN pip install -r requirements.txt",
        "why_it_matters": "Understanding these is essential to build images correctly."
    },
    {
        "category": "docker-kubernetes",
        "term": "COPY vs ADD",
        "difficulty": 4,
        "formal_definition": "COPY simply copies files; ADD can also extract archives and pull remote URLs.",
        "simple_definition": "ADD does more but COPY is safer.",
        "example": "COPY app/ /app",
        "why_it_matters": "Misusing ADD introduces security risks."
    },
    {
        "category": "docker-kubernetes",
        "term": "RUN vs CMD vs ENTRYPOINT",
        "difficulty": 4,
        "formal_definition": "RUN executes commands when building the image. CMD defines the default runtime command. ENTRYPOINT defines the core container process.",
        "simple_definition": "RUN = build time; CMD = default runtime; ENTRYPOINT = fixed runtime.",
        "example": "ENTRYPOINT [\"python\"]",
        "why_it_matters": "Common cause of broken or inflexible containers."
    },
    {
        "category": "docker-kubernetes",
        "term": "EXPOSE vs PUBLISH",
        "difficulty": 4,
        "formal_definition": "EXPOSE documents a port inside the image; PUBLISH (-p) maps a container port to the host.",
        "simple_definition": "EXPOSE is metadata; -p exposes it externally.",
        "example": "docker run -p 8000:8000 image",
        "why_it_matters": "Critical to debugging networking issues."
    },
    {
        "category": "docker-kubernetes",
        "term": "Dangling image",
        "difficulty": 3,
        "formal_definition": "A dangling image is an untagged image layer not referenced by any container.",
        "simple_definition": "Leftover, unused images.",
        "example": "docker images -f dangling=true",
        "why_it_matters": "They waste disk space."
    },
    {
        "category": "docker-kubernetes",
        "term": "Stateful apps in containers",
        "difficulty": 4,
        "formal_definition": "Containers are ephemeral, so stateful workloads require external volumes or specialized orchestration like StatefulSets.",
        "simple_definition": "Containers shouldn’t hold important data.",
        "example": "Postgres running in K8s StatefulSet.",
        "why_it_matters": "Prevents data loss."
    },
    {
        "category": "docker-kubernetes",
        "term": "Docker Compose",
        "difficulty": 3,
        "formal_definition": "A tool to define and run multi-container apps using a YAML file.",
        "simple_definition": "Run multiple containers together.",
        "example": "docker-compose up",
        "why_it_matters": "Essential for local development."
    },
    {
        "category": "docker-kubernetes",
        "term": "What is Kubernetes?",
        "difficulty": 3,
        "formal_definition": "Kubernetes is a container orchestration platform that automates deployment, scaling, and management of containerized applications.",
        "simple_definition": "A system to manage containers on clusters.",
        "example": "Running services on EKS or GKE.",
        "why_it_matters": "Industry standard for production workloads."
    },
    {
        "category": "docker-kubernetes",
        "term": "Problems Kubernetes solves",
        "difficulty": 3,
        "formal_definition": "Kubernetes handles scheduling, scaling, networking, self-healing, and rollout automation.",
        "simple_definition": "It manages lots of containers automatically.",
        "example": "Pods restart when they crash.",
        "why_it_matters": "Core to modern cloud architecture."
    },
    {
        "category": "docker-kubernetes",
        "term": "Control plane vs data plane",
        "difficulty": 4,
        "formal_definition": "Control plane includes kube-apiserver, etcd, controller-manager, scheduler. Data plane includes kubelet, kube-proxy, and pods.",
        "simple_definition": "Control = brains; data = workers.",
        "example": "Scheduler assigns pods to nodes.",
        "why_it_matters": "You must know this for any Kubernetes role."
    },
    {
        "category": "docker-kubernetes",
        "term": "What is a Pod?",
        "difficulty": 3,
        "formal_definition": "A Pod is the smallest deployable unit consisting of one or more tightly coupled containers.",
        "simple_definition": "The smallest unit in Kubernetes.",
        "example": "A pod running a FastAPI container.",
        "why_it_matters": "Everything in K8s runs inside Pods."
    },
    {
        "category": "docker-kubernetes",
        "term": "Container communication inside Pods",
        "difficulty": 3,
        "formal_definition": "Containers inside a pod share the same network namespace and can communicate over localhost.",
        "simple_definition": "Containers talk via localhost.",
        "example": "Sidecar pattern.",
        "why_it_matters": "Key for multi-container design."
    },
    {
        "category": "docker-kubernetes",
        "term": "Kubernetes cluster",
        "difficulty": 2,
        "formal_definition": "A cluster consists of master (control plane) and worker nodes running pods.",
        "simple_definition": "Machines that run Kubernetes.",
        "example": "EKS cluster with 3 worker nodes.",
        "why_it_matters": "Basic conceptual foundation."
    },
    {
        "category": "docker-kubernetes",
        "term": "Deployment",
        "difficulty": 3,
        "formal_definition": "A controller that manages replica sets and rolling updates.",
        "simple_definition": "Controls how pods are updated.",
        "example": "Rolling update from v1 to v2.",
        "why_it_matters": "Fundamental K8s resource."
    },
    {
        "category": "docker-kubernetes",
        "term": "StatefulSet",
        "difficulty": 4,
        "formal_definition": "A Kubernetes workload object that manages stateful applications with stable network IDs and persistent storage.",
        "simple_definition": "For apps that need stable storage.",
        "example": "Running a database in K8s.",
        "why_it_matters": "Essential for persistent workloads."
    },
    {
        "category": "docker-kubernetes",
        "term": "Restrict pod-to-pod communication",
        "difficulty": 4,
        "formal_definition": "NetworkPolicies define allowed ingress and egress traffic between pods.",
        "simple_definition": "Use NetworkPolicies to limit traffic.",
        "example": "Only backend pod can talk to database pod.",
        "why_it_matters": "Critical for cluster security."
    },
    {
        "category": "docker-kubernetes",
        "term": "Rollback a deployment",
        "difficulty": 3,
        "formal_definition": "Kubernetes stores ReplicaSet history and can revert to an older version using kubectl rollout undo.",
        "simple_definition": "Undo a bad release.",
        "example": "kubectl rollout undo deployment/api",
        "why_it_matters": "Prevents long production outages."
    },
    {
        "category": "docker-kubernetes",
        "term": "Namespaces",
        "difficulty": 3,
        "formal_definition": "Kubernetes namespaces logically isolate resources inside a cluster.",
        "simple_definition": "Groups resources by environment or team.",
        "example": "dev, staging, production namespaces.",
        "why_it_matters": "Required for multi-team clusters."
    },
    {
        "category": "docker-kubernetes",
        "term": "kube-apiserver role",
        "difficulty": 4,
        "formal_definition": "The kube-apiserver is the central control plane component managing the Kubernetes API and communication.",
        "simple_definition": "The brain of Kubernetes.",
        "example": "All kubectl commands go through it.",
        "why_it_matters": "Core knowledge for interviews."
    },
    {
        "category": "docker-kubernetes",
        "term": "Ingress controller",
        "difficulty": 4,
        "formal_definition": "Ingress controllers manage HTTP/HTTPS traffic into the cluster.",
        "simple_definition": "Routes external traffic into services.",
        "example": "NGINX ingress routing traffic to pods.",
        "why_it_matters": "Required for production networking."
    },
    {
        "category": "docker-kubernetes",
        "term": "ETCD role",
        "difficulty": 4,
        "formal_definition": "ETCD is a distributed key-value store used by Kubernetes to store cluster state.",
        "simple_definition": "Stores all cluster data.",
        "example": "Pod states, config, secrets.",
        "why_it_matters": "If etcd dies, the cluster dies."
    },
    {
        "category": "docker-kubernetes",
        "term": "Taints and Tolerations",
        "difficulty": 4,
        "formal_definition": "Mechanisms to control pod scheduling by allowing or preventing pods from running on specific nodes.",
        "simple_definition": "Rules for what pods run on what nodes.",
        "example": "Dedicated nodes for GPU workloads.",
        "why_it_matters": "Cluster scheduling mastery."
    }
]
