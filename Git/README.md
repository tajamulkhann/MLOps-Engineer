## Most Important Git Commands

| **Command**                         | **Use (1-line)**                                          |
| ----------------------------------- | --------------------------------------------------------- |
| `git init`                          | Initialize a new Git repository.                          |
| `git clone <url>`                   | Copy an existing remote repository to your system.        |
| `git status`                        | Show current file state (untracked, modified, staged).    |
| `git add .`                         | Stage all changes for the next commit.                    |
| `git commit -m "message"`           | Save staged changes with a message.                       |
| `git push`                          | Upload local commits to the remote repository.            |
| `git pull`                          | Download and merge latest changes from remote.            |
| `git branch`                        | List all branches or create a new one.                    |
| `git checkout <branch>`             | Switch to a different branch.                             |
| `git checkout -b <branch>`          | Create and switch to a new branch.                        |
| `git merge <branch>`                | Merge another branch into the current one.                |
| `git remote add origin <url>`       | Link local repository to a remote origin (e.g., GitHub).  |
| `git log`                           | View commit history.                                      |
| `git branch -d <branch>`            | Delete a local branch (only if already merged).           |
| `git branch -D <branch>`            | Force delete a local branch (even if not merged).         |
| `git push origin --delete <branch>` | Delete a branch from remote (GitHub).                     |
| `git pull origin main`              | Get the latest updates from remote `main` before merging. |
| `git merge dev`                     | Merge `dev` branch into current branch (usually `main`).  |
| `git push origin main`              | Push the updated `main` branch to GitHub after merging.   |

### Merging Dev into Main

1. Switch to main branch
git checkout main

2. Get latest updates
git pull origin main

3. Merge dev into main
git merge dev

4. Push updated main to GitHub
git push origin main

