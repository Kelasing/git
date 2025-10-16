# Git Commands Cheat Sheet

---

*Copies a repository from a remote location like GitHub to your local machine.*

```bash
git clone {repository}
```

*Initializes a new Git repository in the current folder.*

```bash
git init
```

*Stages files to include in the next commit.*

```bash
git add {files / .}
```

*Records staged changes in the repository with a descriptive message.*

```bash
git commit -m "{msg}"
```

*Uploads local commits to the remote repository.*

```bash
git push origin {branch}
```

*Fetches and merges changes from the remote repository into your current branch.*

```bash
git pull
```

*Displays the current state of your working directory and staging area.*

```bash
git status
```

*Lists, creates, or deletes branches in the repository.*

```bash
git branch
```

*Shows a compact view of the commit history.*

```bash
git log --oneline
```

*Displays the installed Git version.*

```bash
git --version
```

*Connects your local repository to a remote repository.*

```bash
git remote add origin {url}
```

*Lists all remote repositories and their URLs.*

```bash
git remote -v
```

*Updates your branch by applying remote changes on top of your local commits to avoid unnecessary merge commits.*

```bash
git pull --rebase
```

*Downloads updates from the remote repository without merging them.*

```bash
git fetch
```

*Creates a new branch and switches to it immediately.*

```bash
git checkout -b {branch}
```

*Discards all local changes and resets the repository to the last commit.*

```bash
git reset --hard HEAD
```

*Shows changes in files that are not yet staged for commit.*

```bash
git diff
```
