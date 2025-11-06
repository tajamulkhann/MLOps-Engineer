# Most Important Git Commands (Interview)

| **Step**               | **Command**                        | **Purpose / Explanation**                      |
| ---------------------- | ---------------------------------- | ---------------------------------------------- |
| **Main Branch Setup**  |                                    |                                                |
| 1                      | `git init`                         | Initialize a new Git repository.               |
| 2                      | `git add .`                        | Stage all files (or `git add <file>`).         |
| 3                      | `git commit -m "Initial commit"`   | Save a snapshot of staged changes.             |
| 4                      | `git remote add origin <repo-URL>` | Link local repo to remote GitHub repository.   |
| 5                      | `git push origin main`             | Push local `main` branch to remote.            |
| **Branch Workflow**    |                                    |                                                |
| 6                      | `git branch`                       | List all branches (optional).                  |
| 7                      | `git checkout -b dev`              | Create and switch to new branch `dev`.         |
| —                      | *(or)* `git checkout dev`          | Switch to existing branch.                     |
| 8                      | `git add .`                        | Stage changes in the `dev` branch.             |
| 9                      | `git commit -m "Work done in dev"` | Commit changes to `dev`.                       |
| 10                     | `git push origin dev`              | Push `dev` branch to remote.                   |
| **Merge Back to Main** |                                    |                                                |
| 11                     | `git checkout main`                | Switch to `main` branch.                       |
| 12                     | `git pull origin main`             | Get latest updates from remote before merging. |
| 13                     | `git merge dev`                    | Merge `dev` branch into `main`.                |
| 14                     | `git push origin main`             | Push updated `main` branch to remote.          |
| **Useful Extras**      |                                    |                                                |
| —                      | `git status`                       | Show tracked/untracked and staged changes.     |
| —                      | `git log`                          | Show commit history.                           |
| —                      | `git diff`                         | Show file differences.                         |
| —                      | `git diff main..dev`               | Show differences between main and dev          |

## How to delete Branches ?
| Task                        | Command                        |
| --------------------------- | ------------------------------ |
| Delete local branch (safe)  | `git branch -d dev`            |
| Delete local branch (force) | `git branch -D dev`            |
| Delete remote branch        | `git push origin --delete dev` |

## Git Status Codes
| **VS Code Symbol/Color** | **Terminal Symbol** | **Meaning (Simple Explanation)**                        |
| ------------------------ | ------------------- | ------------------------------------------------------- |
| **U (Green)**            | `??`                | Untracked file — Git sees it but isn’t tracking it yet. |
| **A (Green)**            | `A`                 | Added/Staged — file is ready to be committed.           |
| **M (Yellow/Blue)**      | `M` (red)           | Modified but unstaged — file changed but not added.     |
| **M (Green)**            | `M` (green)         | Modified and staged — file changed and added to commit. |
| **D (Red)**              | `D`                 | Deleted — file was removed from working directory.      |
| **R (Green/Yellow)**     | `R`                 | Renamed — file was moved or renamed.                    |
