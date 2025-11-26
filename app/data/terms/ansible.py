ansible = [
    {
        "category": "ansible",
        "term": "What is Ansible?",
        "difficulty": 3,
        "formal_definition": "Ansible is an open-source automation tool used for configuration management, application deployment, and orchestration. It uses a declarative YAML-based language and operates agentlessly over SSH or WinRM.",
        "simple_definition": "A tool that automates server setup and deployments without needing agents installed.",
        "example": "Using an Ansible playbook to install Nginx on 50 EC2 instances with one command.",
        "why_it_matters": "Fundamental DevOps skill used in almost every infrastructure automation environment."
    },
    {
        "category": "ansible",
        "term": "How does Ansible work?",
        "difficulty": 3,
        "formal_definition": "Ansible connects to remote machines over SSH (Linux) or WinRM (Windows), pushes modules to them, executes those modules locally on the target machine, and removes them after execution.",
        "simple_definition": "It SSHs into servers, runs tasks, and leaves—no agents needed.",
        "example": "Ansible connects to a server via SSH, copies the 'yum' module, installs Docker, and exits.",
        "why_it_matters": "Understanding the control-flow is key for debugging failures and designing scalable automation."
    },
    {
        "category": "ansible",
        "term": "What is Ansible Galaxy?",
        "difficulty": 3,
        "formal_definition": "Ansible Galaxy is the central repository for community-contributed Ansible roles and collections.",
        "simple_definition": "A marketplace where you download reusable Ansible roles.",
        "example": "Installing the official 'geerlingguy.nginx' role instead of writing your own.",
        "why_it_matters": "Saves massive time by reusing high-quality community automation."
    },
    {
        "category": "ansible",
        "term": "What are Ansible handlers?",
        "difficulty": 3,
        "formal_definition": "Handlers are special tasks that run only when notified, typically used for operations like restarting services.",
        "simple_definition": "Tasks that run only when something changes.",
        "example": "Restarting Nginx only if its config file changed.",
        "why_it_matters": "Prevents unnecessary restarts and enables idempotent automation."
    },
    {
        "category": "ansible",
        "term": "What is Ansible Vault?",
        "difficulty": 3,
        "formal_definition": "Ansible Vault is a feature that allows encrypting sensitive data such as passwords, API keys, and variables used in playbooks.",
        "simple_definition": "Encrypts secrets inside Ansible.",
        "example": "Encrypting a file containing your AWS credentials.",
        "why_it_matters": "Essential for security and compliance in production automation."
    },
    {
        "category": "ansible",
        "term": "What are Ansible collections?",
        "difficulty": 3,
        "formal_definition": "Collections are a distribution format for Ansible content that bundle roles, modules, and plugins into a single package.",
        "simple_definition": "Bundles of roles, plugins, and modules shipped together.",
        "example": "Using the 'amazon.aws' collection for AWS automation.",
        "why_it_matters": "Modern way to distribute scalable, versioned automation assets."
    },
    {
        "category": "anssible",
        "term": "How do you get a list of predefined Ansible variables?",
        "difficulty": 3,
        "formal_definition": "You can access predefined Ansible variables using the `setup` module or by printing hostvars and facts in a play.",
        "simple_definition": "Use `ansible -m setup` to see facts and built-in variables.",
        "example": "`ansible all -m setup | grep ansible_distribution`",
        "why_it_matters": "Critical for dynamic playbooks that adapt to OS, hardware, or environment."
    },
    {
        "category": "ansible",
        "term": "How is a playbook different from ad-hoc commands?",
        "difficulty": 3,
        "formal_definition": "Ad-hoc commands perform one-off tasks, while playbooks define structured, repeatable automation workflows written in YAML.",
        "simple_definition": "Ad-hoc = one command. Playbook = repeatable automation.",
        "example": "Ad-hoc: install nginx once. Playbook: configure entire server setup.",
        "why_it_matters": "Playbooks are the real power of Ansible—reusable, version-controlled automation."
    },
    {
        "category": "ansible",
        "term": "How do you secure secrets in Ansible?",
        "difficulty": 3,
        "formal_definition": "The recommended method is using Ansible Vault to encrypt sensitive files or variables.",
        "simple_definition": "Use Ansible Vault to encrypt secrets.",
        "example": "`ansible-vault encrypt vars/secret.yml`",
        "why_it_matters": "Secrets must not be stored in plain text in Git or deployments."
    },
    {
        "category": "anssible",
        "term": "What templating language does Ansible use?",
        "difficulty": 3,
        "formal_definition": "Ansible uses the Jinja2 templating language for dynamic configuration files and variable substitution.",
        "simple_definition": "Ansible uses Jinja2 for templates.",
        "example": "A `nginx.conf.j2` template using `{{ server_name }}`",
        "why_it_matters": "Enables dynamic configuration and complex logic."
    },
    {
        "category": "ansible",
        "term": "What protocol does Ansible use to communicate?",
        "difficulty": 3,
        "formal_definition": "Ansible primarily uses SSH for Linux systems and WinRM for Windows hosts.",
        "simple_definition": "SSH for Linux, WinRM for Windows.",
        "example": "Running tasks on EC2 instances completely over SSH.",
        "why_it_matters": "No agent installation → simpler, cheaper, easier maintenance."
    },
    {
        "category": "ansible",
        "term": "What is an inventory file?",
        "difficulty": 3,
        "formal_definition": "The inventory file defines the hosts and groups of hosts that Ansible manages, supporting INI, YAML, and dynamic inventory sources.",
        "simple_definition": "A file that lists your servers.",
        "example": "`[web]\nserver1\nserver2`",
        "why_it_matters": "Core to defining the infrastructure Ansible will automate."
    },
    {
        "category": "ansible",
        "term": "What are some Ansible best practices?",
        "difficulty": 4,
        "formal_definition": "Best practices include using roles, separating variables, version-controlling inventory, using handlers for idempotency, encrypting secrets, and organizing playbooks cleanly.",
        "simple_definition": "Use roles, keep things modular, encrypt secrets, and avoid giant playbooks.",
        "example": "Breaking a server setup into roles: nginx/, firewall/, users/",
        "why_it_matters": "Makes automation scalable, maintainable, and production-ready."
    },
    {
        "category": "ansible",
        "term": "How do you handle errors in Ansible?",
        "difficulty": 4,
        "formal_definition": "Error handling can be implemented using `ignore_errors`, `failed_when`, `block-rescue-always`, and conditional checks.",
        "simple_definition": "Use blocks, rescue, failed_when, and ignore_errors when needed.",
        "example": "Retrying a failed API call using block/rescue.",
        "why_it_matters": "Allows resilient, predictable automation pipelines."
    },
    {
        "category": "ansible",
        "term": "How do you test Ansible roles?",
        "difficulty": 4,
        "formal_definition": "Testing is typically done using Molecule, which runs roles against local or containerized environments and verifies outputs.",
        "simple_definition": "Use Molecule to test roles in containers or VMs.",
        "example": "`molecule test` → creates container → runs role → asserts tasks.",
        "why_it_matters": "Testing prevents breakage in CI/CD and production."
    },
    {
        "category": "ansible",
        "term": "What is Molecule and how does it work?",
        "difficulty": 4,
        "formal_definition": "Molecule is a testing framework for Ansible that supports multiple drivers (Docker, Vagrant, EC2) to verify roles through scenarios.",
        "simple_definition": "A tool that tests Ansible roles using containers.",
        "example": "Testing an Nginx role using Molecule + Docker.",
        "why_it_matters": "Critical for professional-grade infrastructure automation testing."
    }
]
