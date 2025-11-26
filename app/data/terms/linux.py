linux = [
    {
        "category": "linux",
        "term": "What is Linux and how is it different from UNIX?",
        "formal_definition": "Linux is an open-source operating system kernel inspired by UNIX. Unlike proprietary UNIX systems, Linux distributions are free, community-driven, and run on a wide range of hardware.",
        "simple_definition": "Linux = free, open-source version of UNIX.",
        "example": "Ubuntu, CentOS, Fedora all run the Linux kernel.",
        "difficulty": 3,
        "why_it_matters": "Linux is the dominant OS for servers, DevOps, cloud, and containers."
    },
    {
        "category": "linux",
        "term": "What is the Linux kernel?",
        "formal_definition": "The Linux kernel is the core of the operating system that manages hardware, processes, memory, security, and device drivers.",
        "simple_definition": "It's the brain of the OS that talks to hardware.",
        "example": "When a process requests memory, the kernel manages allocation.",
        "difficulty": 3,
        "why_it_matters": "Understanding the kernel helps with troubleshooting, performance tuning, and container fundamentals."
    },
    {
        "category": "linux",
        "term": "What are inodes?",
        "formal_definition": "An inode is a data structure in Linux filesystems that stores metadata about a file—except its name.",
        "simple_definition": "Inodes store file details like size and permissions.",
        "example": "`ls -i` displays inode numbers.",
        "difficulty": 3,
        "why_it_matters": "Critical for storage troubleshooting and filesystem design."
    },
    {
        "category": "linux",
        "term": "Explain the Linux boot process.",
        "formal_definition": "The Linux boot sequence includes BIOS/UEFI → Bootloader (GRUB) → Kernel load → init/systemd startup → services start.",
        "simple_definition": "How Linux turns on and loads processes.",
        "example": "If GRUB is corrupted, the system cannot find the kernel.",
        "difficulty": 4,
        "why_it_matters": "Essential for debugging boot failures and server recoveries."
    },
    {
        "category": "linux",
        "term": "What is a zombie process?",
        "formal_definition": "A zombie process is a terminated process that still has an entry in the process table because its parent has not read its exit status.",
        "simple_definition": "A dead process that hasn’t fully cleaned up.",
        "example": "`ps aux | grep Z` shows zombie processes.",
        "difficulty": 3,
        "why_it_matters": "Too many zombies can exhaust process table entries."
    },
    {
        "category": "linux",
        "term": "Soft link vs hard link",
        "formal_definition": "A soft link (symlink) is a pointer to a file path. A hard link is a reference to the same inode as the original file.",
        "simple_definition": "Soft link = shortcut. Hard link = duplicate reference.",
        "example": "`ln -s file.txt link.txt` creates a soft link.",
        "difficulty": 3,
        "why_it_matters": "Common interview topic for filesystem fundamentals."
    },
    {
        "category": "linux",
        "term": "What are namespaces and cgroups?",
        "formal_definition": "Namespaces isolate system resources per process (PID, network, filesystem). cgroups control resource usage (CPU, memory).",
        "simple_definition": "Namespaces = isolation. cgroups = resource limits.",
        "example": "Docker uses namespaces + cgroups to create containers.",
        "difficulty": 4,
        "why_it_matters": "Core to containerization (Docker, Kubernetes)."
    },
    {
        "category": "linux",
        "term": "What are Linux file permissions?",
        "formal_definition": "Linux permissions specify read, write, and execute access for owner, group, and others.",
        "simple_definition": "Controls who can read/write/execute a file.",
        "example": "`chmod 755 script.sh`",
        "difficulty": 2,
        "why_it_matters": "Essential for security and deployment."
    },
    {
        "category": "linux",
        "term": "What is swap space?",
        "formal_definition": "Swap space is a portion of disk used when system memory (RAM) is full.",
        "simple_definition": "Overflow memory stored on disk.",
        "example": "`free -h` shows swap usage.",
        "difficulty": 2,
        "why_it_matters": "Affects performance and troubleshooting."
    },
    {
        "category": "linux",
        "term": "What are cron jobs?",
        "formal_definition": "Cron jobs are scheduled tasks executed automatically at specified intervals.",
        "simple_definition": "Automated scheduled tasks.",
        "example": "`crontab -e` to edit jobs.",
        "difficulty": 2,
        "why_it_matters": "Used heavily in automation and DevOps pipelines."
    }
]
