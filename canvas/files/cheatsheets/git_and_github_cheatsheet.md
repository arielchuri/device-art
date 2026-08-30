# Git, GitHub & GitHub Desktop Cheat Sheet

---

## 1. What is Git vs. GitHub?

- **Git**: A local, open-source version control tool installed on your computer. It tracks the chronological history of changes made to your files, allowing you to create checkpoints ("commits") and roll back mistakes.
- **GitHub**: A cloud hosting platform for Git repositories. It lets you store your code off-site, collaborate with others, publish open-source documentation, and back up your physical computing projects.
- **GitHub Desktop**: A visual application (GUI) that lets you interact with Git and GitHub seamlessly through buttons and visual file diffs, without needing to type terminal commands.

---

## 2. Core Concepts: The Git Lifecycle

```
[ Working Directory ] ──( Stage & Commit )──> [ Local History ] ──( Push )──> [ GitHub Cloud ]
```

1. **Repository (Repo)**: The master project folder containing all your files and the complete tracking history.
2. **Commit**: A permanent snapshot of your project at a specific moment in time, accompanied by a short description message explaining *what* changed.
3. **Push**: Sending your local commits up to GitHub in the cloud.
4. **Pull / Fetch**: Downloading the latest changes and commits from GitHub to your computer.
5. **Clone**: Making a full local copy of a remote GitHub repository on your hard drive for the first time.

---

## 3. GitHub Desktop Workflow (Visual Guide)

### Action 1: Cloning a Repository
1. Open **GitHub Desktop**.
2. Click **File $\to$ Clone Repository...** (or press `Cmd + Shift + O` on Mac / `Ctrl + Shift + O` on Windows).
3. Click the **URL** tab and paste the repository web link:
   ```
   https://github.com/arielchuri/device-art
   ```
4. Choose a **Local Path** on your laptop (e.g. `~/Documents/device-art`).
5. Click **Clone**.

---

### Action 2: Making Changes & Creating a Commit
1. Edit or add files in your project folder using VS Code, Cursor, `nano`, or any text editor.
2. Open **GitHub Desktop**. In the left sidebar under **Changes**, you will see a list of modified files with green (added) and red (deleted) lines.
3. At the bottom left, type a concise **Summary Commit Message** in the title box:
   * *(e.g. `Add Python age check script with comments`)*
4. Click the blue button: **Commit to main**.

---

### Action 3: Pushing Your Changes to GitHub
1. Look at the top bar in GitHub Desktop.
2. Click **Push origin** (or press `Cmd + P` / `Ctrl + P`).
3. Your local commits are now securely backed up on GitHub!

---

### Action 4: Pulling Updates (Getting Latest Course Materials)
1. At the start of each studio class, open GitHub Desktop.
2. Click **Fetch origin** at the top bar.
3. If new instructor slides or code examples have been added, click **Pull origin** to update your laptop.

---

## 4. Terminal Git Quick Reference (For Command-Line Users)

If you prefer using the terminal (Terminal or Ghostty), here are the essential equivalent commands:

| Action | Terminal Command | Description |
| :--- | :--- | :--- |
| **Check Status** | `git status` | Shows which files are modified or untracked |
| **Stage All Changes** | `git add .` | Stages all current changes for commit |
| **Create Commit** | `git commit -m "Your message"` | Creates a snapshot with a description |
| **Push to Cloud** | `git push` | Uploads local commits to GitHub |
| **Pull from Cloud** | `git pull` | Downloads latest commits from GitHub |
| **Clone Repo** | `git clone <URL>` | Downloads a new repository to your laptop |

---

## 5. Best Practices for Device Art & Creative Code

- **Write Meaningful Commit Messages**: State *what* was changed (e.g. `Add photoresistor voltage divider calculations` instead of `stuff`).
- **Commit Often**: Make a commit whenever you finish a working feature, fix a bug, or finish a studio lab step.
- **Never Commit Sensitive Keys**: Never commit Wi-Fi passwords, private API tokens, or canvas secrets to public repositories (use a `.env` file and `.gitignore`).
