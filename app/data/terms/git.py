git = [

    # ---------------------- Difficulty 1 ----------------------
    {
        "category": "git",
        "term": "What is Git?",
        "difficulty": 1,
        "formal_definition": "Git is a distributed version control system that tracks changes in source code over time.",
        "simple_definition": "A tool that saves versions of your project so you can go back in time.",
        "example": "git add, git commit, git push",
        "why_it_matters": "Git is required for all software engineering workflows."
    },
    {
        "category": "git",
        "term": "What is a Git repository?",
        "difficulty": 1,
        "formal_definition": "A Git repository is a directory tracked by Git that contains a project and its entire version history.",
        "simple_definition": "A folder Git tracks for changes.",
        "example": "git init creates a repository.",
        "why_it_matters": "Everything in Git starts with a repo."
    },
    {
        "category": "git",
        "term": "Basic Git workflow",
        "difficulty": 1,
        "formal_definition": "The core Git workflow consists of staging changes, committing them, and syncing with a remote repository.",
        "simple_definition": "Add → Commit → Push.",
        "example": "git add . → git commit → git push",
        "why_it_matters": "This is the foundation of using Git."
    },

    # ---------------------- Difficulty 2 ----------------------
    {
        "category": "git",
        "term": "Difference between Git and SVN",
        "difficulty": 2,
        "formal_definition": "Git is distributed, meaning each user has a full copy of the repo. SVN is centralized with one main server.",
        "simple_definition": "Git = distributed. SVN = centralized.",
        "example": "You can commit locally in Git without Internet.",
        "why_it_matters": "Shows understanding of modern vs legacy version control."
    },
    {
        "category": "git",
        "term": "Difference between git pull and git fetch",
        "difficulty": 2,
        "formal_definition": "git fetch downloads changes from the remote without applying them; git pull downloads AND merges them into your current branch.",
        "simple_definition": "fetch = download only; pull = download + merge.",
        "example": "git fetch origin main",
        "why_it_matters": "Important to avoid accidentally overwriting work."
    },
    {
        "category": "git",
        "term": "What is the HEAD in Git?",
        "difficulty": 2,
        "formal_definition": "HEAD is a pointer that represents your current branch reference and the snapshot you are working on.",
        "simple_definition": "The commit you're currently on.",
        "example": "HEAD → main → latest commit",
        "why_it_matters": "Required to understand commits, reset, rebase, etc."
    },
    {
        "category": "git",
        "term": "What is git cherry-pick?",
        "difficulty": 2,
        "formal_definition": "Cherry-pick applies a specific commit from one branch onto another.",
        "simple_definition": "Copy one commit from another branch.",
        "example": "git cherry-pick <commit>",
        "why_it_matters": "Useful for fixing bugs without merging full branches."
    },
    {
        "category": "git",
        "term": "What is git stash?",
        "difficulty": 2,
        "formal_definition": "git stash saves uncommitted changes temporarily without committing them to the branch.",
        "simple_definition": "Hide your changes for later.",
        "example": "git stash → git stash pop",
        "why_it_matters": "Prevents losing work when switching branches."
    },
    {
        "category": "git",
        "term": "Difference between git stash apply and git stash pop",
        "difficulty": 2,
        "formal_definition": "apply restores stashed changes without deleting them; pop restores AND deletes the stash.",
        "simple_definition": "apply keeps the stash; pop removes it.",
        "example": "git stash pop",
        "why_it_matters": "Common in multi-branch development."
    },

    # ---------------------- Difficulty 3 ----------------------
    {
        "category": "git",
        "term": "What does git reset do?",
        "difficulty": 3,
        "formal_definition": "git reset moves the current branch pointer (HEAD) to a specified commit, optionally modifying the staging area and working directory.",
        "simple_definition": "Moves your project pointer backwards.",
        "example": "git reset --hard HEAD~1",
        "why_it_matters": "Reset is powerful and dangerous—must understand before using."
    },
    {
        "category": "git",
        "term": "What is a fork, clone, and branch?",
        "difficulty": 3,
        "formal_definition": "A fork copies a repo to your account, clone copies it locally, and branch creates parallel lines of development.",
        "simple_definition": "Fork = your own copy; Clone = local copy; Branch = a new line of work.",
        "example": "git clone https://github.com/user/repo",
        "why_it_matters": "Fundamental for open-source and team workflows."
    },
    {
        "category": "git",
        "term": "Updating your local repo",
        "difficulty": 3,
        "formal_definition": "Fetching and merging remote changes into your local branch.",
        "simple_definition": "Pull new changes from GitHub.",
        "example": "git pull origin main",
        "why_it_matters": "Prevents you from working on stale code."
    },
    {
        "category": "git",
        "term": "Rollback to a previous commit",
        "difficulty": 3,
        "formal_definition": "You can reset the HEAD pointer or revert a commit depending on whether you want to rewrite history.",
        "simple_definition": "Go back to an earlier version.",
        "example": "git reset --hard <commit>",
        "why_it_matters": "Critical for fixing broken codebases safely."
    },
    {
        "category": "git",
        "term": "How to amend a commit",
        "difficulty": 3,
        "formal_definition": "git commit --amend modifies the most recent commit (message or content).",
        "simple_definition": "Edit the last commit.",
        "example": "git commit --amend -m 'Updated message'",
        "why_it_matters": "Useful for quick mistakes before pushing."
    },

    # ---------------------- Difficulty 4 ----------------------
    {
        "category": "git",
        "term": "Difference between two commits",
        "difficulty": 4,
        "formal_definition": "git diff compares the changes between commits, branches, or working states.",
        "simple_definition": "See what's different between versions.",
        "example": "git diff commit1 commit2",
        "why_it_matters": "Used constantly in PR reviews."
    },
    {
        "category": "git",
        "term": "When to use git rebase vs merge",
        "difficulty": 4,
        "formal_definition": "Rebase rewrites history by applying commits on top of another base; merge combines histories preserving commit order.",
        "simple_definition": "Rebase = clean history. Merge = preserve history.",
        "example": "git rebase main",
        "why_it_matters": "Essential for clean, readable commit histories."
    },
    {
        "category": "git",
        "term": "Undo a rebase",
        "difficulty": 4,
        "formal_definition": "You can undo an active rebase using git rebase --abort or recover using reflog.",
        "simple_definition": "Stop a rebase and go back to before it started.",
        "example": "git rebase --abort",
        "why_it_matters": "Important when resolving complex conflicts."
    },
    {
        "category": "git",
        "term": "Syncing stale branches",
        "difficulty": 4,
        "formal_definition": "You update a stale branch by fetching remote changes and rebasing or merging them.",
        "simple_definition": "Bring your branch up to date with main.",
        "example": "git fetch origin → git rebase origin/main",
        "why_it_matters": "Critical for team workflows."
    },

    # ---------------------- Difficulty 5 (Advanced) ----------------------
    {
        "category": "git",
        "term": "Git reflog",
        "difficulty": 5,
        "formal_definition": "Reflog records all movements of HEAD, enabling recovery of lost commits or branches.",
        "simple_definition": "Git’s undo button for almost everything.",
        "example": "git reflog → find lost commit",
        "why_it_matters": "Every senior engineer uses reflog to recover disasters."
    },
    {
        "category": "git",
        "term": "Git hooks",
        "difficulty": 5,
        "formal_definition": "Git hooks are scripts triggered by events such as committing, pushing, or merging to automate workflows.",
        "simple_definition": "Scripts Git runs automatically on certain actions.",
        "example": "pre-commit hook for linting.",
        "why_it_matters": "Used in CI, linting, security, and team policies."
    },
    {
        "category": "git",
        "term": "Squashing commits",
        "difficulty": 5,
        "formal_definition": "Squashing condenses multiple commits into one using interactive rebase.",
        "simple_definition": "Combine several commits into one before merging.",
        "example": "git rebase -i HEAD~5",
        "why_it_matters": "Creates clean, readable pull requests."
    }
]
