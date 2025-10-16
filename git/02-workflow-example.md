Workflow-Example: Default Git Development Workflow

---

## Introduction

This document illustrates a **default Git workflow** for development projects.  
It guides developers on how to **organize, track, and collaborate** using Git and GitHub.

---

## 1. Setup

### Clone an existing repository
```bash
git clone {repository-url}
cd {repository-folder}
```

### Check Git version
```bash
git --version
```

---

## 2. Create a Feature Branch

Always work on a **separate branch** for new features or bug fixes:
```bash
git checkout -b feature/my-feature
```

- `feature/my-feature` is a descriptive branch name.
- Keep the `main` or `master` branch clean.

---

## 3. Make Changes Locally

1. **Check repository status**:
```bash
git status
```

2. **Edit files** in your code editor.

3. **View changes before staging**:
```bash
git diff
```

---

## 4. Stage and Commit Changes

### Stage changes
```bash
git add .
```
or stage specific files:
```bash
git add file1.java file2.java
```

### Commit changes with a message
```bash
git commit -m "Add feature X implementation"
```

- Write clear and concise commit messages.

---

## 5. Synchronize with Remote

### Fetch updates from remote
```bash
git fetch
```

### Rebase your branch on top of remote main
```bash
git pull --rebase origin main
```

- Avoid unnecessary merge commits.

---

## 6. Push Changes to Remote

```bash
git push origin feature/my-feature
```

- This makes your branch available to the team.

---

## 7. Create a Pull Request (PR)

1. Go to GitHub and open a **pull request** from your branch to `main`.
2. Describe the changes clearly.
3. Assign reviewers if required.

---

## 8. Merge Changes

- After review, merge the PR into `main`.
- Delete your feature branch to keep the repository clean:
```bash
git branch -d feature/my-feature
git push origin --delete feature/my-feature
```

---

## 9. Update Local Main

After merges, always keep your local main up-to-date:
```bash
git checkout main
git pull origin main
```

---

## 10. Undo Mistakes (Optional)

### Unstage a file
```bash
git reset HEAD file.txt
```

### Discard all local changes (hard reset)
```bash
git reset --hard HEAD
```

- Use carefully: **this will remove all uncommitted changes**.

---

## Summary Workflow Diagram

```text
clone → checkout -b feature → edit → add → commit → fetch → pull --rebase → push → PR → merge → delete branch → update main
```

---

## Notes

- Keep commits **small and focused**.
- Use **branches for features or fixes**.
- Regularly **sync with remote main** to avoid conflicts.
- Follow team conventions for **branch names, commit messages, and PR reviews**.
