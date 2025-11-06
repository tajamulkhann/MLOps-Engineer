## Most Important Git Commands

| **Step**                                         | **Command**                        | **Purpose / Explanation**                                |
| ------------------------------------------------ | ---------------------------------- | -------------------------------------------------------- |
| **Main Branch Setup**                         |                                    |                                                          |
| 1                                                | `git init`                         | Initialize a new Git repository locally.                 |
| 2                                                | `git add .`                        | Stage all files (or `git add <file>` to stage specific). |
| 3                                                | `git commit -m "Initial commit"`   | Save changes into Git history.                           |
| 4                                                | `git remote add origin <repo-URL>` | Connect local repo to GitHub remote.                     |
| 5                                                | `git push origin main`             | Push changes to the `main` branch on remote.             |
| **Branch Workflow (Development)**             |                                    |                                                          |
| 6                                                | `git branch`                       | View all branches.                                       |
| 7                                                | `git checkout -b dev`              | Create and switch to a new branch `dev`.                 |
| —                                                | *(or)* `git checkout dev`          | Switch to an existing branch.                            |
| 8                                                | `git add .`                        | Stage files in the `dev` branch.                         |
| 9                                                | `git commit -m "Work done in dev"` | Commit work done in the `dev` branch.                    |
| 10                                               | `git push origin dev`              | Push `dev` branch to the remote repository.              |
| **Merging dev into main**                     |                                    |                                                          |
| 11                                               | `git checkout main`                | Switch back to `main`.                                   |
| 12                                               | `git pull origin main`             | Update local main with latest remote code.               |
| 13                                               | `git merge dev`                    | Merge `dev` branch changes into `main`.                  |
| 14                                               | `git push origin main`             | Push merged changes to GitHub.                           |
| **Compare Branches (Before Merge or Review)** |                                    |                                                          |
| 15                                               | `git diff main..dev`               | Show differences between `main` and `dev` branches.      |

